from flask import Flask, render_template, request, redirect
import pymongo
import easygui

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', Profile="Profile")

@app.route('/home/<Profilee>')
def homee(Profilee):
    return render_template('index.html', Profile="Log Out")

@app.route('/sigin/', methods=['POST'])
def sigin():
    if request.method == 'POST':
        user_name = request.form['txt']
        email = request.form['email']
        password = request.form['pswd']

        # Insert the data into MongoDB
        col.insert_one({
            'user_name': user_name,
            'email': email,
            'password': password
        })

        return redirect('/')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['txt']
        email = request.form['email']
        password = request.form['pswd']

        # Check if the user already exists based on username or email
        existing_user = col.find_one({
            '$or': [{'user_name': user_name}, {'email': email}]
        })

        if existing_user:
            easygui.msgbox(user_name + " " + email + " " + password)
            # User already exists, handle accordingly (e.g., display an error message)
            # return redirect(f'/homee/{"logout"}')
        else:
            # return redirect('/')
            # easygui.msgbox("login successful")
            pass  # You need to decide what to do when the user does not exist

@app.route('/product/<type>')
def product(type):
    return render_template(f'{type}.html', message="fffff")

@app.route('/about/')
def about():
    return render_template('about.html', message="fffff")

@app.route('/profile/')
def profile():
    return render_template('log.html', message="fffff")

if __name__ == '__main__':
    cl = pymongo.MongoClient("mongodb://localhost:27017/")
    col = cl.Techkart.user
    app.run(debug=True)
