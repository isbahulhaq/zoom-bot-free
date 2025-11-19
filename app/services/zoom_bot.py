import asyncio

async def run_zoom_bot(job_id: str, meeting_code: str, passcode: str, duration: int, bot_index: int):
    bot_name = f"Bot-{bot_index+1}"
    await asyncio.sleep(5)  # Simulate bot running
    return {"status": "completed", "bot_name": bot_name}