import random
import dbOperations
    
def genUserId(name):
    num = str(random.randint(1,1000000))
    userId = name[:2] + num[2:6]
    return userId

def createUser(formData):
    if(len(formData['name'])<=3 or len(formData['password'])<8):
        return {"alert": "Invalid User Data"}
    else:
        userId = genUserId(formData['name'])
        return dbOperations.insertUser(userId, formData)

def loginUser(loginData):
    return dbOperations.validateLogin(loginData)