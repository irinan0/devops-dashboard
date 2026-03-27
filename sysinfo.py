import socket
import getpass

def show_sysinfo():
    print(f"Hostname: {socket.gethostname()}")
    print(f"User: {getpass.getuser()}")
    print(f"Current Directory: {os.getcwd()}")
