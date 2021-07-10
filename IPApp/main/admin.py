from django.contrib import admin
from . models import Departments, Positions, Workers, PersonInfo, Experience, Tasks


admin.site.register(Departments)
admin.site.register(Positions)
admin.site.register(Workers)
admin.site.register(PersonInfo)
admin.site.register(Experience)
admin.site.register(Tasks)
