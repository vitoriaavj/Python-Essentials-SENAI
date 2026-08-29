from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.pessoa_router import router as pessoa_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(pessoa_router)

"""
@app.get("/")
def home():
    return{"Mensagem": "Olá"}
"""

#python -m uvicorn main:app --reload