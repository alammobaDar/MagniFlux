from google import genai
from dotenv import load_dotenv
import os
from google.genai import types
import json
import re

load_dotenv()
def extract_json(response_text):
    match = re.search(r"```json\s*(\{.*?\})\s*```", response_text, re.DOTALL)
    if match:
        json_str = match.group(1)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON"}
    return {"error": "No JSON found"}

def generate_input(problem:str):

    client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="""
                You are a physics teacher with expertise in Magnetic Flux.

                You will be given a word problem. Solve it only if it relates to magnetic flux using this formula: Φ = B ⋅ A ⋅ cos(θ)

                Always follow this output format exactly:

                "flux": <numeric or "--">,
                "explanation": "<brief explanation here>",
                "inputs": {
                    "Tesla": <magnetic field in Tesla>,
                    "Area": <area in square meters>,
                    "Angle": <angle in radians>
                }

                Rules:
                - Only use the formula: Φ = B ⋅ A ⋅ cos(θ)
                - If angle is in degrees, convert it to radians using θ (rad) = degrees × π / 180
                - If the problem is not related to magnetic flux, return:
                  "flux": "--",
                  "explanation": "Not Related",
                  "inputs": { "Tesla": "--", "Area": "--", "Angle": "--" }
                - If any required value (B, A, or θ) is missing or cannot be derived, return:
                  "flux": "--",
                  "explanation": "Insufficient Inputs",
                  "inputs": { "Tesla": "--", "Area": "--", "Angle": "--" }

                Clarify assumptions briefly, but keep the explanation short and accurate.
            """ 
        ),
        contents=problem)

    text = response.text.strip()
    json_text = extract_json(text)
    return json_text

def generate_explanation(input:dict):
    client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

    string = f"""
        the area is {input['Area']} m², the tesla or magnetic field is {input['Tesla']} Tesla.
        The angle is {input['Angle']} {input['angleUnits']}.
        The resulting magnetic flux is {input['flux']} Wb.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="""You are a physics teacher,and expertise in Magnetic Flux.
                and i will give you a string and explain how will you answer it. 
                provide it briefly.

                the format of the answer will be in dict format:
                    "explanation": "your explanation"

                if you encounter an angle in Degree form, turn it into radians form, include that also on your explanation
                don't add anything other than the format, don't include backticks and python or json on your outputs
                don't give me an introduction just explain

            """ 
        ),
        contents=string)

    text = response.text
    json_text = extract_json(text)
    return json_text

