import requests
import json

SUPABASE_URL = "https://your-project-id.supabase.co"
SUPABASE_API_KEY = "your-api-key"

def upload_to_supabase(data):
    url = f"{SUPABASE_URL}/rest/v1/your_table"
    headers = {
        "Authorization": f"Bearer {SUPABASE_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        return True
    else:
        print("Error:", response.text)
        return False
