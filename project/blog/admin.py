from django.contrib import admin
from blog.models import Account,Posts,Book,Role,AccountBook



# Register your models here.

admin.site.register(Account)
admin.site.register(Book)
admin.site.register(Posts)
admin.site.register(Role)
admin.site.register(AccountBook)