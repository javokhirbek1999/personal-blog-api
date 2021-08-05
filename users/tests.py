from django.test import TestCase

from django.contrib import auth
from .models import User

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('test@gmail.com','iamtest', 'test','test123')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()
    
    def testLogin(self):
        self.client.login(username='test@gmail.com',password='test123')
