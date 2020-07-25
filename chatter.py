from fbchat.models import Message
from fbchat import log, Client


# username = "dito.gulua@mail.ru"
# password = "ZolokosTi!04"

# client = Client(username, password)

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)




class Facebook():
	def __init__(self, username, password):
		self.client = Client(username, password)

	def autoReply(self):
		income = self.client.listen()
		author = income.author
		if onMessage():
			self.client.send(Message(text=income.text), thread_id=author)


	def findFriend(self, name):
		friends = []
		for human in self.client.searchForUsers(name):
			if human.is_friend:
				friends.append({
					"username" : human.name,
					"uid" : human.uid,
					"photo" : human.photo
					})
		
		return friends

	def sendMessage(self):
		self.client.send(Message(text="Hi me!"), thread_id=client.uid, thread_type=ThreadType.USER)


	def logout(self):
		self.client.logout()


def main():
	a = Facebook("dito.gulua@mail.ru", "ZolokosTi!04")
	a.autoReply()
	

if __name__ == '__main__':
	client = EchoBot("dito.gulua@mail.ru", "ZolokosTi!04")
	client.listen()


