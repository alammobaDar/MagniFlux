from pydantic import BaseModel


class InputModel(BaseModel):
    magnetic_field: float
    area: float
    theta: float