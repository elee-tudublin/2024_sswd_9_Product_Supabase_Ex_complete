# import the model class
from app.models.product import *
from starlette.config import Config
from supabase import create_client, Client

import httpx, json

import json


# Load environment variables from .env
config = Config(".env")

db_url: str = config("SUPABASE_URL")
db_key: str = config("SUPABASE_KEY")

supabase: Client = create_client(db_url, db_key)


# get all products
def dataGetProducts():
    response = (supabase.table("product")
                .select("*, category(name)")
                .order("title", desc=False)
                .execute()
    )
    return response.data


def dataGetProductByCat(id: int) :

    if (id > 0) :
        response = (supabase.table("product")
                    .select("*, category(name)")
                    .eq("category_id", id)
                    .order("title", desc=False)
                    .execute()
        )
        return response.data
    else :
        return dataGetProducts()    

# get product by id
def dataGetProduct(id):
    # select * from product where id = id 
    response = (
        supabase.table("product")
        .select("*, category(name)")
        .eq("id", id)
        .execute()
    )
    return response.data[0]

# update product
def dataUpdateProduct(product: Product) :
    # pass params individually
    #response = supabase.table("product").upsert({"id": product.id, "category_id": product.category_id, "title": product.title, "thumbnail": product.thumbnail, "stock": product.stock, "price": product.price}).execute()
    response = (
        supabase.table("product")
        .upsert(product.model_dump()) # convert product object to dict - required by Supabase
        .execute()
    )
    # After update get product by id (result will include the category)
    if (response.data) :
        return dataGetProduct(product.id)

    return None

# add product, accepts product object
def dataAddProduct(product: new_Product) :

    response = (
        supabase
        .table("product")
        .insert(product.model_dump()) # convert product object to dict - required by Supabase
        .execute()
    )
    # After inset get product by id (result will include the category)
    if (response.data) :
        return dataGetProduct(response.data[0]['id'])

    return None

# get all categories
def dataGetCategories():
    response = (supabase.table("category")
                .select("*")
                .order("name", desc=False)
                .execute()
    )

    return response.data


# delete product by id
def dataDeleteProduct(id):
    response = (
        supabase.table("product")
        .delete()
        .eq('id', id)
        .execute()
    )
    return response.data
