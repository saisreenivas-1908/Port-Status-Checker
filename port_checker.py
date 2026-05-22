import socket

def check_port(host, port):
    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout
        s.settimeout(1)

        # Check port connection
        result = s.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} on {host} is OPEN")
        else:
            print(f"Port {port} on {host} is CLOSED")

        s.close()

    except Exception as e:
        print("Error:", e)

# User Input
host = input("Enter target IP or domain: ")
port = int(input("Enter port number: "))

# Function call
check_port(host, port)