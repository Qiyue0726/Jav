# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class FocusActor(models.Model):
    actor_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    sort_no = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.actor_id,self.name)

    class Meta:
        managed = False
        db_table = 'focus_actor'


class SysOptions(models.Model):
    option_key = models.CharField(max_length=30)
    option_value = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '%s: %s' % (self.comment,self.option_value)

    class Meta:
        managed = False
        db_table = 'sys_options'


class Actor(models.Model):
    actor_id = models.CharField(max_length=50)
    actor_name = models.CharField(max_length=100)
    letter = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.actor_id,self.actor_name)

    class Meta:
        managed = False
        db_table = 'actor'
