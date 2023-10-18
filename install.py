import sys, time, os


def m(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

os.system("clear")
print("""
██████╗ ██████╗  ██████╗ ██╗    ██╗██╗  ██╗██╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██║    ██║██║ ██╔╝██║██╔══██╗
██║  ██║██████╔╝██║   ██║██║ █╗ ██║█████╔╝ ██║██║  ██║
██║  ██║██╔══██╗██║   ██║██║███╗██║██╔═██╗ ██║██║  ██║
██████╔╝██║  ██║╚██████╔╝╚███╔███╔╝██║  ██╗██║██████╔╝
╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚═════╝ 

""")
m('\x1b[00m\033[041m REPOSITORIO DE BOT PARA TELEGRAM ESCRITO EN LENGUAJE PYTHON Y JAVASCRIPT!! \033[00m')
os.system("pkg update -y")
os.system("pkg upgrade -y")
os.system("pkg install nano")
os.system("pkg install python -y")
os.system("pkg install python2 -y")
os.system("pkg install nodejs -y")
os.system("pkg install libwebp -y")
os.system("pkg install ffmpeg -y")
os.system("npm install")
os.system("npm audit fix")
os.system("npm install axios")
os.system("npm install telegraf@3.32")
m('\x1b[00m\033[041m @drowkid01 | 2022-11-12 ...  \033[00m')
os.system("clear")
os.system("python start.py")
m("\033[1;32m[✓]PAQUETES INSTALADOS CORRECTAMENTE[✓]")
