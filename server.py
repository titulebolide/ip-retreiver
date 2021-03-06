from flask import Flask, request
import os
import config
from apprise import Apprise

apprise = Apprise()
apprise.add(config.TGRAM_URL, tag="tgram")

app = Flask(__name__)

if not os.path.isfile('static/' + config.IMAGE_NAME):
    os.system(f"cd static && curl -o {config.IMAGE_NAME} https://upload.wikimedia.org/wikipedia/commons/4/49/Carte_identit%C3%A9_%C3%A9lectronique_fran%C3%A7aise_%282021%2C_recto%29.png")

@app.route(config.URL)
def index():
    ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    if ip is None:
        ip = request.environ['REMOTE_ADDR']
    msg = "New request from " + ip
    os.system(
        f"apprise -b '{msg}' {config.TGRAM_URL} &"
    )
    return f"<html><head></head><body><script>window.location='/static/{config.IMAGE_NAME}'</script></body></html>", 200

if __name__ == "__main__":
    app.run("localhost", 8000)