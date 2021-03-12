"""
This is the routes module, it contains one FastAPI.APIRouter for each submodule:
    Category
    Marketplace
    Product
    Seller

Each router uses the implementations at the contrllers/ module.

The `router` of each submodule is then attached to the main app at ../main.py.

Read more about the routers at ../__init__.py.

TODO: methods in common between submodules should be generic.
"""
