from django.db import models

from django.contrib.auth.models import User, Group
# Create your models here.

class SubGroup(models.Model):
    name = models.CharField(max_length=30)
    main_group = models.ForeignKey(Group, related_name='sub_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.name