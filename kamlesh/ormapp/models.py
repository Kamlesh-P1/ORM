from django.db import models
from django.contrib import admin
class showroom(models.Model):
      Car_model=models.CharField(max_length=20)
      Series=models.CharField()
      Color=models.CharField(max_length=15)
      Engine_number=models.IntegerField(primary_key=True) 
      Fancy_number=models.IntegerField()  
class showroomAdmin(admin.ModelAdmin):
      list_display=["Car_model","Series","Color","Engine_number","Fancy_number"]