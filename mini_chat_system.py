#message class
class message:
    message_count = 1
    def __init__(self,sender,content):
        self.sender = sender
        self.content = content
        self.id = message.message_count
        message.message_count += 1

    def __str__(self):
        return f"{self.id} {self.sender.username}:{self.content}"
#user class
class user:
    def __init__(self,username):
        self.username = username
        self.chatroom = None
    def join_chatroom(self,chatroom):
        if self.chatroom:
           print(f"{self.username} is present in chatroom")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} has join {chatroom.name}")
    def leave_chatroom(self):
        if not self.chatroom:
           print(f"{self.username} is not in any chatroom")
        else:
           self.chatroom.remove_user(self)
           print(f"{self.username} leave the chatroom")
           self.chatroom = None
    def send_message(self,content):
        if not self.chatroom:
           print(f"{self.username} is not send message(it not present in any chatroom)")
        else:
            self.chatroom.broadcast(self,content)
#chatroom
#a chatroom called Python Group.
#This chatroom needs to do three things:
#1. Keep a list of users.
#2. Keep a list of messages.
#3. Allow users to send messages.
class chatroom:
    def __init__(self,name):
        self.name = name
        self.user = []
        self.message = []
    def add_user(self,user):
       self.user.append(user) 
    def remove_user(self,user):
       self.user.remove(user)

    def broadcast(self,sender,content):
       mess = message(sender,content)
       self.message.append(mess)
       print(mess)
    def chat_history(self):
        print(f"\nChat History of {self.name}:")
        for mess in self.message:
            print(mess)
            print()
# Example Usage

if __name__ == "__main__":
   room = chatroom("Python Lounge")


u1 = user("priyanshu")
u2 = user("priya")
u3 = user("piyush")

u1.join_chatroom(room)
u2.join_chatroom(room)
u3.join_chatroom(room)

u1.send_message("hello everyone")
u2.send_message("hy i am priya ")

u3.join_chatroom(room)
u3.send_message("what up guys")
room.chat_history()

u1.leave_chatroom()
u2.leave_chatroom()
u3.leave_chatroom()


















