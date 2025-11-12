from fastapi import FastAPI
from .model import InputModel, TextModel
import math
from .ai import generate_input, generate_explanation
from .utils import calculate_flux
from fastapi.middleware.cors import CORSMiddleware
from .visual import visualize_inputs

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
async def insert_word_problem(text:TextModel):
    dict_text = text.model_dump()
    explanation = generate_input(dict_text["text"])
    given_inputs = dict(explanation['inputs'])
    visualize_flux = visualize_inputs(B=given_inputs["Tesla"], A=given_inputs["Area"], theta=given_inputs["Angle"])
    return {'result':explanation, 'visual':visualize_flux}

@app.post("/api/explain/")
async def explain(model:InputModel):
    dict_model = model.model_dump()
    explanation = generate_explanation(dict_model)
    visualize_flux = visualize_inputs(B=dict_model["Tesla"], A=dict_model["Area"], theta=dict_model["Angle"], angle_unit=dict_model["angleUnits"])
    return {'result': explanation,
            'visual': visualize_flux}

