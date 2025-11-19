class MongoService:
    async def create_job(self, job_id: str, meeting_code: str, passcode: str, num_bots: int):
        pass
    
    async def get_job(self, job_id: str):
        return {"job_id": job_id, "status": "mock"}

mongo_service = MongoService()