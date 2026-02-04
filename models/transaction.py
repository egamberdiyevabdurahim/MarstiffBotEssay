from database_config.db_settings import execute_query


class TransactionModel:
    def __init__(
            self,
            idn = None,
            balance_idn = None,
            created_by=None,
            amount = None,
            proof = None,
            for_what = None,
            for_what_idn = None,
            is_benefit = None,
            created_at = None,
    ):
        self.idn = idn
        self.balance_idn = balance_idn
        self.created_by = created_by
        self.amount = amount
        self.proof = proof
        self.for_what = for_what
        self.for_what_idn = for_what_idn
        self.is_benefit = is_benefit
        self.created_at = created_at

    @classmethod
    async def get_table_name(cls):
        return 'transaction_model'

    @classmethod
    async def create_table(cls):
        query = f"""
        CREATE TABLE IF NOT EXISTS {await cls.get_table_name()} (
            idn SERIAL PRIMARY KEY,
            balance_idn INT,
            created_by INT,
            amount VARCHAR(50),
            proof TEXT,
            for_what VARCHAR(100),
            for_what_idn INT,
            is_benefit SMALLINT,
            created_at TIMESTAMPTZ DEFAULT timezone('Asia/Tashkent', NOW())
        )
        """
        await execute_query(query=query)
        return None

    @classmethod
    async def create(
            cls,
            balance_idn,
            amount,
            is_benefit,
            by=None,
            proof=None,
            for_what=None,
            for_what_idn=None,
    ):
        query = f"""
        INSERT INTO {await cls.get_table_name()}
        (balance_idn, created_by, amount, is_benefit, proof, for_what, for_what_idn)
        VALUES ($1, $2, $3, $4, $5, $6, $7)
        """
        return await execute_query(
            query=query,
            params=(balance_idn, by, str(amount), is_benefit, proof, for_what, for_what_idn),
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
    async def get_by_balance(cls, balance):
        query = f"""
            SELECT *
            FROM {await cls.get_table_name()}
            WHERE balance_idn=$1
            """
        result = await execute_query(
            query=query,
            params=(int(balance),),
            fetch='all'
        )
        return [cls(**item) for item in result] if result else []

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
