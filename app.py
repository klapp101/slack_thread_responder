import os
from slack_sdk import WebClient
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()

app = App(token=os.environ["SLACK_BOT_TOKEN"])
user_client = WebClient(token=os.environ["SLACK_USER_TOKEN"])
slack_user_id = os.environ["SLACK_USER_ID"]

@app.event("message")
def auto_respond(event, say):
    channel = event["channel"]
    ts = event["ts"]
    text = event.get("text", "").lower()
    
    if "ufc" in text and ("code" in text or "codes" in text):
        try:
            user_client.chat_postMessage(
                channel=channel,
                text="Me please!",
                thread_ts=ts,
                username=slack_user_id
            )
        except Exception as e:
            print(f"Error responding to message: {e}")

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()