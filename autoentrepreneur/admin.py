from django.contrib import admin
from autoentrepreneur.models import UserProfile, SalesLimit, Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    ordering = ['owner__username']

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['__unicode__','phonenumber','professional_email','activity','professional_category']

class SalesLimitAdmin(admin.ModelAdmin):
    list_filter=['year','activity']
    list_display=['__unicode__','year','activity','limit','limit2']
    list_editable=['year','activity','limit','limit2']

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(SalesLimit,SalesLimitAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
