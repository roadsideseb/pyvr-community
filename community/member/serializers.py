# -*- coding: utf-8 -*-
from rest_framework import serializers

from . import models


class MemberSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = models.Member
        fields = ('name', 'email', 'twitter', 'github', 'linkedin',
                  'current_position', 'notes', 'tags')
