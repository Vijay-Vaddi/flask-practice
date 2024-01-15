from db_basic import Puppy, db


db.create_all()
tom = Puppy('Tom', 3)
frank = Puppy('Frankie', 4)

db.session.add_all([tom, frank])
db.session.commit()

print(tom.id)
print(frank.name)






