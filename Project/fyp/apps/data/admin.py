from django.contrib import admin

from apps.data.models import GymPlan, UserBooking

# Register your models here.
admin.site.register(GymPlan)
admin.site.register(UserBooking)