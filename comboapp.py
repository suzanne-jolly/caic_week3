from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate_smart_tweet", methods=["POST"])
def generate_smart_tweet():
    data = request.json
    company = data.get("company", "Nike")
    return jsonify({
        "tweet": f"Sample tweet for {company}",
        "predicted_likes": 123
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "Combo API is up!"})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
