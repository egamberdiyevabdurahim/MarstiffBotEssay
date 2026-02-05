import asyncpg
import logging
from database_config.config import DB_CONFIG


class Database:
    def __init__(self):
        self.pool = None

    async def create_pool(self):
        # We create the pool once.
        # min_size=1, max_size=10 is usually good for a bot.
        self.pool = await asyncpg.create_pool(**DB_CONFIG, min_size=1, max_size=5)
        logging.info("Database pool created")

    async def close_pool(self):
        if self.pool:
            await self.pool.close()
            logging.info("Database pool closed")

    async def get_connection(self):
        if not self.pool:
            await self.create_pool()
        return self.pool.acquire()


# Create a single global instance
db = Database()


# We update execute_query to use the pool.
# This keeps your existing code working without changing every model file.
async def execute_query(query, params=None, fetch=None):
    params = params or ()

    # Ensure pool exists
    if not db.pool:
        await db.create_pool()

    async with db.pool.acquire() as connection:
        try:
            if fetch == "all":
                result = await connection.fetch(query, *params)
                return result
            elif fetch == "one":
                result = await connection.fetchrow(query, *params)
                return result
            elif fetch == "return":
                # execute_and_fetch replacement
                result = await connection.fetchrow(query, *params)
                return result
            else:
                # Standard execute (INSERT, UPDATE, DELETE)
                await connection.execute(query, *params)
                return None
        except Exception as e:
            logging.error(f"DB Error: {e} | Query: {query}")
            # Optional: Re-raise the error if you want the bot to know it failed
            # raise e
            return None