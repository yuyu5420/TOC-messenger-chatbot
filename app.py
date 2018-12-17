#Python libraries that we need to import for our bot
import random
from bottle import static_file
from flask import Flask, request
from fbmq import Page
from fbmq import Attachment, Template, QuickReply, Page
from fsm import TocMachine 
import os

app = Flask(__name__)
ACCESS_TOKEN = 'EAAE76EQAyvkBAICpHDgGVsN4VinEMFWPJGcTj55F3CnxL9sp3ny2tBbvHLtUvZCmZClDtVrXkQ0Ayt6PKxomCmVQ54IySasQC5mNXUageyeA9Rer1vq9ZCvDIlnwHfpBfINN4jpBZAZAgHB1zzQZCLyh52ll1fTBFVnJwIvq94n10ZCxFSpeczW'
VERIFY_TOKEN = '123'
#PORT = os.environ['PORT']

page = Page(ACCESS_TOKEN)
machine = TocMachine();

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET'])
def receive_message():
    if request.method == 'GET':
        # Before allowing people to message your bot, Facebook has implemented a verify token
        # that confirms all requests that your bot receives came from Facebook.
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)

    #if the request was not get, it must be POST and we can just proceed with sending a message back to user

@app.route("/", methods=['POST'])
def webhook_handler():
	body = request.get_json()
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

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["777", "0.0"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user 

if __name__ == "__main__":
    app.run(debug=True)
