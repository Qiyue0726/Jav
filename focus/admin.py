from django.contrib import admin

# Register your models here.
from focus.models import Actor, FocusActor, SysOptions

admin.site.register(Actor)
admin.site.register(FocusActor)
admin.site.register(SysOptions)