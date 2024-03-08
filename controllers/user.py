from flask import Blueprint, render_template, request, redirect
from connectors.mysql_connecotr import engine
from models.user import User
from sqlalchemy import select, or_
from sqlalchemy.orm import sessionmaker
from flask_login import login_user, logout_user
from flask import jsonify
from flask_login import current_user, login_required


user_routes = Blueprint('user_routes',__name__)

@user_routes.route("/register", methods=['GET'])
def user_register():
    return render_template("users/register.html")

@user_routes.route("/register", methods=['POST'])
def do_registration():

    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    NewUser = User(username=username, email=email)
    NewUser.set_password(password)

    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()

    session.begin()
    try:
        session.add(NewUser)
        session.commit()
    except Exception as e:
        session.rollback()
        return { "message": "Gagal Register" }
    
    return { "message": "Sukses Register" }

@user_routes.route("/login", methods=['GET'])
def user_login():
    return render_template("users/login.html")

@user_routes.route("/login", methods=['POST'])
def do_user_login():
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()

    try:
        user = session.query(User).filter(User.email==request.form['email']).first()

        if user == None:
            return {"message" : "Email tidak terdaftar"}
        
        # Check Password
        if not user.check_password(request.form['password']):
            return {"message" : "Password Salah"}

        login_user(user, remember=False)
        return redirect('/product')

    except Exception as e:
        return { "message" : "Login Failed"}
    
@user_routes.route("/logout", methods=['GET'])
def do_user_logout():
    logout_user()
    return redirect('/login')

# @user_routes.route("/get_user_role", methods=["GET"])
# @login_required
# def get_user_role():
#     if current_user.is_authenticated:
#         return jsonify({"role": current_user.role != 'Admin'}), 200
#     else:
#         return jsonify({"message": "User not logged in"})

