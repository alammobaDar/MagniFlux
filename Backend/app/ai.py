from google import genai
from dotenv import load_dotenv
import os
from google.genai import types
import json

load_dotenv()

def generate_input(problem:str):

    client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="""You are a physics teacher,and expertise in Magnetic Flux.
                i will give you a word problem, and answer it, don't add symbols just give me the output of the magnetic flux. after that, explain, brief as possible

                Please respond with a single JSON string exactly like this example:

                {
                "flux": "0.0200",
                "explanation": "<Your explanation>"
                }

                Do not add any extra text or line breaks.
                Note that you should convert the angle to radians if it is a Degree

                if you are given a word problem not related to Magnetic Flux, just say "Not Related"
                if you are given a word Problem that has a missing needed inputs, just sa "Insufficient Input"
            """ 
        ),
        contents=problem)

    text = response.text

    return text

# problem = """
# A rectangular coil of wire with an area of 0.05 m² is placed in a uniform magnetic field of strength 0.8 Tesla. The plane of the coil is tilted at an angle of 40° to the direction of the magnetic field."""

# print(generate_input(problem))

def generate_explanation(input:dict):
    client = genai.Client(api_key=os.getenv("GEMINI_KEY"))


    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="""You are a physics teacher,and expertise in Magnetic Flux.
                and i will give you a dictionary or json and explain how will you answer it. 
                provide it briefly.

                the format of the answer will be in dict format:
                    {"explanation": <your explanation>}
            """ 
        ),
        contents=input)

    text = response.text

    return text
# TO DO: Nag ka error to, dapat ang pinapasa ay nakaganto:
# def input_dict_to_string(input: dict) -> str:
    # return (
    #     f"A coil with area {input['Area']} m² is placed in a {input['Tesla']} Tesla magnetic field. "
    #     f"The coil is tilted at an angle of {input['Angle']} degrees. "
    #     f"The resulting magnetic flux is {input['flux']} Wb."
    # )
input = {
    "Tesla":0.8,
    "Area":0.05,
    "Angle":40,
    "angleUnits":"Degrees",
    "flux":0.306
}

print(generate_explanation(input))

