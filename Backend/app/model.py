from pydantic import BaseModel



class InputModel(BaseModel):
    Tesla: float
    Area: float
    Angle: float
    angleUnits: str
    flux: float 

class TextModel(BaseModel):
    text: str

    # @validator("magnetic_field", "area")
    # def must_be_positive(cls, v):
    #     if v < 0:
    #         raise ValueError("Value must be non-negative.")
    #     return v

    # @validator("theta")
    # def must_be_angle(cls, v):
    #     if not 0 <= v <= 360:
    #         raise ValueError("Angle must be between 0 and 360 degrees.")
    #     return v