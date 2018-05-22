from flask import *
import mlab
from mongoengine import *
from models.customer import Customer

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

    customer_detail = Customer.objects.with_id(customer_id)
    print(customer_id)
    return render_template('detail.html', customer_detail=customer_detail)

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

if __name__ == '__main__':
  app.run(debug=True)
 
