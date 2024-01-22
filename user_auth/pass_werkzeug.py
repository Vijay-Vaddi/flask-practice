from werkzeug.security import generate_password_hash, check_password_hash

# no need to create an instance 
hashed_pass = generate_password_hash('hello123')
print(hashed_pass)

check = check_password_hash(hashed_pass, 'hello123')
print(check)