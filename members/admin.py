from django.contrib import admin

from .models import Profile

admin.site.register(Profile)

from .models import Poll

admin.site.register(Poll)

poll=Poll()
print("result")

print(poll.total())