import requests
import json
from datetime import datetime

# --- Config ---
USERNAME = "TOPSTEP_USERNAME"
API_KEY = "TOPSTEP_API"
LOGIN_URL = "https://api.topstepx.com/api/Auth/loginKey"

# --- Auth Request ---
payload = {
    "userName": USERNAME,
    "apiKey": API_KEY
}

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(LOGIN_URL, headers=headers, json=payload)

# --- Response Handling ---
try:
    result = response.json()
    print(json.dumps(result, indent=2))

    if result.get("success"):
        token = result.get("token")
        print(f"\n🎉 Token acquired: {token}")

        with open("logs/token_log.txt", "a") as f:
            f.write(f"{datetime.now().isoformat()} - {token}\n")
            print("📝 Token saved to logs/token_log.txt")

    else:
        print("\n❌ Authentication failed.")
        print(f"Error code: {result.get('errorCode')}")
        print(f"Error message: {result.get('errorMessage')}")

except Exception as e:
    print("⚠️ Error parsing response:", e)

#
