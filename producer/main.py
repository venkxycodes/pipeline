from fastapi import FastAPI
from producer.router import router
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router.router)

# uvicorn.run("producer.main:app", host="0.0.0.0", port=8000, reload=True)
