import jinja2, random
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, session, redirect, flash

from forms import CreateItem, EditItem, RegisterUser, LoginUser, UpdateHours
from model import connect_to_db, User, Item, db
from sqlalchemy import update




def username_exists(username):
    try: 
        user = User.query.filter_by(username=username).first()
        return user.user_name 
    except:
        return False 


print(username_exists("asdf"))