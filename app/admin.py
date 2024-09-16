from django.contrib import admin
from .models import Category, Product,Contact,Enrollment,Trainer,MenbershipPlan

admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(MenbershipPlan)