from django.db import models

# Create your models here.
class Profile(models.Model):
    BG_CHOICES = (
        ('blue', 'Blue'), 
        ('yellow', 'Yellow'), 
        ('green', 'Green'), 
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self):
        return self.name
    
class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()
    # this basically establishes a relation with the table above
    # models.cascade means if the profile is deleted above, delete all the links associated too
    # related names is more like accessing via attribute, now we have something called profile.links
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return f'{self.text} | {self.profile}'


