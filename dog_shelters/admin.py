from django.contrib import admin
# from core.models import CustomUser
from dog_shelters.models import Shelter, Dog
from .models import Shelter, Dog

# Register your models here.
# admin.site.register(CustomUser)
admin.site.register(Shelter)
admin.site.register(Dog)



