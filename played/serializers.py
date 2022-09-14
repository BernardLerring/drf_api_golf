from django.db import IntegrityError
from rest_framework import serializers
from played.models import Played

class PlayedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Played
        fields = [
            'id', 'created_at', 'owner', 'post'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })