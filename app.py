from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class Events(BaseModel):
    icd: str
    date: str
    age: int

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Functions From Zero 2"}

@app.get("/predict")
async def pancnet_pred(events: Events):
    """make prediction form pancnet"""
    return events

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')