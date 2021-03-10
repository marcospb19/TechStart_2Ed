"""
This is the server module.

It contains the `main.py` file that uses APIRouters from the routes submodule
to create the final server app.

So the final app is composed by:
    category.router       (with prefix '/category')
    + marketplace.router  (with prefix '/marketplace')
    + product.router      (with prefix '/product')
    + seller.router       (with prefix '/seller')

Located at:
    routers.category
    routers.marketplace
    routers.product
    routers.seller
"""
