import imp
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

AGE_OF_DRAGON = (
  ('egg','EGG'),
  ('yearling', 'YEARLING'),
  ('immature', 'IMMATURE'),
  ('adult', 'ADULT'),
  ('great','GREAT'),
  ('Ancient', 'ANCIENT')
  )

class Dragon(models.Model):
  spotter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  name_of_dragon = models.CharField(max_length=64, default="Unknown")
  title = models.CharField(max_length= 256, default="Unkown")
  color = models.CharField(max_length=48, default="None")
  age = models.CharField(max_length=8, choices=AGE_OF_DRAGON, default="adult")
  estimated_height = models.IntegerField()
  descritption_of_dragon = models.TextField()

