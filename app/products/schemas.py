from pydantic import BaseModel, condecimal, conint


class SProduct(BaseModel):
    title: str
    description: str
    price: condecimal(max_digits=10, decimal_places=2, ge=0)
    amount: conint(ge=0)

    class Config:
        from_attributes = True


class SProductOutput(BaseModel):
    id: int
    title: str
    description: str
    price: condecimal(max_digits=10, decimal_places=2, ge=0)
    amount: conint(ge=0)

    class Config:
        from_attributes = True
