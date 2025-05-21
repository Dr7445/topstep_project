import requests
import json
from datetime import datetime
import os

# --- Load the most recent token from logs ---
def load_token(path="logs/token_log.txt"):
    try:
        with open(path, "r") as f:
            last_line = f.readlines()[-1]
            token = last_line.strip().split(" - ")[-1]
            return token
    except Exception as e:
        print("❌ Could not load token:", e)
        return None

# --- Fetch data from an API endpoint ---
def fetch_data(endpoint, token, payload):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "accept": "application/json"
    }

    response = requests.post(endpoint, headers=headers, json=payload)
    try:
        return response.json()
    except:
        print("⚠️ Couldn’t parse JSON.")
        return response.text


# --- Save output to file ---
def save_data(data, filename="data/api_response.json"):
    os.makedirs("data", exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Data saved to {filename}")

# --- Main execution ---
if __name__ == "__main__":
    endpoint = "https://api.topstepx.com/api/Account/search"
    payload = { "onlyActiveAccounts": True }

    token = load_token()
    if not token:
        exit()

    print(f"🔐 Using token: {token[:30]}...")

    data = fetch_data(endpoint, token, payload)
    print("🔎 Response Preview:")
    print(json.dumps(data, indent=2) if isinstance(data, dict) else data)

    save_data(data)

