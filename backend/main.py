from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List

class Events(BaseModel):
    icd: List[str]
    date: List[str]
    age: List[int]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from PancNet"}

@app.post("/predict")
async def pancnet_pred(events: Events):
    """make prediction form pancnet"""
    return events

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')