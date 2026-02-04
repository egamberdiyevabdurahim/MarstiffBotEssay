import random
from loader import User


async def unique_id_name_checker(name: str) -> bool:
    id_names = await User.get_all_id_names()
    return not any(item.id_name == name for item in id_names)


async def id_name_generator() -> str:
    while True:
        data = random.randint(1000, 9999)
        id_name = f"mf{data}"

        if await unique_id_name_checker(id_name):
            return id_name
