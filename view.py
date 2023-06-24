import controller
import model


class Login:
    def __init__(self):
        has_account = input("Do You Have An Account? y/n")
        if has_account.lower() == "y":
            while True:
                self.login_user_id = input("ID: ")
                if not controller.Login.user_id_exists(self.login_user_id):
                    print("Username Not Found")
                    continue
                self.login_password = hash(input("Password"))
                if not controller.Login.password_is_correct(self.login_password):
                    print("Wrong Password")
                    continue
                break
            print("Login Successful!")
        else:
            while True:
                self.user_id = input("ID: ")
                if controller.Login.user_id_exists(self.user_id):
                    print("Someone has this ID")
                    continue
                self.user_password = input("Password")
                self.user_name = input("Name: ")
                break
            print("Account Created Successfully. You're Logged In!")
