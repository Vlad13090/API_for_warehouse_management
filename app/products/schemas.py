from pydantic import BaseModel


class SProduct(BaseModel):
    title: str
    description: str
    price: int
    amount: int

    class Config:
        from_attributes = True


class SProductOutput(BaseModel):
    id: int
    title: str
    description: str
    price: int
    amount: int

    class Config:
        from_attributes = True
