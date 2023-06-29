import model
import view


class Login:

    is_loggedin = False
    login_id = None
    login_pass = None

    def __init__(self, show_in_login):
        show_in_login.prompt("has account")
        has_account = True if input().lower() == "y" else False
        if has_account:
            # login
            while True:
                show_in_login.prompt("get id")
                self.login_id = input()
                if not self.user_id_exists(self.login_id):
                    show_in_login.prompt("no user")
                    continue
                break
            while True:
                show_in_login.prompt("get pass")
                login_pass = input()
                if not self.password_is_correct(self.login_id, login_pass):
                    show_in_login.prompt("wrong pass")
                    continue
                break
            self.is_loggedin = True
            show_in_login.prompt("login success")
        else:
            # sign up
            while True:
                show_in_login.prompt("get id")
                self.login_id = input()
                if self.user_id_exists(self.login_id):
                    show_in_login.prompt("duplicate id")
                    continue
                show_in_login.prompt("get pass")
                signup_pass = input()
                show_in_login.prompt("set name")
                signup_username = input()
                break
            if self.user_created([self.login_id, signup_pass, signup_username]):
                self.is_loggedin = True
                show_in_login.prompt("signup success")
            else:
                show_in_login.prompt("signup failed")

    # checking if the entered username exists in database for login
    def user_id_exists(self, user_id: str) -> bool:
        return True if usermodel.return_user_id(user_id) else False

    # same as username for password
    def password_is_correct(self, user_id: str, user_pass: str) -> bool:
        return True if usermodel.return_user_pass(user_id)[0][0] == user_pass else False

    def user_created(self, information):
        return True if usermodel.create_user(information) else False

    def return_user_id(self):
        return self.login_id


class Chatlist:
    to_chat = None

    def __init__(self, show_in_chatlist):
        self.show_in_chatlist = show_in_chatlist
        while True:
            if not usermodel.is_admin(userlogin.return_user_id()):
                show_in_chatlist.prompt(0)
            else:
                show_in_chatlist.prompt(1)
            selected_option = input()
            if selected_option == "1":
                self.to_chat = self.make_chat()
                if not self.to_chat:
                    self.show_in_chatlist.prompt("ask make new")
                    self.show_in_chatlist.prompt("ask menu")
                    selected_option = input()
                    if selected_option == "1":
                        self.make_chat()
                    else:
                        continue
                else:
                    break
            elif selected_option == "2":
                self.delete_chat()
            elif selected_option == "3":
                chatlist = self.chatlist()
                if chatlist:
                    show_in_chatlist.setchatlist(chatlist)
                    while True:
                        show_in_chatlist.prompt("choose chat")
                        show_in_chatlist.prompt("chatlist")
                        self.to_chat = input()
                        if self.to_chat in chatlist:
                            break  # a code that take the user to chat with selected user
                        else:
                            show_in_chatlist.prompt("no user")
                        break
                else:
                    show_in_chatlist.prompt("empty chatlist")
                    makechat = input()
                    if makechat.lower() == "y":
                        self.make_chat()
                    else:
                        continue
                break
            elif selected_option == "4":
                self.create_message_list(messagemodel.message_list())
            elif selected_option == "5":
                loginview = view.Login()
                Login(loginview)
                break
            else:
                show_in_chatlist.prompt("invalid option")

    def send_message(self, receiver, message):
        try:
            sender = userlogin.return_user_id()
            messagemodel.send_message(sender, receiver, message)
        except Exception:
            return False
        return True

    def make_chat(self):
        while True:
            self.show_in_chatlist.prompt("new")
            receiver_names = input()
            if not usermodel.return_user_id(receiver_names):
                self.show_in_chatlist.prompt("no user")
                return False
            elif not self.send_message(receiver_names, ""):
                self.show_in_chatlist.prompt("not sent")
                return False
            else:
                return receiver_names

    def delete_chat(self):
        while True:
            self.show_in_chatlist.prompt("delete")
            to_delete = input()
            sender = userlogin.return_user_id()
            if messagemodel.chat_exists(to_delete, sender):
                if messagemodel.delete_chat(to_delete, sender):
                    self.show_in_chatlist.prompt("delete success")
                    break
                else:
                    self.show_in_chatlist.prompt("delete fail")
            else:
                self.show_in_chatlist.prompt("no user")

    def chatlist(self):
        self.show_in_chatlist.prompt("current")
        receiver_names = messagemodel.return_chatlist(userlogin.login_id)
        chatlist = []
        for name in receiver_names:
            if name[0] not in chatlist:
                chatlist.append(name[0])
        chatlist.sort()
        return chatlist

    def create_message_list(self, messagelist):
        for message in messagelist:
            msg_id = message[0]
            sender = message[5]
            receiver = message[2]
            senddate = message[4]
            seen_status = True if message[3] else False
            text = message[1]
            chatlistview.message_list = [
                msg_id, sender, receiver, text, seen_status, senddate]
            self.show_in_chatlist.prompt("message list")


class Chatroom:
    def __init__(self, show_in_chat, to_chat):
        my_id = userlogin.return_user_id()
        chat = messagemodel.return_chat(my_id, to_chat)
        if chat:
            for message in chat:
                if message[1] == my_id:
                    show_in_chat.message = message[0]
                    show_in_chat.prompt("my messages")
                else:
                    show_in_chat.message = message[0]
                    show_in_chat.receiver = to_chat
                    show_in_chat.prompt("their messages")
            messagemodel.seen(my_id, to_chat)
            while True:
                show_in_chat.prompt("get message")
                mymessage = input()
                messagemodel.send_message(my_id, to_chat, mymessage)
        else:
            show_in_chat.prompt("chat empty")
            while True:
                show_in_chat.prompt("get message")
                mymessage = input()
                messagemodel.send_message(my_id, to_chat, mymessage)


loginview = view.Login()
messagemodel = model.Message()
usermodel = model.User()
userlogin = Login(loginview)
if userlogin.is_loggedin:
    chatlistview = view.Chatlist()
    chatlist = Chatlist(chatlistview)
    to_chat = chatlist.to_chat
    if to_chat:
        chatroomview = view.Chatroom()
        chatroom = Chatroom(chatroomview, to_chat)
