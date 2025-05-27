def calculate(dictionary:dict):
    theta = dictionary["theta"] * (math.pi/180)
    phi = dictionary["magnetic_field"] * dictionary["area"] * math.cos(theta)
    return round(phi, 2)