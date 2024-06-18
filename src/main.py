import os

def clear_screen():
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Linux and MacOS
        os.system('clear')

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
    clear_screen()
    display_text()
