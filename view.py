class Login:
    # shows the needed prompts in login section
    def prompt(self, to_show: str):
        if to_show == "has account":
            print("Do You Have An Account? Y/N")
        elif to_show == "get id":
            print("ID: ")
        elif to_show == "no user":
            print("Username Not Found!")
        elif to_show == "get pass":
            print("Password: ")
        elif to_show == "wrong pass":
            print("Wrong Password!")
        elif to_show == "login success":
            print("Login Successful!")
        elif to_show == "set name":
            print("Username: ")
        elif to_show == "duplicate id":
            print("Someone Has This ID!")
        elif to_show == "signup success":
            print("Your Account Has Been Created. You Are Logged In, Enjoy!")
        elif to_show == "signup failed":
            print("Sign Up Failed!")


class Chatlist:
    chatlist = []

    def prompt(self, to_show: str):
        if to_show == "":
            print("Options: \n")
            print("1.Add a New Chat")
            print("2.Delete a Chat")
            print("3.Show Current Chats")
            print("4.Logout")
        if to_show == "new":
            print("Enter The Name(s) Of The Person(s) You Want To Message: ")
        elif to_show == "no user":
            print("User Not Found!")
        elif to_show == "ask make new":
            print("1.Make A New Chat?")
        elif to_show == "ask menu":
            print("2.Return To Menu")
        elif to_show == "not sent":
            print("Unable To Send Message!")
        elif to_show == "delete":
            print("Enter The Name(s) Of The Chat(s) You Want To Delete: ")
        elif to_show == "delete success":
            print("Selected Chat(s) Deleted Successfully!")
        elif to_show == "delete fail":
            print("Unable To Delete!")
        elif to_show == "current":
            for chat in self.chatlist:
                print(chat, "\n")
        elif to_show == "invalid option":
            print("Please Choose a Valid Option")
