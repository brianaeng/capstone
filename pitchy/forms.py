from django import forms
from django.contrib.auth.models import User
from .models import Profile, Focus#, Conversation, DirectMessage, Friendship
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('pic', 'bio', 'social_handle', 'company', 'focuses', 'role')

class FocusForm(forms.ModelForm):
    class Meta:
        model = Focus
        fields = ('name',)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

# class ConversationForm(forms.ModelForm):
#     # def __init__(self, friend_choices, *args, **kwargs):
#     #     super(ConversationForm, self).__init__(*args, **kwargs)
#     #
#     #     self.fields["user2"].choices = tuple(friend_choices)
#
#     class Meta:
#         model = Conversation
#         fields = ('user2',)
#
# class DirectMessageForm(forms.ModelForm):
#     class Meta:
#         model = DirectMessage
#         fields = ("body",)
