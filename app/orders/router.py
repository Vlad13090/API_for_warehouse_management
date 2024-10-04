from fastapi import APIRouter
from app.orders.dao import OrderDao


router = APIRouter(prefix="/orders", tags=["Заказы"])


@router.post("")  # Создание заказа (POST /orders)
async def create_order():
    pass


@router.get("")  # Получение списка заказов (GET /orders)
async def get_all_orders():
    return await OrderDao.get_all()


@router.get("/{order_id}")  # Получение информации о заказе по id (GET /orders/{id})
async def get_order_by_id(order_id: int):
    return await OrderDao.get(order_id)


@router.patch("/{order_id}/status")  # Обновление статуса заказа (PATCH /orders/{id}/status)
async def update_order_status(order_id: int):
    pass
