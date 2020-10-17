class Account:
    def __init__(self, firstName="", lastName="", email="", username="", password=""):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.passsword = password
    
    def login(self):
        import json
        #check database to see if the user credentials are valid
        #open UsersList.json database
        userList = open("Database/UsersList.json")
        users = json.load(userList)

        for user in users['users']:
            if user["username"] == self.username and user["password"] == self.password:
                self.firstName = user["firstName"]
                self.lastName = user["lastName"]
                self.email = user["email"]
                return True
            else:
                return False
        
        userList.close()

    
    def logout(self):
        print("Logout method")
    