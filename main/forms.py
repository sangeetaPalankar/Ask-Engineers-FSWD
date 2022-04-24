from django.forms import ModelForm
from .models import Answer,Question,CustomUser
from main.models import CustomUser as User

class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=('detail',)

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=('title','detail')

class ProfileForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','username','bio')