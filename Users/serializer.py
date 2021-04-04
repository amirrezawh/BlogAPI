from rest_framework import serializers
from .models import NewUser
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from django.utils.translation import ugettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, required=True, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password' : {'write_only' : True}}
    
    def create(self, validated_data):

        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = NewUser
        fields = ['email']

class HandleResetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = NewUser
        fields = ['password']

class TokenBlackListSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')