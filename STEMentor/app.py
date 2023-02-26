from flask import Flask, render_template, redirect, request,url_for
import csv
import os

app = Flask(__name__, template_folder='templates')


def filewrite(id):
    fields = ['username', 'email', 'password', 'gender']
    if os.path.isfile("D:\\life\\hackathons\\STEMentor\\data\\userdata.csv"):
        with open("D:\\life\\hackathons\\STEMentor\\data\\userdata.csv", "a") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writerow(id)
    else:
        with open("D:\\life\\hackathons\\STEMentor\\data\\userdata.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerow(id)


@app.route('/home/<name>')
def home(name):
    list = []
    list1=[]
    f = open("D:\\life\\hackathons\\STEMentor\\data\\post.csv", 'r')
    f1=open("D:\\life\\hackathons\\STEMentor\\data\\jobs.csv", 'r')
    reader = csv.DictReader(f)
    reader1=csv.DictReader(f1)
    for i in reader:
        list.append(i)
    for i in reader1:
        list1.append(i)
    print(list,list1)
    return render_template('home.html', data=list,jdata=list1,name=name,us=name)

@app.route('/')
@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/message')
def message():
    return render_template('message.html')

@app.route('/jobs')
def jobs():
    list1=[]
    f1=open("D:\\life\\hackathons\\STEMentor\\data\\jobs.csv", 'r')
    reader1=csv.DictReader(f1)
    for i in reader1:
        list1.append(i)
    print(list1)
    return render_template('jobs.html',data=list1)

@app.route('/adduser', methods=['POST'])
def add_user():
    username = request.form.get('Name')
    email = request.form.get('Email')
    password = request.form.get('Password')
    gender = request.form.get('gender')
    filewrite({'username': username, 'email': email,
              'password': password, 'gender': gender})
    return redirect('/signin')


@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('Email')
    password = request.form.get('Password')
    f = open("D:\\life\\hackathons\\STEMentor\\data\\userdata.csv", 'r')
    reader = csv.DictReader(f)
    for user in reader:
        print(user)
        if user['email'] == email and user['password'] == password:
            print(user['username'])
            list = []
            list1=[]
            f = open("D:\\life\\hackathons\\STEMentor\\data\\post.csv", 'r')
            f1=open("D:\\life\\hackathons\\STEMentor\\data\\jobs.csv", 'r')
            reader = csv.DictReader(f)
            reader1=csv.DictReader(f1)
            for i in reader:
                list.append(i)
            for i in reader1:
                list1.append(i)
            print(list,list1)
            return redirect(url_for('home',name=user['username']))
        elif user['email'] == email and user['password'] != password:
            return redirect('/signin')
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)
