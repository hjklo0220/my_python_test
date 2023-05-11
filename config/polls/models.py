from django.db import models


class Question(models.Model):       #Qustion 모델 생성
    question_text = models.CharField(max_length=200)    #질문 내용 CharField문자열로 이루어진 데이터필드, 글자수 제한
    pub_date = models.DateTimeField('data Published')   #발행 날짜
    def __str__(self):
        return self.question_text


class Choice(models.Model):         #Choice 모델 생성
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #왜래키 설정 Question이 지워지면 Choice도 지워지도록 CASCADE
    choice_text = models.CharField(max_length=200)  #
    votes = models.IntegerField(default=0)          #정수형 데이터 필드 default값 설정
    def __str__(self):
        return self.choice_text

