# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

from .models import HelloSlackAdapter


class RollView(View):
    def post(self, request, *args, **kwargs):
        return HelloSlackAdapter().respond_to_hello()

