from rest_framework import serializers

from django.contrib.auth.models import User

from .models import *


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippets.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippets
        fields = ['id', 'title', 'code', 'created', 'linenos', 'language', 'style', 'owner']

# class SnippetsSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         return Snippets.objects.create(**validated_data)
#
#     def update(self, instance, validate_data):
#         instance.title = validate_data.get('title', instance.title)
#         instance.code = validate_data.get('code', instance.code)
#         instance.linenos = validate_data.get('linenos', instance.linenos)
#         instance.language = validate_data.get('language', instance.language)
#         instance.style = validate_data.get('style', instance.style)
#         instance.save()
#
#         return instance
