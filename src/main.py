import sys
from del_module import loading_animation  # Pastikan nama modulnya sesuai

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

if __name__ == "__main__":
    if len(sys.argv) == 1:
        display_text()
    elif len(sys.argv) == 3 and sys.argv[1] == "del":
        path_to_delete = sys.argv[2]
        loading_animation(path_to_delete)
    else:
        print(f"Invalid command. Usage: xtool del <path_to_delete>")
