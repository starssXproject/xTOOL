import os
import shutil
import time
import sys
import threading
from colorama import init, Fore, Style

init()

def force_delete(path):
    try:
        if os.path.isfile(path) or os.path.islink(path):
            os.chmod(path, 0o777)
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        else:
            print(f"{Fore.RED}Error: {path} not found.{Style.RESET_ALL}")
            return False
        return True
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        return False

def loading_bar(path):
    for i in range(1, 101):
        if not os.path.exists(path):
            break
        sys.stdout.write(f"\r{Fore.YELLOW}Deleting... [{'#' * i:<100}] {i}%{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.05)  # 5 seconds for full bar
    sys.stdout.write("\r" + " " * 120 + "\r")
    sys.stdout.flush()

def loading_animation(path):
    thread = threading.Thread(target=loading_bar, args=(path,))
    thread.start()
    start_time = time.time()
    success = force_delete(path)
    elapsed_time = time.time() - start_time
    if elapsed_time < 1:
        time.sleep(1 - elapsed_time)  # Ensure at least 1 second for the animation
    thread.join()
    if success:
        print(f"{Fore.GREEN}Successfully deleted: {path}{Style.RESET_ALL}")
