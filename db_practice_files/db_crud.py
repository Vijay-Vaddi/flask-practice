from db_basic import db, Puppy

# create
my_pup = Puppy('Bruno', '3')
db.session.add(my_pup)
db.session.commit()

# # read
# all_pups = Puppy.query.all()
# print(all_pups)

# select by ID
# pup1 = Puppy.query.get(1)
# print(pup1.name)

# filters
# filter by command produces sql code
pup_frankie = Puppy.query.filter_by(name='Frankie')
print(pup_frankie.all())

# update , grab , change value, then upload whole obj

pup6 = db.session.get(Puppy, 6)
pup6.name = 'Jimmy'
db.session.add(pup6)
db.session.commit()

# delete 
pup3 = db.session.get(Puppy, 3)
db.session.delete(pup3)
db.session.commit()

# pup_obj = Puppy.query.get(1) is now depreciated and is part of legacy. still can be called but throws a warning. 
all_pups = db.session.get(Puppy, 1)
print(all_pups)

  