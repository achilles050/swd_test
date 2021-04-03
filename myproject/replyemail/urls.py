from django.urls import path
from .views import ReplyEmail

urlpatterns = [
    path('', ReplyEmail.as_view(), name='replyemail'),
]