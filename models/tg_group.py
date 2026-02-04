from database_config.db_settings import execute_query


class TGGroupModel:
    def __init__(
            self,
            idn = None,
            group_id = None,
            status = None,
            created_at = None,
    ):
        self.idn = idn
        self.group_id = group_id
        self.status = status
        self.created_at = created_at

    @classmethod
    async def get_table_name(cls):
        return 'tg_group_model'

    @classmethod
    async def create_table(cls):
        query = f"""
        CREATE TABLE IF NOT EXISTS {await cls.get_table_name()} (
            idn SERIAL PRIMARY KEY,
            group_id TEXT,
            status SMALLINT,
            created_at TIMESTAMPTZ DEFAULT timezone('Asia/Tashkent', NOW())
        )
        """
        await execute_query(query=query)
        return None

    @classmethod
    async def create(
            cls,
            group_id,
            status,
    ):
        query = f"""
        INSERT INTO {await cls.get_table_name()}
        (group_id, status)
        VALUES ($1, $2)
        """
        return await execute_query(
            query=query,
            params=(group_id, status)
        )

    async def save(self):
        query = f"""
        UPDATE {await self.get_table_name()}
        SET group_id=$1, status=$2
        WHERE idn=$3
        """
        await execute_query(
            query,
            params=(
                self.group_id, self.status, self.idn
            )
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
    async def get_by_chat_id(cls, chat_id):
        query = f"""
                SELECT *
                FROM {await cls.get_table_name()}
                WHERE group_id=$1
                """
        result = await execute_query(
            query=query,
            params=(str(chat_id),),
            fetch='one'
        )
        if result:
            return cls(**result)
        return None
