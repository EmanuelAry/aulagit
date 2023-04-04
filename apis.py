from fastapi import FastAPI
import pandas as pd
import datetime as dt 
import json 
import sqlite3 as sql 
app = FastAPI()

#@app.get("/")
#async def hello():
#    return 'Hello word!'




#@app.get("/products")
#async def all_products():
#    conexao = sql.connect('globalstore_normalizada.db')
#    products = pd.read_sql(
#        con = conexao, 
#        sql = 'select * from products'
#        )
#    return products.to_json(orient = 'records')

@app.get("/products/category/{category_name}")
async def category_products(category_name: str):
    conexao = sql.connect('globalstore_normalizada.db')
    cat_products = pd.read_sql(
        con=conexao, 
        sql="select sub.subcategory, pro.product_id, pro.product_name "   
            "from products pro " + \
            "join subcategory sub on pro.sub_sequence = sub.sub_sequence " 
+
            "join category cat on sub.cat_sequence = cat.cat_sequence " +
            "where cat.category = '" + category_name + "'"
    )
    return cat_products.to_json(orient = 'records')

@app.get("/products/categorydf/{category_name}")
async def category_products(category_name: str):
    conexao = sql.connect('globalstore_normalizada.db')
    products = pd.read_sql(con=conexao, 
sql="select * from products")
    subcategory = pd.read_sql(con=conexao, 
sql="select * from subcategory")
    category = pd.read_sql(con=conexao, 
sql="select * from category")
    products = products.merge(subcategory, on='sub_sequence', how='left')
    products = products.merge(category, on='cat_sequence', how='left')
    return products[
products['category'] == category_name
].to_json(orient = 'records')

@app.get('/orderslist')
async def orders_list(year: int, orderpriority: str):
    conexao = sql.connect('globalstore_normalizada.db')
    orders = pd.read_sql(con=conexao, sql="select * from orders")
    orders['order_date'] = orders['order_date'].astype('datetime64[ns]')
    return orders[ 
        (orders['order_date'].dt.year == year) & 
        (orders['order_priority'] == orderpriority)
    ].to_json(orient = 'records')


@app.get('/client')
async def client_from():
    conexao = sql.connect('globalstore_normalizada.db')
    cliente = pd.read_sql(con=conexao, sql = "SELECT * FROM CLIENTS "+\
           "WHERE MERCADO is IN ('LATAM', 'US', 'Canada')")
    print(cliente.to_json(orient='cliente'))


@app.get('/pedidos')
async def pedidos_lista():
    conexao = sql.connect('globalstore_normalizada.db')
    pedidos = pd.read_sql(con = conexao, sql = "SELECT * FROM PEDIDOS"+\
                            "WHERE MERCADO = EU");

@app.get('pedidos')
async def pedidos_ano():
    conexao = sql.connect('globalstore_normalizada.db')
    pedidos = pd>read_sql(con = conexao, sql = "SELECT * FROM PEDIDOS"+\
                            "WHERE DATA ILIKE (2013) OR (2014)")


            