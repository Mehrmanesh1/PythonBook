import datetime
import time

class User:
    def __init__(self, firstname, lastname, birthday, email, ph_number):
        self.firstname = firstname
        self.lastname = lastname
        self.name = f"{firstname} {lastname}"
        self.birthday = datetime.date(birthday[2],birthday[0],birthday[1])
        self.email = email
        self.phonenum = ph_number
        self.name = f"{firstname} {lastname}"
        self.banned = False

    def printall(self):
        if not self.banned:
            print("--------")
            print(self.birthday)
            print(self.email)
            print(self.phonenum)
            print(self.name)
            print("--------")
        else:
            print("Account Banned")

    def greet(self, user):
        if not self.banned:
            print("--------")
            print(f"Hello, {user.firstname}")
            time.sleep(2)
            print(f"My name is {self.firstname}")
            print("--------")
        else:
            print("Account Banned")

class Admin(User):
    def ban_user(self,user):
        user.banned = True
        print(f"Banned {user.name}")
    def unban_user(self,user):
        user.banned = False
        print(f"Unbanned {user.name}")
    def add_post(self,post):
        print(post)



if __name__ == "__main__":
    amir = User("Amir","Mehr", [1,1,2000],"amir@gmail.com","18002561111")
    saeid = User("Saeid","Mehr", [1,8,2001],"saeid@gmail.com","13471563200")
    admin = Admin("John","Smith",[1,1,2000],"admin@admin.com","10000000000")

    amir.printall()

    amir.greet(saeid)

    admin.ban_user(saeid)

    saeid.greet(amir)

    admin.unban_user(saeid)

    saeid.greet(amir)

    admin.add_post("Hello Users")