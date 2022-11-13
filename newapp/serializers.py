from rest_framework import serializers
from django.contrib.auth.models import User
from newapp.models import Questions,Answers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["email","username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class AnswerSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    questions=serializers.CharField(read_only=True)
    votecount=serializers.CharField(read_only=True)
    class Meta:
        model=Answers
        fields=["id","questions","user","created_date","votecount"]
    
    def create(self, validated_data):
        ques=self.context.get("question")
        usr=self.context.get("user")
        return ques.answers_set.create(user=usr,**validated_data)



class QuestionSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    question_answers=AnswerSerializer(read_only=True)

    class Meta:
        model=Questions
        fields=[
            "title",
            "description",
            "image",
            "user",
            "question_answers"
        ]

