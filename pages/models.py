from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Page(models.Model):
    CHOICES = [
        ('tutorial', 'Tutorial'),
        ('video', 'Video'),
    ]
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return self.title


class Tutorial(models.Model):
    # content = CKEditor5Field('Content')
    content = models.CharField(max_length=100)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="tutorials")
    
    def __str__(self):
        return self.content
    
    
class Video(models.Model):
    video = models.URLField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="videos")

    def __str__(self):
        return self.video
