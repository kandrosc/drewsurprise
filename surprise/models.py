from django.db import models

# Create your models here.
class Message(models.Model):
    days = (
        ("1", "June 2nd"),
        ("2", "June 6th"),
        ("3", "June 10th"),
        ("4", "June 14th")
    )
    day = models.CharField(
        max_length=1,
        choices=days,
        primary_key=True
    )

    content = models.CharField(max_length=10000)

class Image(models.Model):
    day = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE
    )

    upload = models.ImageField(upload_to='images')
