from django.db import models

# Create your models here.
class TagModel(models.Model):
    tag=models.CharField(max_length=30,unique=True)

    class Meta:
        db_table = 'tags'