from google import genai
from dotenv import load_dotenv
import os
from google.genai import types
import json
import re

load_dotenv()
def extract_json(response_text):
    match = re.search(r"```json\s*(\{.*?\})\s*```", response_text, re.DOTALL)
    # print(f"match: {match}")
    if match:
        json_str = match.group(1)
        # print(f"json_str: {json_str}")
        try:
            # print(json.loads(json_str))
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
    # print(text)
    json_text = extract_json(text)
    # print(json_text)
    return json_text

# problem = """
# A rectangular coil of wire with an area of 0.05 m² is placed in a uniform magnetic field of strength 0.8 Tesla. The plane of the coil is tilted at an angle of 40° to the direction of the magnetic field."""

# print(generate_input(problem))

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
    # print(text)
    json_text = extract_json(text)
    return json_text


# def input_dict_to_string(input: dict) -> str:
#     return (
#         f"A coil with area {input['Area']} m² is placed in a {input['Tesla']} Tesla magnetic field. "
#         f"The coil is tilted at an angle of {input['Angle']} degrees. "
#         f"The resulting magnetic flux is {input['flux']} Wb."
#     )
# input = {
#     "Tesla":0.8,
#     "Area":0.05,
#     "Angle":40,
#     "angleUnits":"Degrees",
#     "flux":0.0306
# }
# print(generate_explanation(input))

# string = input_dict_to_string(input)
# print(generate_explanation(string))

# response = """```
# {
# "flux": 0.0306,
# "explanation": "Magnetic flux is calculated using the formula Φ = B ⋅ A ⋅ cos(θ), where B is the magnetic field strength, A is the area, and θ is the angle between the magnetic field and the normal to the area.  First convert 40 degrees to radians which is approximately 0.698 radians. Then, plug in the values: 0.8 T * 0.05 m² * cos(0.698) = 0.0306 Wb."
# }
# ```"""

# print(extract_json(response))