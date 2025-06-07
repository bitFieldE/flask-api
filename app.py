from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/top')
def top():
    return jsonify({
        "message": "Hello, Flask!",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)