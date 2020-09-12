import socket

def check_no_network():
    """Returns True if disconnected"""
    try:
        print(socket.gethostbyname("www.google.com"))
        return False
    except:
        return True
print(check_no_network())