from flask import Flask, request, jsonify

app = Flask(__name__)

DATA = {
    "laptop": ["Dell XPS 13", "MacBook Air", "HP Spectre"],
    "phone": ["iPhone 14", "Samsung S22", "Pixel 7"],
    "headphones": ["Sony WH-1000XM4", "Bose QC45", "AirPods Pro"]
}

@app.route("/find", methods=["GET"])
def find_best():
    query = request.args.get("query", "").lower()
    results = DATA.get(query, ["No results found. Try laptop, phone, or headphones."])
    return jsonify({"query": query, "results": results})

@app.route("/", methods=["GET"])
def home():
    return "Best API is running!"

if __name__ == "__main__":
    app.run()
