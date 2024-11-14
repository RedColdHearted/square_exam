import pydantic

class SquareBase(pydantic.BaseModel):
    """Base `Square` schema."""
    x: int
    y: int
    side_length: float