
import socket

def check_port(host, port):
    try:
        # Create a socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout
        s.settimeout(3)

        # Check port status
        result = s.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN on {host}")
        elif result == 111 or result == 10061:
            print(f"Port {port} is CLOSED on {host}")
        else:
            print(f"Port {port} is FILTERED or UNREACHABLE")
            
        s.close()

    except socket.gaierror:
        print("Invalid hostname or IP address.")

    except ValueError:
        print("Please enter a valid port number.")

    except socket.error as error:
        print("Network error:", error)


# Main program
print("===== PORT STATUS CHECKER =====")

host = input("Enter system hostname or IP address: ")

try:
    port = int(input("Enter port number: "))

    if 1 <= port <= 65535:
        check_port(host, port)
    else:
        print("Port number must be between 1 and 65535.")

except ValueError:
    print("Please enter a valid numeric port number.")
