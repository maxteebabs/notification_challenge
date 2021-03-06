from notifications.abstractions.Notification import Notification
from models.User import User
from models.Group import UserGroup, Group
from models.Notification import Notification, TYPE, CHANNEL

class PushNotificationService(Notification):
    def notifyUser(self, message, customer: User):
        """overrides the Notification abstract class method"""
        status = self.service.send(message, customer.mobile)
        self.type = TYPE.SINGLE
        # we need to save to database
        self.saveNotificationToDB(message, customer.id, status)
        return status
    
    def notifyGroup(self, message, group: Group):
        """overrides the Notification abstract class method"""
        # get the users in the group
        group_users = UserGroup.query.filter_by(group_id = group.id).all()

        for group_user in group_users:
            try:
                status = self.service.send(message, group_user.user.mobile)
                self.type = TYPE.GROUP
                # we need to save to database
                self.saveNotificationToDB(message, group_user.user.id, status)
            except Exception as e:
                current_app.logger.info("SMSNotification Error:: %s", str(e))
            
        return status

    def saveNotificationToDB(self,message, user_id, status):
        notification = Notification()
        notification.type = self.type
        notification.channel = self.channel
        notification.group_name = self.group_name
        notification.user_id = user_id
        notification.message = message
        notification.status = 'sent' if status else 'failed'
        notification.save()
