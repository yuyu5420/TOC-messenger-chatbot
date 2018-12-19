#Python libraries that we need to import for our bot

from bottle import route, run, request, abort, static_file
from fbmq import Attachment, Template, QuickReply, Page
from fsm import TocMachine 
import os

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERTIFY_TOKEN']
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
	global Records
	sender_id = event['sender']['id']
	if Records[sender_id]:
		machine.state = Records[sender_id]
	else:
		Records[sender_id] = machine.state
	print('\nFSM STATE: ' + machine.state)
	print('REQUEST BODY: ')
	print(body)

	event = body['entry'][0]['messaging'][0]
	# only deal text messages
	if event['message'].get('text'):
		machine.advance(event)
	# initial state
	if machine.state == "init":
		quick_replies = [QuickReply(title="休閒娛樂", payload="PICK_PLAY"), QuickReply(title="進食", payload="PICK_EAT"), QuickReply(title="睡覺", payload="PICK_SLEEP"), QuickReply(title="聊天", payload="PICK_TALK")]
		page.send(sender_id, "嗨~\n你現在想要做什麼呢?",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")

	return 'OK'

if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)

