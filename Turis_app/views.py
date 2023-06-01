from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

def home_page(request): 
    context = {'home': 'active'}
    return render(request,'home.html',context)

def about_page(request):
    abouts = about.objects.first()
    carusels = aboutcarusel.objects.all()
    context = {
        'abouts': abouts,
        'carusels':carusels,
        'about': 'active',
    }
    return render(request,'about.html',context)

def service_page(request):
    articles = service.objects.all()    
    context = {
        'articles': articles,
        'article': 'active'
    }
    if request.method=='POST':
        name=request.POST['name']
        country=request.POST['country']
        description=request.POST['description']
        img=request.FILES['img']
        servic=service(
            name=name, country=country, description=description,
            img=img, 
        )
        servic.save()
        msg=f'Xurmatli {name} , sizning ma`lumotingiz qabul qilindi.'
        context['message']=msg
    return render(request, 'service.html', context)

def package_page(request):
    products = packages.objects.all()
    q = request.GET.get('q', None)
    if q is not None:
        products = products.filter(Q(product_name__icontains=q))


    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': products,
        "products": paged_products,
        'pac': 'active'
    }
    return render(request,'package.html',context)

def destination_page(request):
    products = des.objects.all()
    q = request.GET.get('q', None)
    if q is not None:
        products = products.filter(Q(product_name__icontains=q))


    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': products,
        "products": paged_products,
        'des': 'active',
    }
    return render(request,'destination.html',context)

def team_page(request):
    carusels = aboutcarusel.objects.all()
    context = {
        'carusels':carusels,
        'team': 'active'
    }
    return render(request,'team.html',context)

def testimonial_page(request):
    articles = service.objects.all()    
    context = {
        'articles': articles,
        'test': 'active'
    }
    return render(request,'testimonial.html',context)

def contact_page(request):
    context = {'contact': 'active'}
    return render(request,'contact.html',context)

def Not_found(request):
    context = {'Not': 'active'}
    return render(request,'404.html',context)
    
def blog_detail(request, cat_id):
    print(cat_id)
    blog = packages.objects.all().get(id=cat_id)
    blog.save()
    context = {'blog': blog}
    return render(request, 'more.html', context)

def contact(request):
    map = Map.objects.filter().first()
    context = {
        'map': map
    }
    if request.method=='POST':
        name=request.POST['fullname']
        contact_number=request.POST['phone']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['text']
        data=ContactUs(
            fullname=name,phone=contact_number,email=email,
            subject=subject,text=message
        )
        data.save()
        msg=f'Xurmatli {name} , sizning shikoyatingiz qabul qilindi'
        context['message']=msg
    return render(request,'contact.html',context)