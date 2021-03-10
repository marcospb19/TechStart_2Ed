from fastapi import FastAPI
import uvicorn

# Import routers
from routers import category, marketplace, product, seller

app = FastAPI()

# Attach each router to the main app
app.include_router(category.router)
app.include_router(marketplace.router)
app.include_router(product.router)
app.include_router(seller.router)


if __name__ == '__main__':
    # Run server with the app declared above in this file
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
