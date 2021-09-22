import requests
import json
import string
import random
import time
from pathlib import Path

class _mailTM():
    apiAddress = "https://api.mail.tm/"

    def __init__(self, username=None, password=None, ca=None, requestTimeout=15):
        self.token = None
        self.requestTimeout = requestTimeout
        if ca != None:
            if type(ca) is str:
                self.ca = str(Path(ca))
            elif type(ca) is bool:
                self.ca = ca
        else:
            self.ca = None
        if username or password:
            self.username = username
            self.password = password
            self.token = self.login(username,password)
        else:
            self.token = self.createAccount()

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        kwargs["headers"] = {
            "accept": "application/ld+json",
            "Content-Type": "application/json"
        }
        if self.token:
            kwargs["headers"]["Authorization"] = "Bearer {0}".format(self.token)
        if self.ca != None:
            kwargs["verify"] = self.ca
        if data:
            kwargs["data"] = json.dumps(data)
        try:
            url = "{0}{1}".format(self.apiAddress,endpoint)
            if methord == "GET":
                response = requests.get(url, **kwargs)
            elif methord == "POST":
                response = requests.post(url, **kwargs)
            elif methord == "DELETE":
                response = requests.delete(url, **kwargs)
            elif methord == "PATCH":
                response = requests.patch(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            return 0, "Connection Timeout - {0}".format(e)
        if response.text:
            return response.status_code, json.loads(response.text)
        return response.status_code, "No response"

    def getSupportedDomains(self):
        statusCode, response = self.apiCall("domains")
        domains = list(map(lambda x: x["domain"], response["hydra:member"]))
        return domains

    def createAccount(self):
        username = "{0}@{1}".format(generateUsername(),self.getSupportedDomains()[0])
        password = generateWeakPassword()
        statusCode, response = self.apiCall("accounts",methord="POST",data={ "address" : username, "password" : password })
        self.id = response["id"]
        self.username = username
        self.password = password
        self.token = self.login(username,password)
        return True

    def login(self,username,password):
        statusCode, response = self.apiCall("token",methord="POST",data={ "address" : username, "password" : password })
        self.id = response["id"]
        return response["token"]

    def getAccount(self):
        statusCode, response = self.apiCall("accounts/{0}".format(self.id))
        return response

    def deleteAccount(self):
        statusCode, response = self.apiCall("accounts/{0}".format(self.id),methord="DELETE")
        return response

    def getMessages(self):
        statusCode, response = self.apiCall("messages")
        return response

    def getMessage(self,message_id):
        statusCode, response = self.apiCall("messages/{0}".format(message_id))
        return response

    def deleteMessage(self,message_id):
        statusCode, response = self.apiCall("messages/{0}".format(message_id),methord="DELETE")
        return response

    def readMessage(self,message_id):
        statusCode, response = self.apiCall("messages/{0}".format(message_id),methord="PATCH",data={ "seen" : True })
        return response

    def waitForNewMessage(self,timeout=30):
        CurrentMessages = self.getMessages()["hydra:totalItems"]
        CurrentMessages2 = CurrentMessages
        now = time.time()
        while CurrentMessages == CurrentMessages2 or time.time() > now + timeout:
            CurrentMessages2 = self.getMessages()["hydra:totalItems"]
            time.sleep(1)
        if CurrentMessages != CurrentMessages2:
            return True
        return False

def generateUsername():
    random_string = ''
    for _ in range(16):
        random_integer = random.randint(97, 122)
        random_string += (chr(random_integer))
    return random_string

def generateWeakPassword(length=16):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(length))
