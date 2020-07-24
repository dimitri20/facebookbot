import tkinter as tk
from tkinter import *
from fbchat.models import Message
from fbchat import *

username = "dito.gulua@mail.ru"
password = "ZolokosTi!04"

client = Client(username, password)

root = tk.Tk()
root.configure(bg="white")
root.geometry("650x600")
root.resizable(False, False)


def onClickPlaceholder(event):
    userCommand.configure(state=NORMAL)
    userCommand.delete(0, END)
    userCommand.unbind('<Button-1>', on_click_id)

def onClickSearch():
	friends = []
	print("Searching...")
	
	for human in client.searchForUsers(user):
		if human.is_friend:
			friends.append(human)
	print(f"found {len(friends)} friend")	
	for friend in friends:
		print(f"{friend.name}  --  {friend.uid} \n")

	label = tk.Label(root, text=f"{friend.name}  --  {friend.uid} \n")
	label.pack()



userCommandBorder = tk.Frame(root, background = 'orange')
userCommandPadding = tk.Frame(userCommandBorder, background = 'white')

userCommand = tk.Entry(userCommandPadding, width=55, font='Arial 12', bd=0)
userCommand.insert(0, "Enter Friend name")
userCommand.configure(state=DISABLED)
on_click_id = userCommand.bind('<Button-1>', onClickPlaceholder)

userCommandPadding.pack(padx=4, pady=4)
userCommandBorder.pack(pady=60)
userCommand.pack(fill="both", expand=True, padx=12, pady=7, side=LEFT)

photo = PhotoImage(file = "next (2).png")
goToResult = tk.Button(userCommandPadding, text="Search", image=photo, width=25, height=25, command=onClickSearch, bd=0, bg='white')
goToResult.pack(side=RIGHT, padx=5)


root.mainloop()


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
