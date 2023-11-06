from app.api import crud
from app.api.models import ItemDB, ItemSchema, ItemRequest
from fastapi import APIRouter, HTTPException, Path, Request
from typing import List
from datetime import datetime as dt

router = APIRouter()


@router.post("/", response_model=ItemDB, status_code=201)
async def create_item(payload: ItemRequest):
    item_id = await crud.post(payload)

    response_object = ItemDB(id=item_id, **payload.dict())
    return response_object


@router.get("/{id}/", response_model=ItemDB)
async def read_item(id: int = Path(..., gt=0), ):
    item = await crud.get(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/", response_model=List[ItemDB])
async def read_all_item(request: Request):
    return await crud.get_all()


@router.put("/{id}/", response_model=ItemDB)
async def update_item(payload: ItemRequest, id: int = Path(..., gt=0)):  # Ensures the input is greater than 0
    item = await crud.get(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item_id = await crud.put(id, payload)
    response_object = ItemDB(id=item_id, **payload.dict())
    return response_object


# DELETE route
@router.delete("/{id}/", response_model=ItemDB)
async def delete_item(id: int = Path(..., gt=0)):
    item = await crud.get(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    await crud.delete(id)
    return item


@router.get("/example_error")
async def example_error():
    await crud.example_error_db()
