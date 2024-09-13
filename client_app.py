import requests
import zipfile
import os
import hashlib

# URL of the server
url = 'http://localhost:8000/generate'

# Make a request to the server
response = requests.get(url)

# Save the received zip file
zip_filename = 'received_files.zip'
with open(zip_filename, 'wb') as f:
    f.write(response.content)

# Unzip the received file
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall('/clientdata')

# Read the random file content
random_file_path = os.path.join('/clientdata', 'random_file.txt')
with open(random_file_path, 'r') as random_file:
    random_file_content = random_file.read()

# Compute the hash of the random file
computed_hash = hashlib.sha256(random_file_content.encode('utf-8')).hexdigest()

# Read the hash from the hash file
hash_file_path = os.path.join('/clientdata', 'file_hash.txt')
with open(hash_file_path, 'r') as hash_file:
    received_hash = hash_file.read().strip()

# Compare the computed hash with the received hash
if computed_hash == received_hash:
    print("Hash matched!")
else:
    print("Hash did not match!")

# Clean up the extracted files (optional)
os.remove(zip_filename)
