class GUI:
    loginCredentials = []

    @classmethod
    def showMainWindow(cls):
        print("**********************************************************************")
        print("**********************************************************************")
        print("***************** WELCOME TO ONLINE SHOPPING CENTER ******************")
        print("**********************************************************************")
        print("**********************************************************************")
    
    @classmethod
    def displayEmptyLines(cls, numLine=1):
        for i in range(numLine):
            print("                                                ")
    
    @classmethod
    def showLoginWindow(cls):
        
        print("############################ Login ###################################")
        username = input("Enter username :")
        password= input("Enter password :")
        cls.loginCredentials.append({
            "username" : username,
            "password" : password
        })
        print("######################################################################")

        
    