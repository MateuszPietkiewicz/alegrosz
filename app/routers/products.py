from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.product import ProductRepository
from app.db.session import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)




@router.get("/")
def list_products(
        search: str | None = None,
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    if search:
        return ProductRepository.search(db, search, skip=skip, limit=limit)
    else:
        return ProductRepository.get_all(db, skip=skip, limit=limit)