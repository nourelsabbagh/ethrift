from flask import render_template, redirect, url_for, request, session, flash
from app import app
from app import models
from app import login_manager
from .forms import LoginForm
from .forms import Registration
from config import SQLALCHEMY_DATABASE_URI
from.models import User
from.models import Inventory
from.models import CartItem
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import os.path
import logging
from  flask_login import LoginManager, login_user, current_user, login_required, logout_user

@app.route('/')
def index():
        #should display all databases created despite their status
        return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
        form = LoginForm()
        if form.validate_on_submit():
                flash('Successfully recieved form data')
                user = User.query.filter_by(username = form.username.data).first()
                if user is not None and user.check_password(form.password.data):
                        login_user(user)
                        next = request.args.get("next")
                        return redirect(next or url_for('index'))
        flash('Invalid username or Password.')    
        return render_template('login.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
        form = Registration()
        if request.method == 'POST':
                if form.validate_on_submit():
                        flash('Successfully created your account')
                        user = User(username =form.username.data, email = form.email.data)
                        user.set_password(form.password1.data)
                        db.session.add(user)
                        db.session.commit()
                        return redirect(url_for('login'))
        return render_template('register.html', title='Registration', form=form)


@app.route('/basket')
def basket():

        #should display all databases created despite their status
        return render_template('basket.html')


@app.route('/tops')
def tops():
        top1 = Inventory(id='1', image='static/logo.png', product='Shrug with holes and flowy/ long sleeves.', size='S', color='apricot', price="7", description='Got compliments every time I wore this top')
        top2 = Inventory(id='2', image='static/logo.png', product='Cut shoulder top with threading designs.', size='M', color='white/black', price="10", description='Unique and edgy top')
        top3 = Inventory(id='3', image='static/logo.png', product='V-neck top with attached choker.', size='S', color='black', price="6", description='Suitable for clubbing')

        db.session.add(top1)
        db.session.add(top2)
        db.session.add(top3)
        

        products = Inventory.query.filter(Inventory.id<4).all()
        return render_template('items.html',products=products)
        

@app.route('/bottoms')
def bottoms():        
        bottom1 = Inventory(id='4', image='static/logo.png', product='Cargo pants', size='36 UK', color='army green', price="15", description='A staple in every girls closet')
        bottom2 = Inventory(id='5', image='static/logo.png', product='Bodycon skirt', size='M', color='black', price="5", description='Classy addition to any closet.')
        bottom3 = Inventory(id='6', image='static/logo.png', product='Parachute pants', size='S', color='white', price="15", description='The latest trend')

        db.session.add(bottom1)
        db.session.add(bottom2)
        db.session.add(bottom3)
        

        products = Inventory.query.filter(Inventory.id.between(4,7))

        return render_template('items.html',products=products)


@app.route('/outerwear')
def outerwear():       
        jacket1 = Inventory(id='7', image='static/logo.png', product='Long coat with silver buttons', size='XS', color='black', price="42", description='High quality coat')
        jacket3 = Inventory(id='8', image='static/logo.png', product='Flowy Cardigan', size='XS', color='pink', price="8", description='Gives a pop to neutral outfits')

        db.session.add(jacket1)
        db.session.add(jacket3)

        products = Inventory.query.filter(Inventory.id.between(7,9))
        
        return render_template('items.html',products=products)


@app.route('/shoes')
def shoes():    
        shoes1 = Inventory(id='9', image='static/shoes1.jpeg', product='Nike Air Force 1s', size='4 UK', color='white and yellow', price="60", description='Unique color')
        
        db.session.add(shoes1)

        products = Inventory.query.filter(Inventory.id == 9).all()
        return render_template('items.html',products=products)


@app.route('/other')
def other():        
        beanie = Inventory(id='10', image='static/beanie.jpeg', product='Beanie', size='one-size', color='white', price="4", description='A staple')
        
        db.session.add(beanie)
        
        db.session.commit()

        products = Inventory.query.filter(Inventory.id == 10)
        return render_template('items.html',products=products)


@app.route('/basket/<int:item_id>', methods=['POST'])
def add_to_cart(item_id):
    product = Inventory.query.filter(Inventory.id == item_id)
    cart_item = CartItem(product=product)
    db.session.add(cart_item)
    db.session.commit()
    

    return render_tempate('basket.html', product=products)


@app.route("/faq", methods=["POST", "GET"])
def faq():
   return render_template('faq.html', title='Frequently Asked Questions?')


@app.route("/forbidden",methods=['GET', 'POST'])
@login_required
def protected():
    return redirect(url_for('forbidden.html'))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))