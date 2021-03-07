from flask import jsonify, request
from models.Notification import Notification
from models.User import User, TYPE
from models.Group import Group
from notifications.services.SMSNotification import SMSNotification
from notifications.services.PushNotification import PushNotification
from notifications.services.EmailNotification import EmailNotification

class NotificationController:
    def get(self):
        notifications = Notification.query.order_by(
            Notification.created_at.desc()).all()
        return jsonify({
            'status': True,
            'notifications': [n.format() for n in notifications]
        }), 200

    def getNotificationByUser(self, user_id):
        try:
            if not user_id:
                raise ValueError("Invalid Request")
            notifications = Notification.query.filter_by(
                user_id = user_id
            ).order_by(
                Notification.created_at.desc()).all()
            return jsonify({
                'status': True,
                'notifications': [n.format() for n in notifications]
            }), 200
        except ValueError as e:
            return jsonify({
                'status': False,
                'message': str(e)
            })

    def send(self):
        """responsible for sending out notifications to a single user"""
        try:
            post_data = request.get_json()
            message = post_data.get("message", None)
            user_id = post_data.get("customer_id", None)

            shouldSendSMS = post_data.get("should_send_sms", False)
            shouldSendPushNotification = post_data.get("should_send_push_notification", False)
            shouldSendEmail = post_data.get("should_send_email", False)

            if not message:
                raise ValueError("Message field is required")
            if not user_id:
                raise ValueError("customer_id field is required")

            # query for a user
            user = User.query.filter_by(
                type= TYPE.CUSTOMER).filter_by(id=user_id).first()
            if not user:
                raise ValueError("Customer not found")

            if shouldSendSMS:
                service = SMSNotification()
                service.notifyUser(message, user)
            if shouldSendPushNotification:
                service = PushNotification()
                service.notifyUser(message, user)
            if shouldSendEmail:
                service = EmailNotification()
                service.notifyUser(message, user)

            return jsonify({
                'status': True,
                'message': "sent", 
                'translated_text': message
            }), 200
        except ValueError as e:
            return jsonify({
                'status': False,
                'message': str(e)
            }), 400
        except Exception as e:
            print(str(e))
            return jsonify({
                'status': False,
                'message': "Failed to send notification"
            }), 400
    
    def sendToGroup(self):
        """responsible for sending out notifications to a group of users"""
        try:
            post_data = request.get_json()
            message = post_data.get("message", None)
            group_id = post_data.get("group_id", None)

            shouldSendSMS = post_data.get("should_send_sms", False)
            shouldSendPushNotification = post_data.get("should_send_push_notification", False)
            shouldSendEmail = post_data.get("should_send_email", False)

            if not message:
                raise ValueError("message field is required")
            if not group_id:
                raise ValueError("group_id field is required")

            group = Group.query.get(group_id)
            if not group:
                raise ValueError("Group not found")

            if shouldSendSMS:
                service = SMSNotification()
                service.notifyGroup(message, group)
            if shouldSendPushNotification:
                service = PushNotificationService()
                service.notifyGroup(message, group)
            if shouldSendEmail:
                service = EmailNotification()
                service.notifyGroup(message, group)

            return jsonify({
                'status': True,
                'message': "sent"
            }), 200
        except ValueError as e:
            return jsonify({
                'status': False,
                'message': str(e)
            }), 400
        except Exception as e:
            print(str(e))
            return jsonify({
                'status': False,
                'message': "Failed to send notification"
            }), 400

    def notifyRiders(self):
        """responsible for sending out notifications to a single rider"""
        try:
            post_data = request.get_json()
            message = post_data.get("message", None)
            user_id = post_data.get("user_id", None)

            shouldSendSMS = post_data.get("should_send_sms", False)
            shouldSendPushNotification = post_data.get("should_send_push_notification", False)
            shouldSendEmail = post_data.get("should_send_email", False)

            if not message:
                raise ValueError("Message field is required")
            if not user_id:
                raise ValueError("user_id field is required")

            rider = User.query.filter_by(
                type= TYPE.RIDER).filter_by(id=user_id).first()
            if not rider:
                raise ValueError("Rider not found")
            
            if shouldSendSMS:
                service = SMSNotification()
                service.notifyUser(message, rider)
            if shouldSendPushNotification:
                service = PushNotificationService()
                service.notifyUser(message, rider)
            if shouldSendEmail:
                service = EmailNotification()
                service.notifyUser(message, rider)

            return jsonify({
                'status': True,
                'message': "sent"
            }), 200
        except ValueError as e:
            return jsonify({
                'status': False,
                'message': str(e)
            }), 400
        except Exception as e:
            print(str(e))
            return jsonify({
                'status': False,
                'message': "Failed to rider notification"
            }), 400