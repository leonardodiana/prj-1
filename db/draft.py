from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from uuid import UUID
from databases import Database


database = Database("sqlite:///db.sqlite3")

app = FastAPI()


class Book(BaseModel):
    id:int = UUID
    regione:str = Field(min_lenght=1)
    anno:int = Field(gt=0)
    arrivi:int = Field(gt=0)
    presenze:int = Field(gt=0)

AGRITURISMOS = []

@app.on_event("startup")
async def database_connect():
    await database.connect()

@app.get("/agriturismo")
def read_api():
    return AGRITURISMOS
