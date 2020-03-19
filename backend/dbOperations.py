import dbConnect
import json

userInfo = dbConnect.database.userInfo

def insertUser(userId, formData):
    formData['_id'] = userId
    if((checkExistingUser(formData['email'])) == 1):
        userInfo.insert_one(formData)
        message = "New User Created"
    else:
        message = "User already exists"
    return {'alert': message}

def checkExistingUser(email):
    dbEmail = userInfo.find_one({'email': email}, {'email': 1, '_id': 0})
    # print("Inside checkExistingUser() --> ")
    # print("Email Parameter --> ", email)
    # print("dbEmail MongoDB --> ", dbEmail['email'])
    if(dbEmail['email'] == email):
        return 1
    else:
        return 0

def validateLogin(loginData):
    username = loginData['username']
    password = loginData['password']
    # print("Inside validatLogin() --> ")
    # print(username, "-->", password )
    if((checkExistingUser(username) != 1)):
        # exist = checkExistingUser(username)
        # print("Return value from checkExistingUser() --> ", exist)
        message = "User does not exist"
    else:
        dbPwd = userInfo.find_one({'email': username}, {'password': 1, '_id':0})
        if(dbPwd['password'] == password):
            message = "User successfully Logged In.!!"
        else:
            message = "Incorrect Password.!!"
    return {'alert': message}