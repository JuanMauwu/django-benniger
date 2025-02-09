from rest_framework import serializers

from myapp.models import Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "active"
        ]
    