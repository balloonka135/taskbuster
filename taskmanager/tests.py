# -*- coding: utf-8 -*-

from django.test import TestCase

from django.contrib.auth import get_user_model
from . import models


class TestProfileModel(TestCase):

    def test_profile_creation(self):
        User = get_user_model()
        user = User.objects.create(username='taskbuster', password='django_tutorial')
        self.assertIsInstance(user.profile, models.Profile)
        user.save()
        self.assertIsInstance(user.profile, models.Profile)
