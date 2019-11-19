from djongo import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    created_at = models.CharField(max_length=100)

    def __str__(self):
        return self.title