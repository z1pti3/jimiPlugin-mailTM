import jimi

from plugins.mailTM.includes import mailTM

class _mailTMConnect(jimi.action._action):
    username = str()
    password = str()

    def doAction(self,data):
        username = jimi.helpers.evalString(self.username,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        password = jimi.helpers.evalString(self.password,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })

        mail = mailTM._mailTM(username,password) 
        if mail:
            data["persistentData"]["mailTM"] = mail
            return { "result" : True, "rc" : 200  }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to create mailTM class object" }

class _mailTMGetAccount(jimi.action._action):

    def doAction(self,data):
        try:
            mail = data["persistentData"]["mailTM"]
            return { "result" : True, "rc" : 200, "data" : mail.getAccount() }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No mailTM class object found. Make sure you have run _mailTMConnect before this object." }

class _mailTMDeleteAccount(jimi.action._action):

    def doAction(self,data):
        try:
            mail = data["persistentData"]["mailTM"]
            return { "result" : True, "rc" : 200, "data" : mail.deleteAccount() }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No mailTM class object found. Make sure you have run _mailTMConnect before this object." }


class _mailTMGetMessages(jimi.action._action):

    def doAction(self,data):
        try:
            mail = data["persistentData"]["mailTM"]
            return { "result" : True, "rc" : 200, "messages" : mail.getMessages() }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No mailTM class object found. Make sure you have run _mailTMConnect before this object." }

class _mailTMGetMessage(jimi.action._action):
    message_id = str()

    def doAction(self,data):
        try:
            message_id = jimi.helpers.evalString(self.message_id,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
            mail = data["persistentData"]["mailTM"]
            return { "result" : True, "rc" : 200, "messages" : mail.getMessage(message_id) }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No mailTM class object found. Make sure you have run _mailTMConnect before this object." }

class _mailTMDeleteMessage(jimi.action._action):
    message_id = str()

    def doAction(self,data):
        try:
            message_id = jimi.helpers.evalString(self.message_id,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
            mail = data["persistentData"]["mailTM"]
            return { "result" : True, "rc" : 200, "messages" : mail.deleteMessage(message_id) }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No mailTM class object found. Make sure you have run _mailTMConnect before this object." }

class _mailTMReadMessage(jimi.action._action):
    message_id = str()

    def doAction(self,data):
        try:
            message_id = jimi.helpers.evalString(self.message_id,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
            mail = data["persistentData"]["mailTM"]
            return { "result" : True, "rc" : 200, "messages" : mail.readMessage(message_id) }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No mailTM class object found. Make sure you have run _mailTMConnect before this object." }

class _mailTMWaitForMessages(jimi.action._action):
    timeout = int()

    def doAction(self,data):
        try:
            mail = data["persistentData"]["mailTM"]
            return { "result" : True, "rc" : 200, "messages" : mail.waitForNewMessage(self.timeout) }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No mailTM class object found. Make sure you have run _mailTMConnect before this object." }
