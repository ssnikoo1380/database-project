import model
import view


class Login:
    usermodel = model.user()
    messagemodel = model.message()
    is_loggedin = False

    def __init__(self, show_in_login):
        show_in_login.prompt("has account")
        has_account = True if input().lower() == "y" else False
        if has_account:
            # login
            while True:
                show_in_login.prompt("get id")
                login_id = input()
                if not self.user_id_exists(login_id):
                    show_in_login.prompt("no user")
                    continue
                break
            while True:
                show_in_login.prompt("get pass")
                login_pass = input()
                if not self.password_is_correct(login_id, login_pass):
                    show_in_login.prompt("wrong pass")
                    continue
                break
            self.is_loggedin = True
            show_in_login.prompt("login success")
        else:
            # sign up
            while True:
                show_in_login.prompt("get id")
                signup_id = input()
                if self.user_id_exists(signup_id):
                    show_in_login.prompt("duplicate id")
                    continue
                show_in_login.prompt("get pass")
                signup_pass = input()
                show_in_login.prompt("set name")
                signup_username = input()
                break
            if self.user_created([signup_id, signup_pass, signup_username]):
                self.is_loggedin = True
                show_in_login.prompt("signup success")
            else:
                show_in_login.prompt("signup failed")

    # checking if the entered username exists in database for login
    def user_id_exists(self, user_id: str) -> bool:
        return True if self.usermodel.return_user_id(user_id) else False

    # same as username for password
    def password_is_correct(self, user_id: str, user_pass: str) -> bool:
        return True if self.usermodel.return_user_pass(user_id, user_pass) else False

    def user_created(self, information):
        return True if self.usermodel.create_user(information) else False


class Chatlist:
    def __init__(self, show_in_chatlist):
        show_in_chatlist.prompt("")
        selected_option = input()
        if selected_option == "1":
            show_in_chatlist.prompt("new")
        elif selected_option == "2":
            show_in_chatlist.prompt("delete")
        elif selected_option == "3":
            loginview = view.Login()
            Login(loginview)
        else:
            show_in_chatlist.prompt("invalid option")


# loginview = view.Login()
# userlogin = Login(loginview) #commented for skipping login remember to uncomment
# if userlogin.is_loggedin:
chatlistview = view.Chatlist()
Chatlist(chatlistview)
