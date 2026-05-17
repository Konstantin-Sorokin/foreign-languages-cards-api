import uvicorn
from fastapi import FastAPI

from app.routers import router
from app.utils import settings

app = FastAPI()
app.include_router(router)


@app.get("/health", include_in_schema=False)
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
