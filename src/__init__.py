"""
gechur is a web application that allowes its users to register a profile, add items to their home, update the number of hours they've used them, and view other people's items. The end goal is to give users a quilt free conscience from the items they've spent money on. 
"""

import jinja2, random, os
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, session, redirect, flash
from sqlalchemy import update
from flask_migrate import Migrate

from .forms import CreateItem, EditItem, RegisterUser, LoginUser, UpdateHours
from .model import connect_to_db, User, Item, db


app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]
app.jinja_env.undefined = jinja2.StrictUndefined
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

Migrate(app, db)

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
            session['username'] = form.username.data
            flash("Logged in!", "success")
            return redirect("/home")
        flash("Sorry, something went wrong!", "warning")
        return redirect("/")

    return render_template('/login.html', form=form)

@app.route('/logout')
def logout():
    """Ends the user session"""
    
    del session['username']
    flash("Logged out.", "success")
    return redirect("/")

@app.route('/register', methods=['GET', 'POST'])
def register():    
    """Registering a user page"""

    form = RegisterUser()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        if email == "":
            flash("Please include email", 'warning')
            return redirect('/register')
        if password != confirm_password:
            flash("Passwords do not match", 'warning')
            return redirect('/register')
        password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("User Created", "success")
        return redirect('/')
        
    return render_template('/register.html', form=form)

@app.route('/home', methods=['GET', 'POST'])
def home():    
    """A Users main page where they see all their items they're trying to use and update their items"""

    if 'username' not in session:
        flash("You are not logged in.", "warning")
        return redirect('/')

    user_file = (User.query.filter_by(username=(session['username'])).one())
    user_id = user_file.user_id

    items = Item.query.filter_by(user_id=user_id)

    form = UpdateHours()

    if form.validate_on_submit():
        pass
    return render_template('/home.html', items=items, form=form)

@app.route('/create', methods=['GET', 'POST'])
def create():  
    """Page to create an item goal"""

    if 'username' not in session:
        flash("You are not logged in.", "warning")
        return redirect('/')

    form = CreateItem()  

    if form.validate_on_submit():

        user_file = (User.query.filter_by(username=(session['username'])).one())
        user_id = user_file.user_id
        item_name = form.item_name.data
        cost_of_item = form.cost_of_item.data
        hours_to_use = form.hours_to_use.data
        description = form.description.data
        photo = form.photo.data
        new_item = Item(user_id=user_id, item_name=item_name, cost_of_item=cost_of_item, hours_to_use=hours_to_use, hours_used=0, completed=False, given_away=False, description=description, photo=photo)
        db.session.add(new_item)
        db.session.commit()
        flash(f"{item_name} Created", "success")
        return redirect("/home")

    return render_template('/create.html', form=form)


@app.route("/view-all", methods=['GET', 'POST'])
def view_all():

    users = User.query.all()
    items = (Item.query.all())
    return render_template('/view-all.html', items=items, users=users)

@app.route('/edit/<item_id>', methods=['GET', 'POST'])
def edit_item(item_id):   
    
    '''Fully Functional edit file'''

    form = EditItem() 

    if 'username' not in session:
        flash("You are not logged in.", "warning")
        return redirect('/')

    item_file = (Item.query.filter_by(item_id=item_id).one())
    item_user_id = item_file.user_id
    
    user_file = (User.query.filter_by(username=(session['username'])).one())
    user_id = user_file.user_id

    if user_id != item_user_id:
        flash("That's not your item, how'd you do that?", "warning")
        return redirect('/home')
    
    item_file = (Item.query.filter_by(item_id=item_id).one())

    if form.validate_on_submit():
        item_file = Item.query.filter_by(item_id=item_id).one()
        item_file.hours_used = int(item_file.hours_used) + int(form.hours_to_use.data)
        
        db.session.add(item_file)
        db.session.commit()

        if item_file.hours_used > item_file.hours_to_use:
            item_file.completed = True
            db.session.add(item_file)
            db.session.commit()
            flash(f"Congrats! You completed your hourly goal for {item_file.item_name}! Think about giving it away or something!", "success")

        return redirect('/home')

    title = item_file.item_name

    return render_template('/edit.html', form=form, title=title)

@app.route('/delete/<item_id>', methods=['GET', 'POST'])
def delete(item_id):   
    
    if 'username' not in session:
        flash("You are not logged in.", "warning")
        return redirect('/')
    
    item_file = (Item.query.filter_by(item_id=item_id).one())
    item_user_id = item_file.user_id
    
    user_file = (User.query.filter_by(username=(session['username'])).one())
    user_id = user_file.user_id

    if user_id != item_user_id:
        flash("This is not your item, how did you get here?", "warning")

    item_file = (Item.query.filter_by(item_id=item_id).one())
    db.session.delete(item_file)
    db.session.commit()

    return redirect('/home')

@app.route("/delete-page/<item_id>", methods=['GET', 'POST'])
def delete_page(item_id):
    

    item_file = Item.query.filter_by(item_id=item_id).one()
    item_name = item_file.item_name

    return render_template("/delete.html", item_id=item_id, item_name=item_name)


if __name__ == "__main__":
    connect_to_db(app)
    app.env = "development" 
    app.run(debug=True)





    """  Register Page <br />
  Welcome to Gechur! <br />
  Use your stuff. Remove your stuff. Gechur money's worth."""