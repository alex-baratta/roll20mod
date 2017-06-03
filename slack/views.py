# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import HelloSlackAdapter


@method_decorator(csrf_exempt, name='dispatch')
class RollView(View):
    def post(self, request, *args, **kwargs):
        return HelloSlackAdapter().respond_to_hello()

