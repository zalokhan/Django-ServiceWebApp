from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
"""
For example:

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
"""


class User(models.Model):
    user_id = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=20)
    user_dob = models.CharField(max_length=20)
    user_creation_datetime = models.DateTimeField('creation datetime', default=timezone.now())

    # To print out the model in a readable format
    def __str__(self):
        model_string = "ID:" + str(self.user_id) + "; " + \
                       "EMAil:" + self.user_email + "; " + \
                       "FIRSTNAME:" + self.user_first_name + "; " + \
                       "LASTNAME:" + self.user_last_name + "; " + \
                       "PHONE:" + self.user_phone + "; " + \
                       "DOB:" + self.user_dob + "; " + \
                       "CREATE_DATETIME:" + str(self.user_creation_datetime) + "; "
        return model_string


class Message(models.Model):
    receiver = models.ForeignKey('User', on_delete=models.CASCADE, )
    sender = models.CharField(max_length=100)
    message_subject = models.CharField(max_length=200)
    message_body = models.CharField(max_length=1000)
    message_datetime = models.DateTimeField('message datetime')

    def __str__(self):
        model_string = "RECEIVER:" + self.receiver.user_id + ";" + \
                       "SENDER:" + self.sender + ";" + \
                       "SUBJECT:" + self.message_subject + ";" + \
                       "MESSAGE:" + self.message_body + ";" + \
                       "MESSAGE_DATETIME" + str(self.message_datetime) + ";"
        return model_string
