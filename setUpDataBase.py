from db_basic import db, Puppy, app

sam = Puppy("Sammy", 2)
frank = Puppy("Frank", 3)

with app.app_context():
    db.create_all()
    # does not update tables if they are already in database
    db.session.add_all([sam,frank])
    
    db.session.commit()




print(sam.id)
print(sam.name)
