from fastapi import FastAPI
from model import InputModel
import math
from ai import generate_input
from utils import calculate
app = FastAPI()

@app.get("/")
async def dummy():
    return {'message': 'Hi!'}

@app.post("/api/")
async def calculate(model: InputModel):
    dictmodel = model.model_dump()
    return calculate(dictmodel)


@app.post("/api/ai/")
async def text_to_inputs(text:str):
    input = generate_input(text)
    return calculate(input)

