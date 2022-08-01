"""Utility file to seed gechur database data"""

from sqlalchemy import func

from model import Items, User, connect_to_db, db
from server import app