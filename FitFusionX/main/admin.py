from django.contrib import admin
from . import models

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('title',"image_tag")
admin.site.register(models.Service , ServiceAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_text' , 'image_tag')

admin.site.register(models.Banner,BannerAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display=('title' , )

admin.site.register(models.Page,PageAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display=('question' , )

admin.site.register(models.FAQ,FaqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('full_name' , )

admin.site.register(models.Enquiry,EnquiryAdmin)

# Gallery Admin
class GalleryAdmin(admin.ModelAdmin):
    list_display=('title' , "image_tag")

admin.site.register(models.Gallery,GalleryAdmin)

# Gallery Image 
class GalleryImageAdmin(admin.ModelAdmin):
    list_display=('alt_text' ,'image_tag' )

admin.site.register(models.GalleryImage,GalleryImageAdmin)

# SubscriptionPlan 
class SubPlanAdmin(admin.ModelAdmin):
    # list_editable = ('highlight_status','max_member')
    list_display=('title' ,'price' ,'highlight_status','max_member')

admin.site.register(models.SubPlan,SubPlanAdmin)

# Subscription Feature 
class SubPlanFeatureAdmin(admin.ModelAdmin):
    list_display=('title' ,'subplans')
    def subplans(self,obj):
        return " | ".join([sub.title for sub in obj.subplan.all()])

admin.site.register(models.SubscriptionFeature,SubPlanFeatureAdmin)

# Discount Feature 
class PlanDiscountAdmin(admin.ModelAdmin):
    list_display=('subplan','total_months' ,'total_discount')

admin.site.register(models.PlanDiscount,PlanDiscountAdmin)

# Subscriber Feature 
class SubscriberAdmin(admin.ModelAdmin):
    list_display=('user','mobile','image_tag')

admin.site.register(models.Subscriber,SubscriberAdmin)

# Subscription Feature
class SubscriptionAdmin(admin.ModelAdmin):
    list_display=('user','plan','price')

admin.site.register(models.Subscription,SubscriptionAdmin)