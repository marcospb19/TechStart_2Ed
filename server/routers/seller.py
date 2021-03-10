from fastapi import APIRouter

router = APIRouter(
    prefix='/seller',
    tags=['Seller'],
)


@router.get('/')
def hello():
    return 'hello seller'
