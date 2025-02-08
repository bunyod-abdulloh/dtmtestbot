from utils.db_api.db_main import Database


class PdfBase:
    def __init__(self, db: Database):
        self.db = db

    async def add_file(self, test_name, file_id):
        sql = "INSERT INTO pdfbase (test_name, file_id) VALUES ($1, $2)"
        return await self.db.execute(sql, test_name, file_id, fetchrow=True)

    async def select_files_by_name(self, test_name):
        sql = "SELECT file_id FROM pdfbase WHERE test_name = $1"
        return await self.db.execute(sql, test_name, fetch=True)

    async def delete_files(self, test_name):
        await self.db.execute("DELETE FROM pdfbase WHERE test_name = $1", test_name, execute=True)

    async def drop_table_pdfbase(self):
        await self.db.execute("DROP TABLE pdfbase", execute=True)
