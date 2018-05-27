from flask import *
import mlab
from mongoengine import *
from models.customer import Customer
from models.user import User
from models.order import Order

mlab.connect()
app = Flask(__name__)
# @app.route('/delete/<customer_id>')
# def delete(customer_id):
#     customer_del = Customer.objects.with_id(customer_id)
#     if customer_del is not None:
#         customer_del.delete()
#     return redirect(url_for('admin'))

@app.route('/customer')
def customer():
    customer_list = Customer.objects()
    return render_template('customer.html', customer_list = customer_list)

@app.route('/admin')
def admin():
    all_customer = Customer.objects()
    return render_template('admin.html', all_customer=all_customer)

@app.route('/detail/<customer_id>')
def detail(customer_id):
    if "loggedin" in session:
        customer_detail = Customer.objects.with_id(customer_id)
        print(customer_id)
        return render_template('detail.html', customer_detail=customer_detail)
    else:
        return render_template('login.html')
@app.route('/add', methods=['POST', 'GET'])  
def add():
    if request.method == 'GET':  
        return render_template('new.html')
    elif request.method == 'POST':
        form = request.form  

        name = form['name']
        yob = form['yob']
        phone = form['phone']
        if form['gender'] == 'male':
            gender = 1
        else:
            gender = 0

        new_customer = Customer(name=name, yob=yob, phone=phone, gender=gender)
        new_customer.save()

        return redirect(url_for('customer'))

@app.route('/update/<user_id>', methods=['POST', 'GET'])
def update(user_id):
    if "loggedin" in session:
        customer_dict = Customer.objects.with_id(user_id)
        if request.method == 'GET':
            return render_template('update.html', item=customer_dict)
        elif request.method == 'POST':
            customer_list = Customer.objects(id=user_id)
            form = request.form

            name = form['name']
            yob = form['yob']
            phone = form['phone']
            if form['gender'] == 'male':
                gender = 1
            else:
                gender = 0

            customer_list.update(set__name=name,  
                                set__yob=yob,
                                set__phone=phone,
                                set__gender=gender)

        
            return 'cập nhật thành công'
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        users = User.objects(username=username, password=password)
        if len(users) == 0:
            return redirect(url_for('signin'))
        else:
            session['loggedin'] = True
            return redirect(url_for('customer'))

@app.route('/signin', methods = ["GET","POST"])
def signin():
    if request.method == "GET":
        return render_template("signin.html")
    elif request.method == "POST":
        form = request.form
        name = form['HoTen']
        email = form['Email']
        username = form['Username']
        password= form['Passwords']
        user = User(name= name,
                    email = email,
                    username = username,
                    password= password)
        user.save()
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if "loggedin" in session:
        del session['loggedin']
        return redirect(url_for('customer.html'))
    else:
        return redirect(url_for('customer.html'))

@app.route('/order_list')
def order_list():
    if "loggedin" in session:
        all_order = Order.objects()
        return render_template('order.html', all_order=all_order)
    else:
        return redirect(url_for("login"))


if __name__ == '__main__':
  app.run(debug=True)
 
