from pydantic import BaseModel


class SProduct(BaseModel):
    title: str
    description: str
    price: int
    amount: int

    class Config:
        orm_mode = True