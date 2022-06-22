from django.contrib import admin
from .models import Organization, Section, Garten, Child, Parent, Group, Admin_Garten, Admin_Organization

admin.site.register(Organization)
admin.site.register(Section)
admin.site.register(Garten)
admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(Group)
admin.site.register(Admin_Organization)
admin.site.register(Admin_Garten)

