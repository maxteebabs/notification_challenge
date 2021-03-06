from flask import Blueprint
from notifications.NotificationController import NotificationController

notificationController = NotificationController()

notifications = Blueprint(
    'notifications',
    __name__)

@notifications.route('/notifications', methods=["GET"])
def get_notification():
    return notificationController.get()

@notifications.route('/notifications/customer/<int:customer_id>', methods=["GET"])
def get_notificationByCustomer(customer_id):
    return notificationController.getNotificationByUser(customer_id)

@notifications.route('/notifications/send', methods=["POST"])
def send_notification():
    return notificationController.send()

@notifications.route('/notifications/group/send', methods=["POST"])
def send_notification_to_group():
    return notificationController.sendToGroup()

@notifications.route('/notifications/riders', methods=["POST"])
def notifyRiders():
    return notificationController.notifyRiders()