

class Login:
    def prompt(self, to_show: str):  # shows the needed prompts in login section
        if to_show == "has account":
            print("Do You Have An Account? Y/N \n")
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
