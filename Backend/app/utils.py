import math
async def calculate_flux(dictionary:dict):
    phi = dictionary["magnetic_field"] * dictionary["area"] * math.cos(dictionary["theta"])
    return round(phi, 4)