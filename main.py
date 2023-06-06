import os

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from utils import Auth0

app = FastAPI(default_response_class=JSONResponse, default_encoding="utf-8")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/get_token")
async def index(req: Request):
    data = await req.json()
    username = data.get('username', '')
    password = data.get('password', '')
    access_token = Auth0(username, password).auth(True)
    return JSONResponse({"token": access_token})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
