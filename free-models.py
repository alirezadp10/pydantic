import os, requests
from dotenv import load_dotenv
load_dotenv()

res = requests.get(
    "https://openrouter.ai/api/v1/models",
    headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}
)
for m in res.json()["data"]:
    if m.get("pricing", {}).get("prompt") == "0":
        print("FREE:", m["id"])
        print(m["description"])
        print("."*100)