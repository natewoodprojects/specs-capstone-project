from flask import Flask, render_template
from forms import CreateItem, EditItem, RegisterUser, LoginUser

app = Flask(__name__)

app.secret_key = "39p4uhgau-ewvhoruawe4-9gfhap34u9bp-upsdzv923"

@app.route('/', methods=['GET', 'POST'])
def login():
    """First page is the login page"""

    form = LoginUser()
    return render_template('/login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():    
    """Registering a user page"""

    form = RegisterUser()
    return render_template('/register.html', form=form)

@app.route('/home', methods=['GET', 'POST'])
def home():    
    """A Users main page where they see all their items they're trying to use and maybe update their items"""

    return render_template('/home.html')

@app.route('/create', methods=['GET', 'POST'])
def create():  
    """Page to create an item goal"""

    form = CreateItem()  
    return render_template('/create.html', form=form)

@app.route('/edit', methods=['GET', 'POST'])
def edit():   


    form = EditItem() 
    return render_template('/edit.html', form=form)



if __name__ == "__main__":
    app.run()