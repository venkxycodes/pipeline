from fastapi import FastAPI
from producer.router import router
import uvicorn

def create_app() -> FastAPI:
    producer_app = FastAPI(title="Event Producer Service")
    producer_app.include_router(router.router)
    return producer_app

if __name__ == "__main__":
    app = create_app()
    # uvicorn.run("producer.main:app", host="0.0.0.0", port=8000, reload=True)
