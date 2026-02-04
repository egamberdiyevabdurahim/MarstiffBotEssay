from database_config.db_settings import execute_query
from utils.additions import tas_t


class EventUserModel:
    def __init__(
            self,
            idn = None,
            event_idn = None,
            u_idn = None,
            paid = None,
            proof = None,
            amount = None,
            in_process = None,
            deadline = None,
            message_id = None,
            message_id2 = None,
            done_by = None,
            active = None,
            created_at = None,
    ):
        self.idn = idn
        self.event_idn = event_idn
        self.u_idn = u_idn
        self.paid = paid
        self.proof = proof
        self.amount = amount
        self.in_process = in_process
        self.deadline = deadline
        self.message_id = message_id
        self.message_id2 = message_id2
        self.done_by = done_by
        self.active = active
        self.created_at = created_at

    @classmethod
    async def get_table_name(cls):
        return 'event_user_model'

    @classmethod
    async def create_table(cls):
        query = f"""
        CREATE TABLE IF NOT EXISTS {await cls.get_table_name()} (
            idn SERIAL PRIMARY KEY,
            event_idn INT,
            u_idn INT,
            paid SMALLINT,
            proof TEXT,
            amount FLOAT,
            in_process SMALLINT,
            deadline TIMESTAMPTZ,
            message_id VARCHAR(255),
            message_id2 VARCHAR(255),
            done_by INT,
            active SMALLINT,
            created_at TIMESTAMPTZ DEFAULT timezone('Asia/Tashkent', NOW())
        )
        """
        await execute_query(query=query)
        return None

    @classmethod
    async def create(
            cls,
            event_idn,
            u_idn,
            paid=0,
            proof=None,
            amount=0.00,
            in_process=0,
            deadline=None,
            message_id=None,
            message_id2=None,
            active=1,
    ):
        query = f"""
        INSERT INTO {await cls.get_table_name()}
        (event_idn, u_idn, paid, proof, amount, deadline, in_process,
        message_id, message_id2, active, created_at)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
        """
        return await execute_query(
            query=query,
            params=(event_idn, u_idn, paid, proof, amount, deadline, in_process,
                    str(message_id), str(message_id2), active, tas_t()),
        )

    async def save(self):
        query = f"""
        UPDATE {await self.get_table_name()}
        SET event_idn=$1, u_idn=$2, paid=$3, deadline=$4, in_process=$5, message_id=$6, amount=$7, proof=$8,
        done_by=$10, message_id2=$11, active=$12
        WHERE idn=$9
        """
        await execute_query(
            query,
            params=(
                self.event_idn, self.u_idn, self.paid, self.deadline, self.in_process, self.message_id,
                self.amount, self.proof, self.idn, self.done_by, self.message_id2, self.active,
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
    async def get_by_u(cls, u, ex=""):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE u_idn=$1 {ex}
            """
        result = await execute_query(
            query=query,
            params=(int(u),),
            fetch='all'
        )
        return [cls(**item) for item in result] if result else []

    @classmethod
    async def get_by_event(cls, event, ex=""):
        query = f"""
                SELECT *
                FROM {await cls.get_table_name()}
                WHERE event_idn=$1 {ex}
                """
        result = await execute_query(
            query=query,
            params=(int(event),),
            fetch='all'
        )
        return [cls(**item) for item in result] if result else []

    @classmethod
    async def get_data_by_event_u(cls, event, u, active=1):
        query = f"""
        SELECT *
        FROM {await cls.get_table_name()}
        WHERE event_idn=$1 AND u_idn=$2 AND active=$3
        """
        result = await execute_query(
            query=query,
            params=(int(event), int(u), active),
            fetch='one'
        )
        if result:
            return cls(**result)
        return None
