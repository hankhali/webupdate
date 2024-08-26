import bcrypt
import random
import string

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate a hashed password // use it for unique purchase code
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Function to generate a unique username
def generate_username(existing_usernames):
    while True:
        username = f"user{random.randint(1000, 9999)}"
        if username not in existing_usernames:
            return username

# Open file to write user credentials
try:
    with open('users.txt', 'w') as file:
        existing_usernames = set()
        for _ in range(200):
            username = generate_username(existing_usernames)
            existing_usernames.add(username)
            hashed_password = generate_password()
            # hashed_password = hash_password(password)
            file.write(f'{username}:{hashed_password}\n')
    print("User credentials generated and saved to users.txt")
except Exception as e:
    print(f"An error occurred: {e}")
