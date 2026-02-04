from database_config.db_settings import execute_query
from utils.additions import tas_t


class EssayModel:
    def __init__(
            self,
            idn = None,
            video = None,
            cost = None,
            section = None,
            participated = None,
            active = None,
            created_at = None,
            updated_at = None,
            deleted_at = None,
            created_by = None,
            updated_by = None,
            deleted_by = None,
            deleted = None,
    ):
        self.idn = idn
        self.video = video
        self.cost = cost
        self.section = section
        self.participated = participated
        self.active = active
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted_by = deleted_by
        self.deleted = deleted

    @classmethod
    async def get_table_name(cls):
        return 'essay_model'

    @classmethod
    async def create_table(cls):
        query = f"""
            CREATE TABLE IF NOT EXISTS {await cls.get_table_name()} (
                idn SERIAL PRIMARY KEY,
                video TEXT,
                cost FLOAT,
                section INT,
                participated INT,
                active SMALLINT DEFAULT 1,
                created_at TIMESTAMPTZ DEFAULT timezone('Asia/Tashkent', NOW()),
                updated_at TIMESTAMPTZ,
                deleted_at TIMESTAMPTZ,
                created_by INT,
                updated_by INT,
                deleted_by INT,
                deleted SMALLINT DEFAULT 0
            )
        """
        await execute_query(query=query)
        return None

    @classmethod
    async def create(
            cls,
            video=None,
            cost=None,
            section=None,
            active=1,
            created_by=None,
    ):
        query = f"""
        INSERT INTO {await cls.get_table_name()}
        (video, cost, section,
        active, created_by, created_at)
        VALUES ($1,$2,$3,$4,$5,$6)
        """
        return await execute_query(
            query=query,
            params=(video, cost, section,
                    active, created_by, tas_t())
        )

    @classmethod
    async def delete(cls, idn, by=None):
        query = f"""
        UPDATE {await cls.get_table_name()}
        SET deleted_at=$1, deleted_by=$2, deleted=$3
        WHERE idn=$4
        """
        return await execute_query(
            query=query,
            params=(tas_t(), by, 1, idn)
        )

    @classmethod
    async def column_updater(cls, idn, col_name, data, by=None):
        if by is not None:
            query = f"""
            UPDATE {await cls.get_table_name()}
            SET {col_name}={data}, updated_at=$1, updated_by=$2
            WHERE idn=$3
            """
            return await execute_query(
                query=query,
                params=(tas_t(), by, idn)
            )

        query = f"""
        UPDATE {await cls.get_table_name()}
        SET {col_name}={data}, updated_at=$1
        WHERE idn=$2
        """
        return await execute_query(
            query=query,
            params=(tas_t(), idn)
        )

    async def save(self):
        query = f"""
        UPDATE {await self.get_table_name()}
        SET video=$1, cost=$2, section=$3, participated=$4, active=$5, created_at=$6, updated_at=$7
        WHERE idn=$8
        """
        await execute_query(
            query,
            params=(
                self.video, self.cost, self.section, self.participated, self.active, self.created_at, self.updated_at,
                self.idn
            )
        )

    @classmethod
    async def get_data(cls, idn):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE idn=$1
            """
        data = await execute_query(
            query=query,
            params=(int(idn),),
            fetch='one'
        )
        if data:
            return cls(**data)
        return None

    @classmethod
    async def get_data_by(cls, col, val, ex_d=""):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE {str(col)}=$1 {ex_d}
            """
        data = await execute_query(
            query=query,
            params=(val,),
            fetch='one'
        )
        if data:
            return cls(**data)
        return None

    @classmethod
    async def get_all(cls, ex=""):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE 1=1 {ex}
            """
        result = await execute_query(
            query=query,
            fetch='all'
        )
        return [cls(**item) for item in result] if result else []

    @classmethod
    async def get_active(cls, ex=""):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE active=1 {ex}
            ORDER BY created_at DESC
            """
        result = await execute_query(
            query=query,
            fetch='one'
        )
        if result:
            return cls(**result)
        return None