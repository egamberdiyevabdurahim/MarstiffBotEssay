from database_config.db_settings import execute_query


class EssentialsModel:
    def __init__(
            self,
            idn = None,
            key = None,
            val = None,
            created_at = None,
    ):
        self.idn = idn
        self.key = key
        self.val = val
        self.created_at = created_at

    @classmethod
    async def get_table_name(cls):
        return 'essentials_model'

    @classmethod
    async def create_table(cls):
        query = f"""
        CREATE TABLE IF NOT EXISTS {await cls.get_table_name()} (
            idn SERIAL PRIMARY KEY,
            key VARCHAR(250),
            val VARCHAR(250),
            created_at TIMESTAMPTZ DEFAULT timezone('Asia/Tashkent', NOW())
        )
        """
        await execute_query(query=query)
        return None

    @classmethod
    async def create(
            cls,
            key,
            val,
    ):
        query = f"""
        INSERT INTO {await cls.get_table_name()}
        (key, val)
        VALUES ($1, $2)
        """
        return await execute_query(
            query=query,
            params=(key, val)
        )

    @classmethod
    async def get_data(cls, idn):
        query = f"""
        SELECT *
        FROM {await cls.get_table_name()}
        WHERE idn=$1
        """
        result = await execute_query(
            query=query,
            params=(int(idn),),
            fetch='one'
        )
        if result:
            return cls(**result)
        return None

    @classmethod
    async def get_all(cls):
        query = f"""
        SELECT *
        FROM {await cls.get_table_name()}
        """
        result = await execute_query(
            query=query,
            fetch='all'
        )
        return [cls(**item) for item in result] if result else []

    @classmethod
    async def get_by_key(cls, key):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE key=$1
            """
        result = await execute_query(
            query=query,
            params=(key,),
            fetch='one'
        )
        if result:
            return cls(**result)
        return None