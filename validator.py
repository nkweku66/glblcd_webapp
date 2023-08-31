from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'update'

user_database = [{"email": 'lito@gmail.com', "password": 'what123'}]

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
  email = request.form.get('email')
  password = request.form.get('password')

  for user in user_database:
    if user['email'] == email and user['password'] == password:
      return "Login successful"
    
  return "Login Failed"

if __name__ == '__main__':
  app.run(debug=True)