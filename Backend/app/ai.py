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
            system_instruction="""You are a physics teacher,and expertise in Magnetic Flux.
                i will give you a word problem, and answer it, don't add symbols just give me the output of the magnetic flux. after that, explain, brief as possible

                the format of your answer will be like this:
                
                "flux": 0.0200,
                "explanation": "Your explanation"
                "inputs": { 'Tesla':<magnetic field value>,
                            'Area': <Area input>,
                            'Angle': <Angle input: radians>}

                Note that you should convert the angle to radians if it is a Degree
                if user includes angle in degree form, always convert it into radian form
                if you are given a word problem not related to Magnetic Flux, just answer this, 
                
                "flux": "--",
                "explanation": "Not Related"

                if you are given a word Problem that has a missing needed inputs, just sa "Insufficient Input" in explanation and "--" in flux
                
                "flux": "--",
                "explanation": "Insufficient Inputs"

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

