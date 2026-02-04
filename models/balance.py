from database_config.db_settings import execute_query


class BalanceModel:
    def __init__(
            self,
            idn = None,
            u_idn = None,
            amount = None,
            is_benefit = None,
            created_at = None,
    ):
        self.idn = idn
        self.u_idn = u_idn
        self.amount = amount
        self.is_benefit = is_benefit
        self.created_at = created_at

    @classmethod
    async def get_table_name(cls):
        return 'balance_model'

    @classmethod
    async def create_table(cls):
        query = f"""
        CREATE TABLE IF NOT EXISTS {await cls.get_table_name()} (
            idn SERIAL PRIMARY KEY,
            u_idn INT,
            amount VARCHAR(50),
            is_benefit SMALLINT,
            created_at TIMESTAMPTZ DEFAULT timezone('Asia/Tashkent', NOW())
        )
        """
        await execute_query(query=query)
        return None

    @classmethod
    async def create(
            cls,
            u_idn,
            amount,
            is_benefit,
    ):
        query = f"""
        INSERT INTO {await cls.get_table_name()}
        (u_idn, amount, is_benefit)
        VALUES ($1, $2, $3)
        """
        return await execute_query(
            query=query,
            params=(u_idn, str(amount), is_benefit)
        )

    async def save(self):
        query = f"""
        UPDATE {await self.get_table_name()}
        SET amount=$1, is_benefit=$2
        WHERE idn=$3
        """
        await execute_query(
            query,
            params=(
                self.amount, self.is_benefit, self.idn
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
    async def get_by_u(cls, u):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE u_idn=$1
            """
        result = await execute_query(
            query=query,
            params=(int(u),),
            fetch='one'
        )
        if result:
            return cls(**result)
        return None

    @classmethod
    async def get_by_is_benefit(cls, is_benefit):
        query = f"""
                SELECT *
                FROM {await cls.get_table_name()}
                WHERE is_benefit=$1
                """
        result = await execute_query(
            query=query,
            params=(int(is_benefit),),
            fetch='all'
        )
        return [cls(**item) for item in result] if result else []
