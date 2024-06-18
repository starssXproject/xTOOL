import os
import zipfile
import base64
from cryptography.fernet import Fernet
from colorama import init, Fore, Style
from tqdm import tqdm

init()

def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()

def get_cipher_suite(key):
    """Get the cipher suite using the provided key."""
    return Fernet(key)

def archive(source_path, dest_path):
    key = generate_key()
    cipher_suite = get_cipher_suite(key)

    total_size = 0
    if os.path.isdir(source_path):
        for root, dirs, files in os.walk(source_path):
            for file in files:
                total_size += os.path.getsize(os.path.join(root, file))
    else:
        total_size = os.path.getsize(source_path)

    with zipfile.ZipFile('temp.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isdir(source_path):
            with tqdm(total=total_size, desc="Archiving", unit="B", unit_scale=True) as pbar:
                for root, dirs, files in os.walk(source_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, os.path.join(source_path, '..')))
                        pbar.update(os.path.getsize(file_path))
        else:
            with tqdm(total=total_size, desc="Archiving", unit="B", unit_scale=True) as pbar:
                zipf.write(source_path, os.path.basename(source_path))
                pbar.update(total_size)

    with open('temp.zip', 'rb') as file:
        encrypted_data = cipher_suite.encrypt(file.read())

    with zipfile.ZipFile(dest_path, 'w') as szip:
        szip.writestr('data.enc', encrypted_data)
        szip.writestr('key.enc', base64.urlsafe_b64encode(key))

    os.remove('temp.zip')
    print(f"{Fore.GREEN}Successfully archived: {source_path} to {dest_path}{Style.RESET_ALL}")

def extract(szip_path, dest_dir):
    with zipfile.ZipFile(szip_path, 'r') as szip:
        key = base64.urlsafe_b64decode(szip.read('key.enc'))
        cipher_suite = get_cipher_suite(key)
        encrypted_data = szip.read('data.enc')

    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open('temp.zip', 'wb') as file:
        file.write(decrypted_data)

    with zipfile.ZipFile('temp.zip', 'r') as zipf:
        total_size = sum(info.file_size for info in zipf.infolist())
        with tqdm(total=total_size, desc="Extracting", unit="B", unit_scale=True) as pbar:
            for file in zipf.namelist():
                zipf.extract(file, dest_dir)
                pbar.update(zipf.getinfo(file).file_size)

    os.remove('temp.zip')
    print(f"{Fore.GREEN}Successfully extracted: {szip_path} to {dest_dir}{Style.RESET_ALL}")
