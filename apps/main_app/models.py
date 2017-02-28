from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def add_user(self, data):
        errors = []
        if len(data['name']) < 2:
            errors.append('First Name must be at least 2 characters long.')
        if len(data['alias']) < 2:
            errors.append('Last Name must be at least 2 characters long.')
        if not data['email']:
            errors.append('Email field in required')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('Enter a valid email')
        if len(data['password']) < 8:
            errors.append('Password must be at least 8 characters long.')
        if data['password'] != data['confirm_password']:
            errors.append('Password must match.')
        if not len(data['dob']):
            errors.append('Date of birth is required!')

        user = self.filter(email=data['email'])
        if user:
            errors.append('Email already exists')

        response = {}

        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            hashed_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            user = self.create(name = data['name'], alias = data['alias'], email = data['email'], dob = data['dob'], password = hashed_password)
            response['status'] = True
            response['user'] = user

        return response

    def check_user(self, data):
        user = self.filter(email=data['email'])
        errors = []
        response = {}
        if user:
            if bcrypt.hashpw(data['password'].encode(), user[0].password.encode()) == user[0].password.encode():
                print("It Matches!")
                response['status'] = True
                response['loggedin_user'] = user[0]
            else:
                print("It Does not Match :(")
                errors.append('Invalid email/password combination.')
                response['status'] = False
                response['errors'] = errors
        else:
            # email does not exits in DB
            errors.append('Email does not exist.')
            response['status'] = False
            response['errors'] = errors

        return response

class User(models.Model):
    name = models.CharField(max_length = 45)
    alias = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    dob = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
