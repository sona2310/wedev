from flask import Flask,render_template,request,redirect
import csv
app=Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def hello(page_name):
    return render_template(page_name)

def data_in_txt(data):
    with open('test2.txt','a') as file1:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=file1.write(f'\n{email},{subject},{message}')

def data_in_csv(data):
    with open('new.csv','a') as file2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        writers=csv.writer(file2,delimiter=',',lineterminator='\n',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writers.writerow([email,subject,message])


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        data=request.form.to_dict()
        print(data)
        data_in_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong '