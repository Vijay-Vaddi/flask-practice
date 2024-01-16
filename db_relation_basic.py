# basic.py file 
# create database entries using Models created in models file.

from db_relationships import db, Puppy, Owner, Toy

# create 2 puppy objects

rufus = Puppy('Rufus', 2)
bruno = Puppy('Bruno', 1)

# add puppies to db
db.session.add_all([rufus, bruno])
db.session.commit()

# check 
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
# get the first item named rufus. can do .all()[0]

# create owner object

jose = Owner('Jose', rufus.id)

# give puppy a toy, one to many relationship
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Squeeky Ball', rufus.id)

db.session.add_all([jose, toy1,toy2])
db.session.commit()

# grab items after adding to db. 

rufus = Puppy.query.filter_by(name = 'Rufus').first()
print(rufus)

rufus.report_toys()


