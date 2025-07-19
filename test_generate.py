# test_generate.py
import requests

url = "http://127.0.0.1:5002/generate_smart_tweet"

data = {
    "company": "Nike",
    "industry": "sportswear",
    "word_count_target": 12,
    "sentiment_target": 0.6,
    "has_media": 1
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
try:
    print("📝 Tweet:", response.json().get("tweet"))
    print("❤️ Predicted Likes:", response.json().get("predicted_likes"))
except Exception as e:
    print("❌ JSON decode failed:", e)
    print("Raw Response:", response.text)
