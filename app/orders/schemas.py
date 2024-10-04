from pydantic import BaseModel
from datetime import date
from enum import Enum

class Status(str, Enum):
    in_progress = 'в процессе'
    sent = 'отправлен'
    delivered = 'доставлен'


class SOrders(BaseModel):
    id: int
    date: date
    status: str

    class Config:
        orm_mode = True


class SOrderItem(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True