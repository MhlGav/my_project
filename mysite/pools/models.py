from django.db import models

# Create your models here.


class Feedback(models.Model):
    email = models.CharField(max_length=30)
    text = models.TextField()

class Comment(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    comment = models.TextField()

    def str(self):
        return self.comment