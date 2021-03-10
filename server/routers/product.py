from fastapi import APIRouter

router = APIRouter(
    prefix='/product',
    tags=['Product'],
)


@router.get('/')
def hello():
    return 'hello product'
