from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    reviewer = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    def get_reviewer(self, obj):
        return obj.reviewer.username

    def get_agent(self, obj):
        return obj.agent.user.username
