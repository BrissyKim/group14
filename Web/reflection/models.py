import re
from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


STATUS_CHOICES = (
     ('d', 'Draft'),
     ('p', 'Published'),)


class Reflection(models.Model):
    #author = models.CharField(max_length=20)
    title = models.CharField(max_length=20, verbose_name = 'title')
    team_number  = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(50)], blank=True, null=True)
    week = models.IntegerField(default=2, validators=[MinValueValidator(2), MaxValueValidator(12)], blank=True, null=True)
    student_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    #student_name = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(7)], help_text ='Reflect on how well you delivered your product')
    self_reflection = models.TextField(verbose_name ='Self-reflection',help_text ='Reflect on how you delivered on your three main tasks for the last fortnight')
    self_plan = models.TextField(verbose_name ='Detail your three main tasks for the next fortnight',help_text ='Detail your three main tasks for the next fortnight')


    team1_name= models.CharField(max_length=100, verbose_name = 'Student 1 Name')
    team1_grade = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(7)], help_text ='Grade between 1 and 7')
    team1_reflection = models.TextField(verbose_name ='Evaluation of contribution and performance')

    team2_name = models.CharField(max_length=100, verbose_name = 'Student 2 Name')
    team2_grade = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(7)], help_text ='Grade between 1 and 7')
    team2_reflection = models.TextField(verbose_name ='Evaluation of contribution and performance')

    team3_name = models.CharField(max_length=100, verbose_name = 'Student 3 Name')
    team3_grade = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(7)], help_text ='Grade between 1 and 7')
    team3_reflection = models.TextField(verbose_name ='Evaluation of contribution and performance')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        ordering = ['-id']
        ordering = ['team_number']

    def __str__(self):
        return self.title

#form 작성시 이게 있어야 저장됨
    def get_absolute_url(self):
        return reverse('reflection:reflection_detail', args=[self.id])
