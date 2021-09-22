import jimi

class _mailTM(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("mailTMConnect","_mailTMConnect","_action","plugins.mailTM.models.action")
        jimi.model.registerModel("mailTMGetAccount","_mailTMGetAccount","_action","plugins.mailTM.models.action")
        jimi.model.registerModel("mailTMDeleteAccount","_mailTMDeleteAccount","_action","plugins.mailTM.models.action")
        jimi.model.registerModel("mailTMGetMessages","_mailTMGetMessages","_action","plugins.mailTM.models.action")
        jimi.model.registerModel("mailTMGetMessage","_mailTMGetMessage","_action","plugins.mailTM.models.action")
        jimi.model.registerModel("mailTMDeleteMessage","_mailTMDeleteMessage","_action","plugins.mailTM.models.action")
        jimi.model.registerModel("mailTMReadMessage","_mailTMReadMessage","_action","plugins.mailTM.models.action")
        jimi.model.registerModel("mailTMWaitForMessages","_mailTMWaitForMessages","_action","plugins.mailTM.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("mailTMConnect","_mailTMConnect","_action","plugins.mailTM.models.action")
        jimi.model.deregisterModel("mailTMGetAccount","_mailTMGetAccount","_action","plugins.mailTM.models.action")
        jimi.model.deregisterModel("mailTMDeleteAccount","_mailTMDeleteAccount","_action","plugins.mailTM.models.action")
        jimi.model.deregisterModel("mailTMGetMessages","_mailTMGetMessages","_action","plugins.mailTM.models.action")
        jimi.model.deregisterModel("mailTMGetMessage","_mailTMGetMessage","_action","plugins.mailTM.models.action")
        jimi.model.deregisterModel("mailTMDeleteMessage","_mailTMDeleteMessage","_action","plugins.mailTM.models.action")
        jimi.model.deregisterModel("mailTMReadMessage","_mailTMReadMessage","_action","plugins.mailTM.models.action")
        jimi.model.deregisterModel("mailTMWaitForMessages","_mailTMWaitForMessages","_action","plugins.mailTM.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        #if self.version < 0.2:
        return True
