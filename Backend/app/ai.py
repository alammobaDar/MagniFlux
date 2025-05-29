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
            system_instruction="""You are a physics teacher,and expertise in Magnetic Flux. And i want you to disseminate the given from a word problem into magnetic field, area, and the angle.
            be concise, just say provide in this format:
                "magnetic_field": 
                "area": 
                "theta": 
                don't provide symbols

                if you encounter scientific notation inputs, convert them into decimals
                and if the angle is in degrees, convert it to radians
            """ 
        ),
        contents=problem)

    text = response.text

    json_text = "{"  + text.strip().replace("\n", ",")+ "}"
    dict_json = json.loads(json_text)

    return dict(dict_json)
