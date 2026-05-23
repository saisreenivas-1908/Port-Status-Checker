import socket
import time

# Banner
print("=" * 60)
print("              ADVANCED PORT SCANNER")
print("=" * 60)

# Get target
target = input("Enter Target IP or Domain: ")

# Function to scan a port
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown Service"

            print(f"[OPEN]   Port {port} - {service}")

        else:
            print(f"[CLOSED] Port {port}")

        s.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Server not responding.")

# Start time
start_time = time.time()

# Menu
print("\n1. Scan Single Port")
print("2. Scan Common Ports")

choice = input("\nEnter your choice (1 or 2): ")

# Single Port Scan
if choice == "1":
    port = int(input("Enter Port Number: "))
    print("\nScanning...\n")
    scan_port(target, port)

# Common Port Scan
elif choice == "2":

    common_ports = [
        20, 21, 22, 23, 25,
        53, 80, 110, 123,
        135, 139, 143, 443, 445
    ]

    print("\nScanning Common Ports...\n")

    for port in common_ports:
        scan_port(target, port)

else:
    print("Invalid Choice")

# End time
end_time = time.time()

print("\n" + "=" * 60)
print(f"Scanning Completed in {round(end_time - start_time, 2)} seconds")
print("=" * 60)
