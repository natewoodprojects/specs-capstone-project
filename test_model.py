
from db import session # probably a contextbound sessionmaker
from db import model

from sqlalchemy import create_engine

def setup():
    engine = create_engine('sqlite:///:memory:')
    session.configure(bind=engine)
    # You probably need to create some tables and 
    # load some test data, do so here.

    # To create tables, you typically do:
    model.metadata.create_all(engine)

def teardown():
    session.remove()


def test_something():
    instances = session.query(model.SomeObj).all()
    eq_(0, len(instances))
    session.add(model.SomeObj())
    session.flush()
    # ...