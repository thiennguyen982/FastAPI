import asyncio
import pyodbc

cnxn_str = "..."

async def read_data(*args, **kwargs):
    table = args[0]
    async with pyodbc.connect(cnxn_str) as conn:
        rows = conn.execute("SELECT * FROM iotsolution.")