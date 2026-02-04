from database_config.db_settings import execute_query


class TGGroupSectionModel:
    def __init__(
            self,
            idn = None,
            group_idn = None,
            section_id = None,
            type_connected = None,
            status = None,
            created_at = None,
    ):
        self.idn = idn
        self.group_idn = group_idn
        self.section_id = section_id
        self.type_connected = type_connected
        self.status = status
        self.created_at = created_at

    @classmethod
    async def get_table_name(cls):
        return 'tg_group_section_model'

    @classmethod
    async def create_table(cls):
        query = f"""
        CREATE TABLE IF NOT EXISTS {await cls.get_table_name()} (
            idn SERIAL PRIMARY KEY,
            group_idn INT,
            section_id INT,
            type_connected SMALLINT,
            status SMALLINT,
            created_at TIMESTAMPTZ DEFAULT timezone('Asia/Tashkent', NOW())
        )
        """
        await execute_query(query=query)
        return None

    @classmethod
    async def create(
            cls,
            group_idn,
            section_id,
            type_connected,
            status,
    ):
        query = f"""
        INSERT INTO {await cls.get_table_name()}
        (group_idn, section_id, type_connected, status)
        VALUES ($1, $2, $3, $4)
        """
        return await execute_query(
            query=query,
            params=(group_idn, section_id, type_connected, status)
        )

    async def save(self):
        query = f"""
        UPDATE {await self.get_table_name()}
        SET group_idn=$1, section_id=$2, type_connected=$3, status=$4
        WHERE idn=$5
        """
        await execute_query(
            query,
            params=(
                self.group_idn, self.section_id, self.type_connected, self.status, self.idn
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
    async def get_by_type_connected(cls, type_connected):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE type_connected=$1
            """
        result = await execute_query(
            query=query,
            params=(int(type_connected),),
            fetch='all'
        )
        return [cls(**item) for item in result] if result else []

    @classmethod
    async def get_by_group(cls, group):
        query = f"""
                SELECT *
                FROM {await cls.get_table_name()}
                WHERE group_idn=$1
                """
        result = await execute_query(
            query=query,
            params=(int(group),),
            fetch='all'
        )
        return [cls(**item) for item in result] if result else []

    @classmethod
    async def get_data_by_type_connected_group(cls, group_idn, type_connected):
        query = f"""
        SELECT *
        FROM {await cls.get_table_name()}
        WHERE group_idn=$1 AND type_connected=$2
        """
        result = await execute_query(
            query=query,
            params=(group_idn, type_connected),
            fetch='one'
        )
        if result:
            return cls(**result)
        return None