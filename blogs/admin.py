from django.contrib import admin
from .models import Categories, Posts, Tags, Authors, CustomUser
# from .forms import PostForm, CategoryForm


# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = ({'slug': ('category_name',)})

admin.site.register(Categories, CategoriesAdmin)

admin.site.register(Posts)
admin.site.register(Tags)
admin.site.register(Authors)
admin.site.register(CustomUser)
# admin.site.register(PostForm)
# admin.site.register(CategoryForm)


