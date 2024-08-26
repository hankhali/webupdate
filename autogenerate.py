import bcrypt
import random
import string
import time

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to hash a password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Function to generate a unique username
def generate_username(existing_usernames):
    while True:
        username = f"user{random.randint(100, 999)}"
        if username not in existing_usernames:
            return username

# Open file to write user credentials
start_time = time.time()

try:
    with open('users.txt', 'w') as file:
        existing_usernames = set()
        for i in range(200):
            username = generate_username(existing_usernames)
            existing_usernames.add(username)
            password = generate_password()
            hashed_password = hash_password(password)  # Use hashed password here
            file.write(f'{username}:{password}\n')
            if i % 10 == 0:  # Print status every 10 iterations
                print(f'Processed {i + 1} users...')
except Exception as e:
    print(f"An error occurred: {e}")

end_time = time.time()
print(f"User credentials generated and saved to users.txt")
print(f"Time taken: {end_time - start_time} seconds")
