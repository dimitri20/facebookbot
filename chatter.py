from fbchat import *
from fbchat.models import Message
import PySimpleGUI as sg


sg.theme('DarkAmber')

layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] 

        	]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()


"""
username = "dito.gulua@mail.ru"
password = "ZolokosTi!04"

client = Client(username, password)


while True:
	friends = []
	user = input("Enter username:  ")
	if user == 'exit':
		break
	print("Searching...")
	
	for human in client.searchForUsers(user):
		if human.is_friend:
			friends.append(human)
	print(f"found {len(friends)} friend")	
	for friend in friends:
		print(f"{friend.name}  --  {friend.uid} \n")

	# print(client.searchForUsers(user)[0].name, 'uid = ', client.searchForUsers(user)[0].uid)

client.logout()


"""
