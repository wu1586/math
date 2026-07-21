import asyncio
from app.core.database import AsyncSessionLocal
from app.services.init_data import init_categories


async def main():
    """初始化数据库数据"""
    async with AsyncSessionLocal() as db:
        print("开始初始化数据...")
        await init_categories(db)
        print("数据初始化完成！")


if __name__ == "__main__":
    asyncio.run(main())
