from typing import List

from fastapi import APIRouter
from app.products.schemas import SProduct, SProductOutput
from app.products.dao import ProductsDao

router = APIRouter(prefix="/products", tags=["Продукты"])


@router.post("")  # Создание товара (POST /products)
async def create_product(product: SProduct):
    await ProductsDao.add(title=product.title,
                          description=product.description,
                          price=product.price,
                          amount=product.amount)


@router.get("", response_model=List[SProductOutput])  # Получение списка товаров (GET /products)
async def get_all_products():
    return await ProductsDao.get_all()


@router.get("/{product_id}", response_model=SProductOutput)  # Получение информации о товаре по id (GET /products/{id})
async def get_product_by_id(product_id: int):
    return await ProductsDao.get(product_id)


@router.put("/{product_id}")  # Обновление информации о товаре (PUT /products/{id})
async def update_product_by_id(product_id: int, values: SProduct):
    await ProductsDao.update(product_id, title=values.title,
                             description=values.description,
                             price=values.price,
                             amount=values.amount
                             )


@router.delete("/{product_id}")  # Удаление товара (DELETE /products/{id})
async def delete_product_by_id(product_id: int):
    await ProductsDao.delete(product_id)
