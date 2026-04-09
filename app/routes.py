from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import StockForm, RegisterForm

@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('index.html', title='Home Page')

@app.route('/shop')
def shop():
    """Shop URL"""
    return render_template('shop.html', title='Shop Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You are requesting to register {form.username.data}')
        return redirect(url_for('register'))
    return render_template('register.html', title='Register Page', form=form)

@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    """Add Product URL"""
    form = StockForm()
    if form.validate_on_submit():
        flash(f'You are requesting to place an order of a {form.product_name.data}')
        return redirect(url_for('index'))
    return render_template('add_product.html', title='Product Page', form=form)