import unittest
import os
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask import json
from extensions import db
from models.Notification import Notification

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

class NotificationTestCase(unittest.TestCase):
    """Test case for the notification blueprint."""

    def setUp(self):
        engine = create_engine(os.environ.get("TEST_DATABASE_URI"))
        if not database_exists(engine.url):
            create_database(engine.url)
        """Set up test variables."""
        app = create_app("Testing")
        
        self.app = app
        # initialize the test client
        self.client = self.app.test_client
       
        self.headers = {
            'Content-Type': 'application/json'}
        self.port="7000"
        
        self.db = db

        # binds the app to the current context
        with self.app.app_context():
            self.db.create_all()
        
    
    def tearDown(self):
        with self.app.app_context():
            # db.session.remove()
            self.db.drop_all()

    def test_get_notifications(self):
        """Test get notifications"""
        
        resp = self.client().get(
            "/api/notifications", headers=self.headers)
        # get the results returned in json format
        result = json.loads(resp.data)
        self.assertTrue(result['status'])
        self.assertEqual(resp.status_code, 200)
    
    def test_get_notification_by_customer(self):
        """Test get notification by customer"""
        
        resp = self.client().get(
            "/api/notifications/customer/1", headers=self.headers)
        # get the results returned in json format
        result = json.loads(resp.data)
        self.assertTrue(result['status'])
        self.assertEqual(resp.status_code, 200)
    
    def test_send_notification(self):
        """Test send single notification to customer"""
        # get the notification size
        notifications = Notification.query.all()
        
        json_data = {
            "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
            "should_send_sms": True,
            "customer_id": 1
        }
        resp = self.client().post(
            "/api/notifications/send", json = json_data, headers=self.headers)
        
        # after insertations get the notifications to ensure is in the database
        actual_notifactions = Notification.query.all()
        # get the results returned in json format
        result = json.loads(resp.data)
        self.assertTrue(result['status'])
        self.assertEqual(result['message'], 'sent')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(notifications) + 1, len(actual_notifactions))

    def test_failed_send_notification(self):
        """Test failed send single notification to customer"""
        
        # get the notification size
        notifications = Notification.query.all()

        json_data = {
            "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
            "should_send_sms": True,
            "customer_id": 1000000
        }
        resp = self.client().post(
            "/api/notifications/send", json = json_data, headers=self.headers)
        
        # after insertations get the notifications to ensure is in the database
        actual_notifactions = Notification.query.all()

        # get the results returned in json format
        result = json.loads(resp.data)
        
        self.assertFalse(result['status'])
        self.assertEqual(result['message'], 'Customer not found')
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(len(notifications) , len(actual_notifactions))
    
    def test_send_group_notification(self):
        """Test send group notification to a group of customers"""
        # get the notification size
        notifications = Notification.query.all()
        
        json_data = {
            "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
            "should_send_sms": True,
            "group_id": 1
        }
        resp = self.client().post(
            "/api/notifications/group/send", json = json_data, headers=self.headers)
        
        # after insertations get the notifications to ensure is in the database
        actual_notifactions = Notification.query.all()
        # get the results returned in json format
        result = json.loads(resp.data)
        self.assertTrue(result['status'])
        self.assertEqual(result['message'], 'sent')
        self.assertEqual(resp.status_code, 200)
        self.assertGreater(len(actual_notifactions), len(notifications))

    def test_send_failed_group_notification(self):
        """Test send failed group notification to a group of customers"""
        # get the notification size
        notifications = Notification.query.all()
        
        json_data = {
            "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
            "should_send_sms": True,
            "group_id": 100
        }
        resp = self.client().post(
            "/api/notifications/group/send", json = json_data, headers=self.headers)
        
        # after insertations get the notifications to ensure is in the database
        actual_notifactions = Notification.query.all()
        # get the results returned in json format
        result = json.loads(resp.data)
        print(result)
        self.assertFalse(result['status'])
        self.assertEqual(result['message'], 'Group not found')
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(len(actual_notifactions), len(notifications))
    
    def test_send_notification_to_rider(self):
        """Test send notification to rider"""
        # get the notification size
        notifications = Notification.query.all()
        
        json_data = {
            "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
            "should_send_sms": True,
            "user_id": 4,
        }
        resp = self.client().post(
            "/api/notifications/riders", json = json_data, headers=self.headers)
        
        # after insertations get the notifications to ensure is in the database
        actual_notifactions = Notification.query.all()
        # get the results returned in json format
        result = json.loads(resp.data)
        self.assertTrue(result['status'])
        self.assertEqual(result['message'], 'sent')
        self.assertEqual(resp.status_code, 200)
        self.assertGreater(len(actual_notifactions), len(notifications))
    
    def test_send_failed_notification_to_rider(self):
        """Test send notification to rider"""
        # get the notification size
        notifications = Notification.query.all()
        
        json_data = {
            "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
            "should_send_sms": True,
            "user_id": 40,
        }
        resp = self.client().post(
            "/api/notifications/riders", json = json_data, headers=self.headers)
        
        # after insertations get the notifications to ensure is in the database
        actual_notifactions = Notification.query.all()
        # get the results returned in json format
        result = json.loads(resp.data)
        self.assertFalse(result['status'])
        # self.assertEqual(result['message'], 'sent')
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(len(actual_notifactions), len(notifications))