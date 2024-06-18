import os
import zipfile
from cryptography.fernet import Fernet
from colorama import init, Fore, Style

init()

KEY_FILE = 'encryption.key'

def load_key():
    """Load the encryption key from a file"""
    return open(KEY_FILE, 'rb').read()

def generate_and_save_key():
    """Generate a new encryption key and save it to a file"""
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def get_cipher_suite():
    """Get the cipher suite, generating a new key if necessary"""
    if not os.path.exists(KEY_FILE):
        key = generate_and_save_key()
    else:
        key = load_key()
    return Fernet(key)

cipher_suite = get_cipher_suite()

def archive(source_path, dest_path):
    with zipfile.ZipFile('temp.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isdir(source_path):
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    zipf.write(os.path.join(root, file),
                               os.path.relpath(os.path.join(root, file),
                               os.path.join(source_path, '..')))
        else:
            zipf.write(source_path, os.path.basename(source_path))

    with open('temp.zip', 'rb') as file:
        encrypted_data = cipher_suite.encrypt(file.read())
    
    with open(dest_path, 'wb') as file:
        file.write(encrypted_data)
    
    os.remove('temp.zip')
    print(f"{Fore.GREEN}Successfully archived: {source_path} to {dest_path}{Style.RESET_ALL}")

def extract(szip_path, dest_dir):
    with open(szip_path, 'rb') as file:
        encrypted_data = file.read()
    
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    with open('temp.zip', 'wb') as file:
        file.write(decrypted_data)
    
    with zipfile.ZipFile('temp.zip', 'r') as zipf:
        zipf.extractall(dest_dir)
    
    os.remove('temp.zip')
    print(f"{Fore.GREEN}Successfully extracted: {szip_path} to {dest_dir}{Style.RESET_ALL}")
