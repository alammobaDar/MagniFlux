from fastapi import FastAPI
from model import InputModel
import math
app = FastAPI()

@app.get("/")
async def dummy():
    return {'message': 'Hi!'}

@app.post("/api/")
async def calculate(model: InputModel):
    dictmodel = model.model_dump()
    theta = dictmodel["theta"] * (math.pi/180)
    phi = dictmodel["magnetic_field"] * dictmodel["area"] * math.cos(theta)
    return round(phi, 2)