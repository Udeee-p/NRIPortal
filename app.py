from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = 'test'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return challenge, 200
        return 'Invalid verification token', 403
    elif request.method == 'POST':
        print("Received POST:", request.json)  # <--- THIS LINE
        return "OK", 200

if __name__ == "__main__":
    import os

    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)

