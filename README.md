# Ex02 Django ORM Web Application
## Date: 08-10-2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import showroom,showroomAdmin
admin.site.register(showroom,showroomAdmin)
```

## OUTPUT
![alt text](<Screenshot 2025-10-08 211057.png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
