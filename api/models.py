# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Userinfo(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

class info(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

class FocusActor(models.Model):
    id = models.IntegerField(primary_key=True)
    actor_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'focus_actor'
