from fastapi import APIRouter
from controllers import category

router = APIRouter(
    prefix='/category',
    tags=['Category'],
)


@router.post('/')
def create():
    category.create()


@router.get('/')
def show():
    category.show()


@router.put('/')
def update():
    category.update()


@router.delete('/')
def delete():
    category.delete()
