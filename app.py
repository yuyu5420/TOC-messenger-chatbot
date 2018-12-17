#Python libraries that we need to import for our bot
import random
from bottle import route, run, request, abort, static_file
from fbmq import Page
from fbmq import Attachment, Template, QuickReply, Page
from fsm import TocMachine 
import os

ACCESS_TOKEN = 'EAAE76EQAyvkBAICpHDgGVsN4VinEMFWPJGcTj55F3CnxL9sp3ny2tBbvHLtUvZCmZClDtVrXkQ0Ayt6PKxomCmVQ54IySasQC5mNXUageyeA9Rer1vq9ZCvDIlnwHfpBfINN4jpBZAZAgHB1zzQZCLyh52ll1fTBFVnJwIvq94n10ZCxFSpeczW'
VERIFY_TOKEN = '123'
PORT = os.environ['PORT']

page = Page(ACCESS_TOKEN)
machine = TocMachine();

@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
	body = request.json
	print('\nFSM STATE: ' + machine.state)
	print('REQUEST BODY: ')
	print(body)

	event = body['entry'][0]['messaging'][0]
	# only deal text messages
	if event['message'].get('text'):
		machine.advance(event)
	# initial state
	if machine.state == "init":
		sender_id = event['sender']['id']
		quick_replies = [QuickReply(title="休閒娛樂", payload="PICK_PLAY"), QuickReply(title="進食", payload="PICK_EAT"), QuickReply(title="睡覺", payload="PICK_SLEEP"), QuickReply(title="聊天", payload="PICK_TALK")]

		page.send(sender_id, "嗨~\n你現在想要做什麼呢?",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")

	return 'OK'

if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)

