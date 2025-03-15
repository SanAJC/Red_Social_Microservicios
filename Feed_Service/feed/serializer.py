from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)  
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=280)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance