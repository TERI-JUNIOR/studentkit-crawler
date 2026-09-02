from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "service": "StudentKit Crawler"
    })


@app.route("/crawl")
def crawl():

    url = request.args.get("url")

    if not url:
        return jsonify({
            "success": False,
            "error": "No URL provided"
        }), 400

    return jsonify({
        "success": True,
        "url": url,
        "siteName": "Loading...",
        "title": "Loading...",
        "description": "Loading...",
        "faviconUrl": ""
    })


if __name__ == "__main__":
    app.run()
