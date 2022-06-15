from linebot import WebhookParser
from linebot.models import TextSendMessage
from linebot import LineBotApi
from decouple import config

from scraping import scraping_contribution

ACCESS_TOKEN = config("ACCESS_TOKEN")
SECRET = config("CHANNEL_SECRET")
USER_ID = config("USER_ID")

line_api = LineBotApi(channel_access_token=ACCESS_TOKEN)
parser = WebhookParser(channel_secret=SECRET)


def push_contribution_count():
    contribution_count = scraping_contribution()
    if contribution_count < 1:
        text = f"contribution : {contribution_count}\n遊んでる暇があったらコード書け"
    else:
        text = f"contribution : {contribution_count}\n素晴らしい！この調子で毎日コードを書きましょう！"
    messages = TextSendMessage(text=text)
    line_api.push_message(USER_ID, messages=messages)


def main():
    push_contribution_count()


if __name__ == "__main__":
    main()
