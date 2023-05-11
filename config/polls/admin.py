

#polls/models.py 에서 추가해준 Question과 Choice를 등록

from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

