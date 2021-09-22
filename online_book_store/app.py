from flask import Flask, session, redirect, render_template, url_for #type:ignore
from models import authentication, account, inventory, manager, social, stats
from functools import wraps
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config.SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
app.config.DATABASE = 'store.db'
app.config.UPLOAD_FOLDER = 'static/uploads'
bootstrap = Bootstrap(app)

def login_required(status="manager"):
    def login_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'username' in session and status in session:
                return func(*args, **kwargs)
            else:
                if status == "manager":
                    return redirect(url_for('managerLogin'))
                if status == "user":
                    return redirect(url_for('login'))
        return wrapper
    return login_decorator

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/topCharts", methods=["GET","POST"])
def topCharts():
    return stats.topCharts()

@app.route("/awards", methods=["GET","POST"])
def awards():
    return stats.awards()

@app.route("/search", methods=["GET","POST"])
def search():
    return inventory.search()

@app.route("/product/<isbn>", methods=["GET","POST"]) 
def viewProduct(isbn):
    return inventory.viewProduct(isbn)


@app.route("/addToCart/<isbn>", methods=["GET","POST"])
@login_required("user")
def addToCart(isbn):
    return account.addToCart(isbn)

@app.route("/account/profile")
@login_required("user")
def profileHome():
    return render_template("profileHome.html", username = session['username'], no_of_items = 0)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    return account.register()

@app.route("/registerationForm")
def registrationForm():
    return render_template("register.html")

@app.route("/account/profile/update", methods=["GET", "POST"])
@login_required("user")
def updateProfile():
    return account.updateProfile()

@app.route("/account/profile/changePassword", methods=["GET", "POST"])
@login_required("user")
def changePassword():
    return account.changePassword()

@app.route("/account/cart", methods=["GET", "POST"])
@login_required("user")
def viewCart():
    return account.viewCart()

@app.route("/login", methods = ['POST', 'GET'])
def login():
    return authentication.login()

@app.route("/logout", methods = ['GET'])
@login_required("user")
def logout():
    session.pop('user', None)
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route("/manager/login", methods = ['POST', 'GET'])
def managerLogin():
    return authentication.managerLogin()

@app.route("/manager/logout", methods = ['POST', 'GET'])
@login_required("manager")
def managerLogout():
    return authentication.managerLogout()

@app.route("/manager", methods = ['GET'])
@login_required("manager")
def managerHome():
    return render_template("managerHome.html")


@app.route("/manager/addBook", methods = ['POST', 'GET'])
@login_required("manager")
def addBook():
    return inventory.addBook()

@app.route("/manager/addManager", methods = ['POST', 'GET'])
@login_required("manager")
def addManager():
    return manager.addManager()

@app.route("/manager/goodsMovement/<movement_type>", methods = ['POST', 'GET'])
@login_required("manager")
def goodsMovement(movement_type):
    return inventory.goodsMovement(movement_type = movement_type)

@app.route("/product/<isbn>/review/edit/<review_id>", methods = ['POST', 'GET'])
@login_required("user")
def editReview(isbn, review_id):
    return social.editReview(isbn, review_id)

@app.route("/product/<isbn>/review/add", methods = ['POST', 'GET'])
@login_required("user")
def addReview(isbn):
    return social.addReview(isbn)

@app.route("/review/vote/<review_id>/<vote_type>", methods = ['GET','POST'])
@login_required("user")
def voteReview(review_id, vote_type):
    return social.voteReview(review_id, vote_type)

@app.route("/user/<username>", methods = ['POST', 'GET'])
def viewUser(username):
    return social.viewUser(username)    

@app.route("/user/<username>/trustVote/<vote_val>", methods = ['GET','POST'])
@login_required("user")
def trustVoteUser(username, vote_val):
    return social.trustVoteUser(username, vote_val)


if __name__ == '__main__':
    app.run(debug=True)
