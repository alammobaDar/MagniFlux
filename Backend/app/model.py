from pydantic import BaseModel



class InputModel(BaseModel):
    magnetic_field: float
    area: float
    theta: float
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