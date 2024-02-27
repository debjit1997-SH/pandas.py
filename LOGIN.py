class User:
    name=" "
    email= " "
    password= " "
    login = False

    def login (self):
        email = input("Enter email :-")
        password = input("Enter Password :-")

        if email == self.email and password == self.password:
            login = True
            print("login Succesfull")
        else:
            print("login Failed")
    def logout(self):
        login = False
        print("Logged out")
    def isloggedin(self):
        if self.login:
            return True
        else:
            return False
    def profile(self):
        if self.isLoggedIn():
            print(self.name,"\n",self.email)
        else:
            print("User is not Logged in")

User1 = User()
User1.name="Debjit"
User1.email="debjitdey1997@gmail.com"
User1.password="1997"

User1.login()
