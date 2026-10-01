from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def test():
    ip = request.remote_addr
    print("Visitor IP:", ip)

    return f"""
    <h2>Networking Experiment</h2>
    <p>This page recorded the IP address associated with your connection:</p>
    <strong>{ip}</strong>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
