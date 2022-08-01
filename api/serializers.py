from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.authtoken.models import Token


class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_ratings')


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'meal')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     token = Token.objects.create(user=user)
    #     return token