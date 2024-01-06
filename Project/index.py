import math
from flask import render_template, request, redirect, jsonify, session
from Project import template
import database
import utils
import json
from Project import app


@app.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    num = database.count_book()
    page_size = app.config["PAGE_SIZE"]

    pro = database.get_book(kw, cate_id, page)
    return render_template('HomePage.html', pages=math.ceil(num/page_size), produces=pro)


@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/api/cart', methods=['post'])
def add_to_cart():
    '''
    {
        "cart": {
            "1": {
                "id": "1",
                "name": "ABC",
                "price": 123,
                "quantity": 2
            },
            "2": {
                "id": "2",
                "name": "ABC",
                "price": 123,
                "quantity": 1
            }
        }
    }
    '''

    cart = session.get('cart')
    if cart is None:
        cart = {}

    data = request.json
    id = str(data.get("id"))

    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            "id": id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": 1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.context_processor
def common_responses():
    return {
        'categories': database.get_category(),
        'cart_stats': utils.count_cart(session.get('cart'))
    }
# @app.route('/user-login', methods=['get', 'post'])
# def user_signin():
#     if request.method.__eq__('POST'):
#         username = request.form.get('username')
#         password = request.form.get('password')
#     return render_template('index.html')


if __name__ == '__main__':
    # from Project import admin
    app.run(debug=True)
