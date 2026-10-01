from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def test():
    print("remote_addr:", request.remote_addr)
    print("X-Forwarded-For:", request.headers.get("X-Forwarded-For"))

    return """
    <h2>Networking Experiment</h2>
    <p>Request received.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
