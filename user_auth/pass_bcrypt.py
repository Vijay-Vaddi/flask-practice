from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'hello123'

hashed_pass = bcrypt.generate_password_hash(password=password)
print(hashed_pass)

chek_pass = bcrypt.check_password_hash(hashed_pass, 'hello123')
print(chek_pass)
