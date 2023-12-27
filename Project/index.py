from flask import render_template, request, redirect
from Project import template
import database
from Project import app


@app.route('/')
def index():
    kw = request.args.get("kw")
    cate_id = request.args.get('cate_id')

    pro = database.get_book(kw, cate_id)
    cas = database.get_category()
    return render_template('HomePage.html', categories=cas, produces=pro)


@app.route('/user-login', methods=['get', 'post'])
def user_signin():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
    return render_template('index.html')




if __name__=='__main__':
    # from Project import admin
    app.run(debug=True)