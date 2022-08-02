import jinja2
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, session, redirect, flash

from forms import CreateItem, EditItem, RegisterUser, LoginUser
from model import connect_to_db, User, Item, db

app = Flask(__name__)

# A secret key is needed to use Flask sessioning features
app.secret_key = "39p4uhgau-ewvhoruawe4-9gfhap34u9bp-upsdzv923"

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

@app.route('/', methods=['GET', 'POST'])
def login():
    """First page is the login page"""
    form = LoginUser()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if not user: 
            return redirect("/login")
        if check_password_hash(user.password, password):
            flash("Logged in!")
            return redirect("/home")
        flash("Sorry, something went wrong!")
        return redirect("/")

    return render_template('/login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():    
    """Registering a user page"""

    form = RegisterUser()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("User Created")
        return redirect('/')
        
    return render_template('/register.html', form=form)

@app.route('/home', methods=['GET', 'POST'])
def home():    
    """A Users main page where they see all their items they're trying to use and maybe update their items"""

    '''
    I need to:
    Pull info from the database and display it. 
    Have different users logged in in order to create items. 
    '''

    items = Item.query.all()

    return render_template('/home.html', items=items)

@app.route('/create', methods=['GET', 'POST'])
def create():  
    """Page to create an item goal"""

    form = CreateItem()  

    if form.validate_on_submit():
        user_id = 1
        item_name = form.item_name.data
        cost_of_item = form.cost_of_item.data
        hours_to_use = form.hours_to_use.data
        hours_used = form.hours_used.data
        description = form.description.data
        new_item = Item(user_id=user_id, item_name=item_name, cost_of_item=cost_of_item, hours_to_use=hours_to_use, hours_used=0, completed=False, given_away=False, description=description)
        db.session.add(new_item)
        db.session.commit()
        flash(f"{item_name} Created")
        return redirect("/home")

    return render_template('/create.html', form=form)

@app.route('/edit', methods=['GET', 'POST'])
def edit():   


    form = EditItem() 
    return render_template('/edit.html', form=form)



if __name__ == "__main__":
    connect_to_db(app)
    app.env = "development" 
    app.run(debug=True)