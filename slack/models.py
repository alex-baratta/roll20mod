# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.conf import settings
from django.db import models
from django.http import HttpResponse, JsonResponse


class HelloSlackAdapter(object):

    WEBHOOK_URL = ''

    HELLO_MESSAGE = {
        "text": "Hello!",
    }

    def respond_to_hello(self):
        return JsonResponse(self.HELLO_MESSAGE)
