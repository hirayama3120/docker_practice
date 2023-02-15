from django.db import models


class TOrder(models.Model):
    commands = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 't_order'
