from db_basic import Puppy, db, app


with app.app_context():
    db.create_all()
    u1 = Puppy('Tom', 3)
    
    db.session.add(u1)
    db.session.commit()
    print(repr(u1))






