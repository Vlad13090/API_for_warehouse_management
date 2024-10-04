from fastapi import FastAPI
from app.orders.router import router as order_router
from app.products.router import router as product_router


app = FastAPI()
app.include_router(order_router)
app.include_router(product_router)