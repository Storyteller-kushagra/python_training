from flask import Flask, request

from pymessenger.bot import Bot


app = Flask("hello")

VERIFY_TOKEN = "1234567890"
ACCESS_TOKEN = "EAAIxI7TsZBEQBAE6cb78KhM4ZB5WjSFfVFmrWPq37URzNcBkAcEjYmFw9T7dIGpJ88cnLrE5DXU67LnXP4LzROjRJehipdulecHoWfZAjIbQPqZAwJRKhlcZBZCGDzsDU0CfDE9sCa7nZAJrX0eaKRgIZBz8mfXLehCblDLQ4NFvFxpv64LVLtvK"
pybot= Bot(ACCESS_TOKEN)

@app.route("/check/", methods=["GET"])
def sayhi():
    return "working"


@app.route("/callback/", methods=["GET"])
def get_callback():
    if VERIFY_TOKEN == request.args.get("hub.verify_token"):
        return request.args.get("hub.challenge")
    else:
        return "not working"


@app.route("/callback/", methods=["POST"])
def post_callback():
    output = request.get_json()

    for entry in output.get("entry"):
        if "messaging" in entry:
            for messaging in entry.get("messaging"):
                sender = messaging.get("sender").get("id")
                recipient = messaging.get("recipient").get("id")

                text = "You sent an attachment"

                if "text" in messaging.get("message"):
                    text = messaging.get("message").get("text")

                print(sender, recipient, text)

                pybot.send_text_message(sender, text)
                image_url = r"https://images.unsplash.com/photo-1566487097168-e91a4f38bee2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80"
                pybot.send_image_url(sender, image_url)

    return "done"

app.run()