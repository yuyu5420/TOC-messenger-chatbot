from transitions.extensions import GraphMachine
from fbmq import Page
from fbmq import Attachment, Template, QuickReply, Page
import os
import random

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERTIFY_TOKEN']

page = Page(ACCESS_TOKEN)

class TocMachine(GraphMachine):
	def __init__(self, **machine_configs):
		self.machine = GraphMachine(
		model=self,
		states=[
			'init',
			'playing',
			'eatting',
			'sleeping',
			'talking',
			'music',
			'game',
			'exercise',
			'drinking',
			'meal',
			'dessert',
			'8hr',
			'12hr',
			'24hr',
			'man',
			'woman',
			'bye'
		],
		transitions=[
			{
 				'trigger': 'advance',
				'source': 'init',
				'dest': 'playing',
				'conditions': 'is_going_to_playing'
			},
			{
 				'trigger': 'advance',
				'source': 'init',
				'dest': 'eatting',
				'conditions': 'is_going_to_eatting'
			},
			{
 				'trigger': 'advance',
				'source': 'init',
				'dest': 'talking',
				'conditions': 'is_going_to_talking'
			},
			{
 				'trigger': 'advance',
				'source': 'init',
				'dest': 'sleeping',
				'conditions': 'is_going_to_sleeping'
			},
			{
 				'trigger': 'advance',
				'source': 'playing',
				'dest': 'game',
				'conditions': 'is_going_to_game'
			},
			{
 				'trigger': 'advance',
				'source': 'playing',
				'dest': 'music',
				'conditions': 'is_going_to_music'
			},
			{
 				'trigger': 'advance',
				'source': 'playing',
				'dest': 'exercise',
				'conditions': 'is_going_to_exercise'
			},
			{
 				'trigger': 'advance',
				'source': 'eatting',
				'dest': 'drinking',
				'conditions': 'is_going_to_drinking'
			},
			{
 				'trigger': 'advance',
				'source': 'eatting',
				'dest': 'meal',
				'conditions': 'is_going_to_meal'
			},
			{
 				'trigger': 'advance',
				'source': 'eatting',
				'dest': 'dessert',
				'conditions': 'is_going_to_dessert'
			},
			{
 				'trigger': 'advance',
				'source': 'sleeping',
				'dest': '8hr',
				'conditions': 'is_going_to_8hr'
			},
			{
 				'trigger': 'advance',
				'source': 'sleeping',
				'dest': '12hr',
				'conditions': 'is_going_to_12hr'
			},
			{
 				'trigger': 'advance',
				'source': 'sleeping',
				'dest': '24hr',
				'conditions': 'is_going_to_24hr'
			},
			{
 				'trigger': 'advance',
				'source': 'music',
				'dest': 'man',
				'conditions': 'is_going_to_man'
			},
			{
 				'trigger': 'advance',
				'source': 'music',
				'dest': 'woman',
				'conditions': 'is_going_to_woman'
			},
			{
 				'trigger': 'advance',
				'source': 'woman',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
 				'trigger': 'advance',
				'source': 'man',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
 				'trigger': 'advance',
				'source': 'game',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
 				'trigger': 'advance',
				'source': 'exercise',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
 				'trigger': 'advance',
				'source': 'drinking',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
 				'trigger': 'advance',
				'source': 'meal',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
 				'trigger': 'advance',
				'source': 'dessert',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
 				'trigger': 'advance',
				'source': '8hr',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
 				'trigger': 'advance',
				'source': '12hr',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
 				'trigger': 'advance',
				'source': '24hr',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
 				'trigger': 'advance',
				'source': 'talking',
				'dest': 'bye',
				'conditions': 'is_going_to_bye'
			},
			{
				'trigger': 'go_back',
				'source': [
					'bye'
				],
				'dest': 'init'
			}
		],
		initial='init',
		auto_transitions=False,
		show_conditions=True,

	)

	def is_going_to_playing(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '休閒娛樂'
		return False

	def is_going_to_eatting(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '進食'
		return False

	def is_going_to_sleeping(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '睡覺'
		return False

	def is_going_to_talking(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '聊天'
		return False

	def is_going_to_game(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '玩遊戲'
		return False

	def is_going_to_music(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '聽音樂'
		return False

	def is_going_to_exercise(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '運動'
		return False

	def is_going_to_drinking(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '喝飲料'
		return False

	def is_going_to_meal(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '吃正餐'
		return False

	def is_going_to_dessert(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '吃零食/甜點'
		return False

	def is_going_to_8hr(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '8小時'
		return False

	def is_going_to_12hr(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '12小時'
		return False

	def is_going_to_24hr(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '24小時'
		return False

	def is_going_to_woman(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '女歌手'
		return False

	def is_going_to_man(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '男歌手'
		return False
		
	def is_going_to_bye(self, event):
		if event.get("message"):
			text = event['message']['text']
			return text == '好 拜拜~'
		return False

	def on_enter_playing(self, event):
		print("I'm entering playing")

		sender_id = event['sender']['id']
		quick_replies = [QuickReply(title="聽音樂", payload="PICK_MUSIC"), QuickReply(title="玩遊戲", payload="PICK_GAME"), QuickReply(title="運動", payload="PICK_EXERCISE")]

		page.send(sender_id, "你對哪一項比較有興趣呢~",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")


	def on_exit_playing(self, event):
		print('Leaving playing')

	def on_enter_eatting(self, event):
		print("I'm entering eatting")

		sender_id = event['sender']['id']
		quick_replies = [QuickReply(title="喝飲料", payload="PICK_DRINK"), QuickReply(title="吃正餐", payload="PICK_MEAL"), QuickReply(title="吃零食/甜點", payload="PICK_DESSERT")]

		page.send(sender_id, "你對哪一項比較有興趣呢~",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")


	def on_exit_eatting(self, event):
		print('Leaving eatting')

	def on_enter_sleeping(self, event):
		print("I'm entering sleeping")

		sender_id = event['sender']['id']
		quick_replies = [QuickReply(title="8小時", payload="PICK_8"), QuickReply(title="12小時", payload="PICK_12"), QuickReply(title="24小時", payload="PICK_24")]

		page.send(sender_id, "那你想要睡多久呢><",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")



	def on_exit_sleeping(self, event):
		print('Leaving sleeping')

	def on_enter_talking(self, event):
		print("I'm entering talking")

		sender_id = event['sender']['id']
		page.send(sender_id, Attachment.Image("https://i.imgur.com/EdQYTpW.png"))
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, "希望你有朋友跟你聊天><\n拜拜~",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")

	def on_exit_talking(self, event):
		print('Leaving talking')


	def on_enter_game(self, event):
		print("I'm entering game")

		sender_id = event['sender']['id']
		page.send(sender_id, Attachment.Image("https://i.imgur.com/KqnRW1R.png"))
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, "要小心變臭宅宅哦><\n(但可以找我一起玩！)",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")

	def on_exit_game(self, event):
		print('Leaving game')

	def on_enter_music(self, event):
		print("I'm entering music")

		sender_id = event['sender']['id']
		quick_replies = [QuickReply(title="男歌手", payload="PICK_man"), QuickReply(title="女歌手", payload="PICK_woman")]

		page.send(sender_id, "那你想聽男歌手的歌還是女歌手的呢~",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")



	def on_exit_music(self, event):
		print('Leaving music')

	def on_enter_exercise(self, event):
		print("I'm entering exercise")

		sender_id = event['sender']['id']
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, "多運動身體好<3",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")


	def on_exit_exercise(self, event):
		print('Leaving exercise')

	def on_enter_drinking(self, event):
		print("I'm entering drinking")

		sender_id = event['sender']['id']
		page.send(sender_id, Attachment.Image("https://i.imgur.com/JKvLLSq.png"))
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, "小心胖死><\n不要再喝了~",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")



	def on_exit_drinking(self, event):
		print('Leaving drinking')

	def on_enter_meal(self, event):
		print("I'm entering meal")

		sender_id = event['sender']['id']
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, "你真是個準時吃飯的好孩子~",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")


	def on_exit_meal(self, event):
		print('Leaving meal')

	def on_enter_dessert(self, event):
		print("I'm entering dessert")

		sender_id = event['sender']['id']
		page.send(sender_id, Attachment.Image("https://i.imgur.com/JKvLLSq.png"))
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, "小心胖死><\n不要再吃了~",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")

	def on_exit_dessert(self, event):
		print('Leaving dessert')

	def on_enter_8hr(self, event):
		print("I'm entering 8hr")

		sender_id = event['sender']['id']
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, "睡眠充足~\n給你100分<3",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")

	def on_exit_8hr(self, event):
		print('Leaving 8hr')
	
	def on_enter_12hr(self, event):
		print("I'm entering 12hr")

		sender_id = event['sender']['id']
		page.send(sender_id, Attachment.Image("https://i.imgur.com/WfO1GfO.png"))
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, "你還有很多作業跟考試><\n你要被當了QQ",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")


	def on_exit_12hr(self, event):
		print('Leaving 12hr')

	def on_enter_24hr(self, event):
		print("I'm entering 24hr")

		sender_id = event['sender']['id']
		page.send(sender_id, Attachment.Image("https://i.imgur.com/DQMhbLG.png"))
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, "......希望你還有起床的一天><",quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")

	def on_exit_24hr(self, event):
		print('Leaving 24hr')

	def on_enter_man(self, event):
		print("I'm entering man")
		sender_id = event['sender']['id']
		responses = ["atGbcYTjZCY", "KEgOrgcLu0s", "Dnj5Tcpev0Q", "s-CcFyyPJiY", "wFqUAw_NYvs"]
		page.send(sender_id, Template.Generic([
			Template.GenericElement(" ",
							subtitle ="  ",
							item_url = "https://www.youtube.com/watch?v=" + random.choice(responses),
							image_url = "https://img.youtube.com/vi/" + random.choice(responses) + "/hqdefault.jpg",
							buttons = [
								Template.ButtonWeb("Open Web URL", "https://www.youtube.com/watch?v=" + random.choice(responses)),
								Template.ButtonPostBack("好 拜拜~", "DEVELOPED_DEFINED_PAYLOAD")
							])
		]))
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, "隨機推薦你一位男歌手的歌囉~" ,quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")

	def on_exit_man(self, event):
		print('Leaving man')

	def on_enter_woman(self, event):
		print("I'm entering woman")
		sender_id = event['sender']['id']
		responses = ["https://www.youtubeFB.com/watch?v=P8uJ4gFjJGE", "https://www.youtubeFB.com/watch?v=3mEeKAdXAo4", "https://www.youtubeFB.com/watch?v=ma7r2HGqwXs", "https://www.youtubeFB.com/watch?v=VGHLqi_mxnk", "https://www.youtubeFB.com/watch?v=NYYuVnjg0SQ", "https://www.youtubeFB.com/watch?v=FqrzCxSWaZY", "https://www.youtubeFB.com/watch?v=k8jAqe9QZ7I", "https://www.youtubeFB.com/watch?v=BRcudpJzy1I"]
		page.send(sender_id, "隨機推薦你一位女歌手的歌囉~")
		quick_replies = [QuickReply(title="好 拜拜~", payload="PICK_bye")]
		page.send(sender_id, random.choice(responses),quick_replies=quick_replies,metadata="DEVELOPER_DEFINED_METADATA")

	def on_exit_woman(self, event):
		print('Leaving woman')
		
	def on_enter_bye(self, event):
		print("I'm entering bye")
		self.go_back()

	def on_exit_bye(self):
		print('Leaving bye')
