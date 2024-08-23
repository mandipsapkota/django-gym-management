import django.contrib.auth.models
from django.shortcuts import render
from . import models
from . import forms
from django.template.loader import get_template
from django.shortcuts import redirect
import stripe 
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
    plans = models.SubPlan.objects.all().order_by('price')
    distinct_features = models.SubscriptionFeature.objects.all()
    return render(request , 'pricing.html' , {"plans":plans , "distinct_features":distinct_features})

# Signup
def signup(request):
    msg = ""
    if request.method == 'POST':
        form = forms.Signup(request.POST)
        if form.is_valid:
            form.save()
            msg = "Thank you for registering."
    form = forms.Signup
    return render(request , 'registration/signup.html' , {"form":form , "msg":msg})

# Checkout page 
def checkout(request , plan_id):
    planDetail = models.SubPlan.objects.get(pk =plan_id)
    return render(request, 'checkout.html' , {'plan':planDetail})


# Stripe payment 

stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
def checkout_session(request,plan_id):
    plan = models.SubPlan.objects.get(pk=plan_id)
    session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'npr',
        'product_data': {
          'name': plan.title,
        },
        'unit_amount': plan.price*132,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='https://opulent-carnival-464rqxvp59627456-8000.app.github.dev/pay_success?session_id={CHECKOUT_SESSION_ID}',
    cancel_url='https://opulent-carnival-464rqxvp59627456-8000.app.github.dev/pay_cancel',
    client_reference_id = plan_id

    )
    return redirect(session.url, code=303)

# Successful payment 
from django.core.mail import EmailMessage
def pay_success(request):
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    plan_id = session.client_reference_id
    plan = models.SubPlan.objects.get(pk=plan_id)
    user = request.user 
    models.Subscription.objects.create(
        plan=plan,
        user=user,
        price = plan.price
    )
    subject = "Order Email"
    html_content = get_template('orderemail.html').render({'title':plan.title})
    from_email = 'mandeepsapkota13@gmail.com'
    msg = EmailMessage(subject, html_content, from_email, ['mandeepsapkota13@gmail.com'])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

    return render(request , 'success.html')


# Unsuccessful payment 
def pay_cancel(request):
    return render(request , 'cancel.html')