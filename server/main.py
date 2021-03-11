from fastapi import FastAPI
import db
import uvicorn

# Import routers that compose the app endpoints
from routers import category, marketplace, product, seller

# Initializing the database
db.init_db()

# Main app
app = FastAPI()

# Attach each router to the main app
app.include_router(category.router)
app.include_router(marketplace.router)
app.include_router(product.router)
app.include_router(seller.router)


def main():
    """ Run the server app at `main.py` """
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)


if __name__ == '__main__':
    main()
