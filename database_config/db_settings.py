import asyncpg
import logging
from contextlib import asynccontextmanager
from database_config.config import DB_CONFIG
import time


class Database:
    def __init__(self):
        self.pool = None
        self.query_stats = {"total": 0, "errors": 0, "slow_queries": []}
        self.SLOW_QUERY_THRESHOLD = 1.0  # seconds

    async def create_pool(self):
        """Create connection pool with optimized settings"""
        self.pool = await asyncpg.create_pool(
            **DB_CONFIG,
            min_size=5,  # Keep 5 connections ready
            max_size=30,  # Max 30 connections for 1000+ users
            max_queries=50000,  # Close connections after 50k queries
            max_inactive_connection_lifetime=300,  # 5 minutes
            timeout=10,  # 10s to acquire connection
            command_timeout=30,  # 30s query timeout
            statement_cache_size=0,  # Disable statement cache (aiogram handles)
            server_settings={
                'timezone': 'Asia/Tashkent',
                'application_name': 'marstiff_bot'
            }
        )
        logging.info(f"Database pool created: min=5, max=30")

    async def get_stats(self):
        """Get current pool statistics"""
        if not self.pool:
            return {}

        return {
            'size': self.pool._size,
            'min_size': self.pool._min_size,
            'max_size': self.pool._max_size,
            'free': self.pool._free_count(),
            'checkedout': len(self.pool._holders),
            'queries': self.query_stats
        }

    @asynccontextmanager
    async def transaction(self):
        """Context manager for transactions"""
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                yield conn


# Create a single global instance
db = Database()


async def execute_query(query, params=None, fetch=None, conn=None):
    """
    Execute query with performance monitoring

    Args:
        query: SQL query
        params: Query parameters
        fetch: 'all', 'one', 'return', or None for execute
        conn: Optional existing connection (for transactions)
    """
    params = params or ()
    start_time = time.time()

    # If connection provided (for transaction), use it
    if conn:
        connection_context = None
        connection = conn
    else:
        # Ensure pool exists
        if not db.pool:
            await db.create_pool()
        connection_context = db.pool.acquire()
        connection = await connection_context.__aenter__()

    try:
        db.query_stats["total"] += 1

        if fetch == "all":
            result = await connection.fetch(query, *params)
        elif fetch == "one":
            result = await connection.fetchrow(query, *params)
        elif fetch == "return":
            result = await connection.fetchrow(query, *params)
        else:
            await connection.execute(query, *params)
            result = None

        # Log slow queries
        query_time = time.time() - start_time
        if query_time > db.SLOW_QUERY_THRESHOLD:
            db.query_stats["slow_queries"].append({
                "query": query[:200],  # First 200 chars
                "time": query_time,
                "params": params
            })
            logging.warning(f"Slow query ({query_time:.2f}s): {query[:100]}...")

        return result

    except asyncpg.exceptions.TooManyConnectionsError:
        logging.critical("Database connection limit exceeded!")
        # Implement retry logic or queue system
        raise
    except Exception as e:
        db.query_stats["errors"] += 1
        logging.error(f"DB Error: {e} | Query: {query[:100]}...")
        # Don't raise by default - return None for graceful degradation
        return None
    finally:
        if connection_context and not conn:
            await connection_context.__aexit__(None, None, None)


# Add monitoring endpoint
async def monitor_database():
    """Log database stats periodically"""
    stats = await db.get_stats()
    logging.info(f"DB Stats: {stats}")

    # Alert if connection pool is exhausted
    if stats.get('free', 0) == 0 and stats.get('checkedout', 0) >= stats.get('max_size', 0):
        logging.warning("Database connection pool exhausted!")