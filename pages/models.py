from django.db import models


class Page(models.Model):
    CHOICES = [
        ('tutorial', 'Tutorial'),
        ('video', 'Video'),
    ]
    type = models.CharField(max_length=10, choices=CHOICES)


class Tutorial(models.Model):
    content = models.CharField(max_length=54)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="tutorials")
    
    def __str__(self):
        return self.content
    
    
class Video(models.Model):
    video = models.URLField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="videos")

    def __str__(self):
        return self.video
