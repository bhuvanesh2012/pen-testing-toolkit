from port_scanner import scan_ports
from brute_forcer import brute_force_login

def menu():
    while True:
        print("\n=== Penetration Testing Toolkit ===")
        print("1. Port Scanner")
        print("2. Brute Force Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print("\n--- Port Scanner ---")
            target = input("Enter target IP (e.g., 192.168.1.1): ")
            port_range = input("Enter port range (e.g., 20-100): ")
            start_port, end_port = map(int, port_range.split('-'))
            scan_ports(target, start_port, end_port)

        elif choice == "2":
            print("\n--- Brute Forcer ---")
            url = input("Enter target URL: ")
            username = input("Enter username: ")
            wordlist = input("Enter path to password wordlist (e.g., passwords.txt): ")
            brute_force_login(url, username, wordlist)

        elif choice == "3":
            print("\nExiting... ✅")
            break
        else:
            print("Invalid option. Try again.")

menu()