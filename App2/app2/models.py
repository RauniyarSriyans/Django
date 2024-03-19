from typing import Any
from django.db import models

# Create your models here.
# model is just a Python class 
# model also represents a table in the database
# attributes are the fields in the table

class JobPosting(models.Model):
    # by default, there's an id field 
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    email = models.EmailField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} | {self.company} | active={self.is_active}'

# there are two commands one has to always use while making changes to the database 
# one is makemigrations and the second is migrate
    # makemigrations --> tells django how the database has changed
    # migrate --> actually makes the changes