import flask
import os
import requests
import config
from apprise import Apprise
import asyncio

apprise = Apprise()
apprise.add(config.TGRAM_URL, tag="tgram")

app = flask.Flask(__name__)
false_name = "ed85436e-14f9-481c-b011-e43a24f90810.png"

if not os.path.isfile('static/' + false_name):
    os.system(f"cd static && curl -o {false_name} https://upload.wikimedia.org/wikipedia/commons/4/49/Carte_identit%C3%A9_%C3%A9lectronique_fran%C3%A7aise_%282021%2C_recto%29.png")

@app.route("/")
def index():
    msg = "New request from " + flask.request.remote_addr
    os.system(
        f"apprise -b '{msg}' {config.TGRAM_URL} &"
    )
    return f"<html><head></head><body><script>window.location='/static/{false_name}'</script></body></html>", 200

if __name__ == "__main__":
    app.run("localhost", 8000)