from flask import Flask, request
import ipaddress

app = Flask(__name__)

def classify_ip(ip):
    try:
        addr = ipaddress.ip_address(ip)

        if addr.is_loopback:
            return "Loopback / local system"
        if addr.is_private:
            return "Private / internal network"
        if addr.is_reserved:
            return "Reserved address"
        return "Public internet address"

    except ValueError:
        return "Unknown"

@app.route("/")
def test():

    forwarded = request.headers.get("X-Forwarded-For", "")
    forwarded_ips = [x.strip() for x in forwarded.split(",") if x.strip()]

    client_ip = forwarded_ips[0] if forwarded_ips else request.remote_addr

    user_agent = request.headers.get("User-Agent", "Unknown")
    referer = request.headers.get("Referer", "None")
    language = request.headers.get("Accept-Language", "Unknown")

    print("\n========== NEW VISIT ==========")
    print("Visible client IP:", client_ip)
    print("IP type:", classify_ip(client_ip))
    print("Full X-Forwarded-For:", forwarded)
    print("remote_addr:", request.remote_addr)
    print("User-Agent:", user_agent)
    print("Referer:", referer)
    print("Language:", language)

    # Basic browser/device hints
    ua = user_agent.lower()

    if "iphone" in ua:
        device = "iPhone"
    elif "android" in ua:
        device = "Android device"
    elif "windows" in ua:
        device = "Windows computer"
    elif "macintosh" in ua:
        device = "Mac"
    else:
        device = "Unknown device"

    if "instagram" in ua:
        browser = "Instagram in-app browser"
    elif "facebookexternalhit" in ua:
        browser = "Facebook/Meta automated fetch"
    elif "google-lens" in ua:
        browser = "Google Lens automated fetch"
    elif "chrome" in ua:
        browser = "Chrome"
    elif "safari" in ua:
        browser = "Safari"
    else:
        browser = "Unknown browser/client"

    print("Detected device:", device)
    print("Detected client:", browser)
    print("===============================\n")

    return f"""
    <h2>Networking Experiment</h2>

    <p>Request received successfully.</p>

    <h3>Connection information</h3>

    <p><b>Visible IP:</b> {client_ip}</p>
    <p><b>Address type:</b> {classify_ip(client_ip)}</p>
    <p><b>Device:</b> {device}</p>
    <p><b>Browser/client:</b> {browser}</p>

    <p style="margin-top:30px;">
    This experiment demonstrates what basic network metadata
    a web server can observe from an HTTP request.
    </p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
