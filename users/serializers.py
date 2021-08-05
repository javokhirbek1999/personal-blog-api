from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username','password', 'name', 'joined_at')
        extra_kwargs = {'password':{'style':{'input_type':'password'},'write_only':True,},}
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        if validated_data['password'] is not None:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
            