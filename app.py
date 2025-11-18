from flask import Flask, request, jsonify

app = Flask(__name__)

def custom_gpt(query):
    query = query.lower()
    
    # Simple rule-based responses
    if "hello" in query or "hi" in query:
        return "Hello! How can I help you today?"
    elif "weather" in query:
        return "I can’t fetch real-time weather yet, but it’s always a good day to code!"
    elif "joke" in query:
        return "Why did the computer go to the doctor? Because it caught a virus! 😄"
    elif "help" in query:
        return "I can answer simple questions. Try asking me for a joke or say hello!"
    else:
        return f"You asked: '{query}'. I’m still learning, but I’ll try my best!"

@app.route("/ask", methods=["GET"])
def ask_gpt():
    query = request.args.get("query", "")
    answer = custom_gpt(query)
    return jsonify({"query": query, "answer": answer})

@app.route("/", methods=["GET"])
def home():
    return "Best API is running!"

if __name__ == "__main__":
    app.run(debug=True)
