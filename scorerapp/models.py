from django.db import models


class ImageScore(models.Model):
    image_path = models.URLField()
    score = models.IntegerField(default=-1)
    scorer = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.image_path}:\n ({self.scorer}, {self.score})"  

