from app import app

'''
Routes
'''
#Index
@app.route("/")
def home():
    return "Hello World!"

#Login
@app.route("/login")
def login():
    return "Login"

#Logout
@app.route("/logout")
def logout():
    return "Logout"

