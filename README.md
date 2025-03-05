# PHP-RCE-8-3-8

This PoC would target PHP running on Windows systems with PHP-CGI in environments where Unicode characters are improperly handled.

Explanation:

    TARGET_URL: Replace this with the target server running PHP-CGI.
    CMD: The system command to be executed remotely.
    PAYLOAD: The injection payload with PHP settings manipulated via command-line switches (-d).
    URL Encoding: Bypasses filters by encoding special characters.
    PHP Payload: Injected PHP code to execute system commands.

⚠️ Disclaimer:

This script is for educational and research purposes only. Unauthorized use of this exploit against systems without permission is illegal. Always use such information responsibly in legal, ethical contexts like penetration testing within authorized environments.
