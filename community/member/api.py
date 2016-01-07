# -*- coding: utf-8 -*-
from rest_framework import generics

from .models import Member
from . import serializers


class MemberList(generics.ListCreateAPIView):
    serializer_class = serializers.MemberSerializer

    def get_queryset(self):
        return Member.objects.all()
