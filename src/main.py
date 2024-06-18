import os
import sys
import ctypes
import time
from colorama import init, Fore, Style

init()

def display_text():
    text = r"""
       ___________________   ________  .____     
___  __\__    ___/\_____  \  \_____  \ |    |    
\  \/  / |    |    /   |   \  /   |   \|    |    
 >    <  |    |   /    |    \/    |    \    |___ 
/__/\_ \ |____|   \_______  /\_______  /_______ \
      \/                  \/         \/        \/
Version r0.0.1 starssXproject

Type 'help' for more information
    """
    print(text)

def force_delete(path):
    # Menggunakan ctypes untuk menghapus file/folder secara paksa
    if os.path.isfile(path) or os.path.islink(path):
        os.chmod(path, 0o777)
        ctypes.windll.kernel32.SetFileAttributesW(path, 0x80)  # Remove readonly attribute
        os.remove(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.chmod(file_path, 0o777)
                ctypes.windll.kernel32.SetFileAttributesW(file_path, 0x80)  # Remove readonly attribute
                os.remove(file_path)
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.chmod(dir_path, 0o777)
                ctypes.windll.kernel32.SetFileAttributesW(dir_path, 0x80)  # Remove readonly attribute
                os.rmdir(dir_path)
        os.rmdir(path)
    else:
        print(f"{Fore.RED}Error: {path} not found.{Style.RESET_ALL}")

def loading_animation(duration):
    chars = "/—\|"
    for i in range(duration * 4):
        sys.stdout.write(f"\r{Fore.YELLOW}Deleting... {chars[i % len(chars)]}{Style.RESET_ALL}")
        time.sleep(0.25)
        sys.stdout.flush()
    print("\r" + " " * 20 + "\r", end='')  # Menghapus baris loading

if __name__ == "__main__":
    if len(sys.argv) == 1:
        display_text()
    elif len(sys.argv) == 3 and sys.argv[1] == "del":
        path_to_delete = sys.argv[2]
        loading_animation(10)  # Durasi loading dalam detik
        force_delete(path_to_delete)
        print(f"{Fore.GREEN}Successfully deleted: {path_to_delete}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Invalid command. Usage: python main.py del <path_to_delete>{Style.RESET_ALL}")
