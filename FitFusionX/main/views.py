from django.shortcuts import render
from . import models
from . import forms
# Create your views here.

# Home page 
def home(request):
    banners = models.Banner.objects.all()
    services = models.Service.objects.all()[:3]
    gimages = models.GalleryImage.objects.all().order_by("-id")[:9]
    return render(request , 'home.html' , {"banners":banners , "services":services , "gimages":gimages})

def page_detail(request,id):
    page = models.Page.objects.get(id = id)
    return render(request , 'page.html' , {'page':page })

def faq_list(request):
    faq = models.FAQ.objects.all()
    return render(request , 'faq.html' , {'faq':faq })

def enquiry(request):
    msg=''
    if request.method == 'POST' :
        form = forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            msg='Thank you for contacting us . We will get in touch with you soon . Meanwhile do some pushups.'

    # faq = models.FAQ.objects.all()
    form = forms.EnquiryForm
    return render(request , 'enquiry.html',{'form':form , 'msg':msg})

# Show gallery 
def gallery(request):
    gallery = models.Gallery.objects.all().order_by('-id')
    return render(request , 'gallery.html' , {'galleries':gallery})

# Show gallery photo 
def gallery_photo(request,id):
    gallery = models.Gallery.objects.get(id = id)
    gallery_imgs = models.GalleryImage.objects.filter(gallery = gallery).order_by('-id')
    return render(request , 'gallery_img.html' , {'gallery_images':gallery_imgs , 'gallery':gallery})

# Show pricing plans
def pricing(request):
    plans = models.SubPlan.objects.all()
    distinct_features = models.SubscriptionFeature.objects.all()
    return render(request , 'pricing.html' , {"plans":plans , "distinct_features":distinct_features})