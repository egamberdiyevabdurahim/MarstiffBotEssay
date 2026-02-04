from database_config.db_settings import execute_query
from utils.additions import tas_t


class UserModel:
    def __init__(
            self,
            idn = None,
            chat_id = None,
            id_name = None,
            phone_number = None,
            tg_username = None,
            tg_first_name = None,
            tg_last_name = None,
            name = None,
            age = None,
            used = None,
            role = None,
            lang = None,
            active = None,
            log_in = None,
            deleted = None,
            created_at = None,
            updated_at = None,
            deleted_at = None,
            deleted_by = None,
    ):
        if chat_id:
            chat_id = int(chat_id)
        self.idn = idn
        self.chat_id = chat_id
        self.id_name = id_name
        self.phone_number = phone_number
        self.tg_username = tg_username
        self.tg_first_name = tg_first_name
        self.tg_last_name = tg_last_name
        self.name = name
        self.age = age
        self.used = used
        self.role = role
        self.lang = lang
        self.active = active
        self.log_in = log_in
        self.deleted = deleted
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.deleted_by = deleted_by

    @classmethod
    async def get_table_name(cls):
        return 'user_model'

    @classmethod
    async def create_table(cls):
        query = f"""
        CREATE TABLE IF NOT EXISTS {await cls.get_table_name()} (
            idn SERIAL PRIMARY KEY,
            chat_id VARCHAR(255),
            id_name VARCHAR(255),
            phone_number VARCHAR(20),
            tg_username VARCHAR(64),
            tg_first_name VARCHAR(64),
            tg_last_name VARCHAR(64),
            name VARCHAR(64),
            age INT,
            used BIGINT DEFAULT 1,
            role SMALLINT DEFAULT 0,
            lang VARCHAR(4),
            active SMALLINT DEFAULT 1,
            log_in SMALLINT,
            deleted SMALLINT DEFAULT 0,
            created_at TIMESTAMPTZ DEFAULT timezone('Asia/Tashkent', NOW()),
            updated_at TIMESTAMPTZ,
            deleted_at TIMESTAMPTZ
        )
        """
        await execute_query(query=query)
        return None

    @classmethod
    async def create(
            cls,
            chat_id: int=None,
            id_name: str=None,
            phone_number: str=None,
            name: str=None,
            age: int=None,
            tg_username: str=None,
            tg_first_name: str=None,
            tg_last_name: str=None,
            role: int=1,
            lang: str=None,
            log_in: int=1,
    ):
        query = f"""
        INSERT INTO {await cls.get_table_name()}
        (chat_id, id_name, phone_number, name, age,
        tg_username, tg_first_name, tg_last_name, role, lang, log_in)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
        """
        return await execute_query(
            query=query,
            params=(str(chat_id), id_name, phone_number, name, age,
                    tg_username, tg_first_name, tg_last_name, role, lang, log_in)
        )

    @classmethod
    async def column_updater(cls, idn, col, data, by=None):
        if by:
            query = f"""
                UPDATE {await cls.get_table_name()}
                SET {col}={data}, updated_at=$1, updated_by=$2
                WHERE idn=$3
                """
            return await execute_query(
                query=query,
                params=(tas_t(), by, idn)
            )

        query = f"""
            UPDATE {await cls.get_table_name()}
            SET {col}={data}
            WHERE idn=$1
            """
        return await execute_query(
            query=query,
            params=(idn,)
        )

    @classmethod
    async def delete(cls, idn, by):
        if by:
            query = f"""
            UPDATE {await cls.get_table_name()}
            SET deleted=TRUE, deleted_at=$1, deleted_by=$2
            WHERE idn=$3
            """
            return await execute_query(
                query=query,
                params=(tas_t(), by, str(idn))
            )

        else:
            query = f"""
            UPDATE {await cls.get_table_name()}
            SET deleted=TRUE, deleted_at=$1
            WHERE idn=$2
            """
            return await execute_query(
                query=query,
                params=(tas_t(), str(idn))
            )

    async def save(self):
        query = f"""
        UPDATE {await self.get_table_name()}
        SET tg_username=$1, tg_first_name=$2, tg_last_name=$3, role=$4, updated_at=$5,
        lang=$6, log_in=$7, used=$8, name=$9, age=$10, phone_number=$11
        WHERE idn=$12
        """
        await execute_query(
            query,
            params=(
                self.tg_username, self.tg_first_name, self.tg_last_name,
                self.role, tas_t(), self.lang, self.log_in, self.used, self.idn,
                self.name, self.age, self.phone_number
            )
        )

    async def use(self):
        await self.column_updater(idn=self.idn, col='used', data=self.used + 1)

    @classmethod
    async def get_data(cls, chat_id, deleted=0):
        query = f"""
        SELECT *
        FROM {await cls.get_table_name()}
        WHERE chat_id=$1 AND deleted=$2
        """
        result = await execute_query(
            query=query,
            params=(str(chat_id), deleted),
            fetch='one'
        )
        if result:
            return cls(**result)
        return None

    @classmethod
    async def get_by_idn(cls, idn, deleted=0):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE idn=$1 AND deleted=$2
            """
        result = await execute_query(
            query=query,
            params=(int(idn), deleted),
            fetch='one'
        )
        if result:
            return cls(**result)
        return None

    @classmethod
    async def get_data_by(cls, col, val, deleted=0):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE {col}=$1 AND deleted=$2
            """
        result = await execute_query(
            query=query,
            params=(val, deleted),
            fetch='one'
        )
        if result:
            return cls(**result)
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
    async def get_all_id_names(cls, ex=""):
        query = f"""
        SELECT id_name
        FROM {await cls.get_table_name()}
        WHERE 1=1 {ex}
        """
        result = await execute_query(
            query=query,
            fetch='all'
        )
        return [cls(**item) for item in result] if result else []
