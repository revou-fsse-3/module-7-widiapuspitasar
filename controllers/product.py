from flask import Blueprint, render_template, request, jsonify
from connectors.mysql_connecotr import engine, Session
from models.product import Product
from sqlalchemy import select, or_
from flask_login import current_user, login_required
from sqlalchemy.orm import sessionmaker

from decorators.role_checker import role_required
from validations.product_schema import product_schema
from cerberus import Validator



product_routes = Blueprint('product_routes',__name__)

@product_routes.route("/product", methods=['GET'])
@login_required
def product_home():
    response_data = dict()
    
    
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    
    try:
        product_query = select(Product)

        if request.args.get('query') != None:
            search_query = request.args.get('query')
            product_query = product_query.where(Product.name.like(f'%{search_query}%'))

        products = session.execute(product_query).scalars()
        response_data['products'] = list(products)

        for product in response_data['products']:
            print(product)
    except Exception as e:
        print(e)
        return "Error Processing Data"

    response_data['username'] = current_user.username
    response_data['isAdmin'] = current_user.role 

    return render_template("products/product_home.html", response_data=response_data)



@product_routes.route("/product", methods=['POST'])
@login_required
def product_insert():

    # v = Validator(product_schema)
    # json_data = request.get_json()

    # if not v.validate(json_data):
    #     return jsonify({"error": v.errors}), 400

    try:
        new_product = Product(
            name=request.form['productName'],
            price=request.form['productPrice'],
            description=request.form['productDescription']
        )

        
        with engine.connect() as connection:
            Session = sessionmaker(bind=connection)
            session = Session()

            
            with session.begin():
                session.add(new_product)

        return { "message": "Success insert data"}

    except Exception as e:
        print(e)
        return { "message": "Fail to insert data"}

@product_routes.route("/product/<id>", methods=['DELETE'])
@role_required('Admin')
def product_delete(id):
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    session.begin()

    try:
        product_to_delete = session.query(Product).filter(Product.id==id).first()
        session.delete(product_to_delete)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return { "message": "Fail to delete data"}
    
    return { "message": "Success delete data"}

@product_routes.route("/product/<id>", methods=['PUT'])
@role_required('Admin')
def product_update(id):
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    session.begin()

    try:
        print(request.form)
        product = session.query(Product).filter(Product.id==id).first()

        product.name = request.form.get('productName', product.name)
        product.price = request.form.get('productPrice', product.price)
        product.description = request.form.get('productDescription', product.description)
        session.commit()
        return { "message": "Success updating data"}
    except Exception as e:
        session.rollback()

    return { "message": "Success updating data"}
    

   



