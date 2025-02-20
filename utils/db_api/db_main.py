from typing import Union

import asyncpg
from asyncpg import Connection, Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        """Create the connection pool for database."""
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(self, command, *args, fetch=False, fetchval=False, fetchrow=False, execute=False):
        """Execute database commands."""
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    return await connection.fetch(command, *args)
                elif fetchval:
                    return await connection.fetchval(command, *args)
                elif fetchrow:
                    return await connection.fetchrow(command, *args)
                elif execute:
                    return await connection.execute(command, *args)

    async def create_tables(self):
        """Create the required tables in the database."""
        queries = [
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                telegram_id BIGINT NOT NULL UNIQUE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS send_status (                
                send_post BOOLEAN DEFAULT FALSE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS pdfbase (
                id SERIAL PRIMARY KEY,                
                test_name VARCHAR(255) NOT NULL,
                file_id VARCHAR(255) NOT NULL
            );
            """
        ]
        # Execute each table creation query
        for query in queries:
            await self.execute(query, execute=True)

    # =========================== TABLE | USERS ===========================
    async def add_user(self, telegram_id):
        """ Add a user to the private table. """
        sql = "INSERT INTO users (telegram_id) VALUES ($1) ON CONFLICT (telegram_id) DO NOTHING"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users"
        return await self.execute(sql, fetchval=True)

    async def select_all_users(self):
        sql = "SELECT telegram_id FROM users "
        return await self.execute(sql, fetch=True)

    async def delete_user(self, telegram_id):
        await self.execute("DELETE FROM users WHERE telegram_id=$1", telegram_id, execute=True)

    async def drop_table_users(self):
        await self.execute("DROP TABLE users", execute=True)

    # =========================== TABLE | SEND_STATUS | BOT ADMINKASI UCHUN ===========================
    async def add_send_status(self):
        sql = ("INSERT INTO send_status (send_post) SELECT false "
               "WHERE NOT EXISTS (SELECT 1 FROM send_status WHERE send_post = false)")
        return await self.execute(sql, fetchrow=True)

    async def update_send_status(self, send_post):
        sql = "UPDATE send_status SET send_post = $1"
        return await self.execute(sql, send_post, execute=True)

    async def get_send_status(self):
        sql = "SELECT send_post FROM send_status"
        return await self.execute(sql, fetchval=True)

    async def drop_table_send_status(self):
        await self.execute("DROP TABLE send_status", execute=True)
