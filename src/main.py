import sys
from colorama import init, Fore, Style
from del_module import loading_animation
from szip_module import archive, extract

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

    """
    print(text)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        display_text()
    elif len(sys.argv) == 3 and sys.argv[1] == "del":
        path_to_delete = sys.argv[2]
        loading_animation(path_to_delete)
    elif len(sys.argv) >= 4 and sys.argv[1] == "szip":
        if sys.argv[2] == "-a":
            source_path = sys.argv[3]
            dest_path = sys.argv[4]
            archive(source_path, dest_path)
        elif sys.argv[2] == "-e":
            szip_path = sys.argv[3]
            dest_dir = sys.argv[5] if len(sys.argv) == 6 and sys.argv[4] == "-d" else "."
            extract(szip_path, dest_dir)
        else:
            print(f"Invalid command. Usage: xtool szip -a <source_path> <dest_path.szip> | xtool szip -e <source.szip> [-d <dest_dir>]")
    else:
        print(f"Invalid command. Usage: xtool del <path_to_delete> | xtool szip -a <source_path> <dest_path.szip> | xtool szip -e <source.szip> [-d <dest_dir>]")
