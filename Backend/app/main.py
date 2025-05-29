from fastapi import FastAPI
from model import InputModel, TextModel
import math
from ai import generate_input, generate_explanation
from utils import calculate_flux
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def dummy():
    return {'message': 'Hi!'}

@app.post("/api/")
async def calculate(model: InputModel):
    dictmodel = model.model_dump()
    return calculate_flux(dictmodel)


@app.post("/api/ai/")
async def text_to_inputs(text:TextModel):
    dict_text = text.model_dump()
    num = generate_input(dict_text["text"])
    return num

@app.post("/api/explain/")
async def explain(model:dict):
    dict_model = model.model_dump()
    explanation = generate_explanation(dict_model)
    return explanation

