from app import app
from config import db
from models import Customer, Credit, Item, Order, OrderDetail, OrderStatus, Payement
from flask import request, jsonify

with app.app_context():
    db.create_all()


@app.route('/custum/add', methods=['POST'])
def add_custum():
    try:
       json = request.json
       name = json["name"]
       deliveryAddress = json["deliveryAddress"]
       contact = json["contact"]
       active = json["active"]

       if name and deliveryAddress and contact and active and request.method == 'POST':
        custum = Customer(name=name, deliveryAddress=deliveryAddress, contact=contact, active=active)
        db.session.add(custum)
        db.session.commit()
        resultat = {"message":" Customer a été bien ajouté"}
        return jsonify(resultat)

    except Exception as e:
        print(e)
        resultat = {"message":"nous avons rencontrer un problème"}
        return resultat
        


@app.route('/cred/add', methods=['POST'])
def add_cred():
    try:
       json = request.json
       number = json["number"]
       type = json["type"]
       expireDAte = json["expireDAte"]

       if number and type and type and request.method == 'POST':
        cred = Credit(number=number, type=type, expireDAte=expireDAte,)
        db.session.add(cred)
        db.session.commit()
        resultat = {"message":" credrit a été bien ajouté"}
        return jsonify(resultat)

    except Exception as e:
        print(e)
        resultat = {"message":"nous avons rencontrer un problème"}
        return resultat



@app.route('/ite/add', methods=['POST'])
def add_ite():
    try:
       json = request.json
       name = json["name"]
       description = json["description"]

       if name and description and request.method == 'POST':
        ite = Item(name=name, description=description,)
        db.session.add(ite)
        db.session.commit()
        resultat = {"message":" Item a été bien ajouté"}
        return jsonify(resultat)

    except Exception as e:
        print(e)
        resultat = {"message":"nous avons rencontrer un problème"}
        return resultat



@app.route('/ode/add', methods=['POST'])
def add_ode():
    try:
       json = request.json
       createDate = json["createDate"]

       if createDate and request.method == 'POST':
        ode = Order(createDate=createDate,)
        db.session.add(ode)
        db.session.commit()
        resultat = {"message":" Order a été bien ajouté"}
        return jsonify(resultat)

    except Exception as e:
        print(e)
        resultat = {"message":"nous avons rencontrer un problème"}
        return resultat



@app.route('/oderdet/add', methods=['POST'])
def add_oderdet():
    try:
       json = request.json
       qty = json["qty"]
       taxStatus = json["taxStatus"]

       if qty and taxStatus and request.method == 'POST':
        oderdet = OrderDetail(qty=qty, taxStatus=taxStatus)
        db.session.add(oderdet)
        db.session.commit()
        resultat = {"message":" OrderDetail a été bien ajouté"}
        return jsonify(resultat)

    except Exception as e:
        print(e)
        resultat = {"message":"nous avons rencontrer un problème"}
        return resultat





