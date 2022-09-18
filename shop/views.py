from django.shortcuts import render, redirect
from django.views import View
from shop.models import *
from shop.forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import auth

# Create your views here.

class BaseView(View):
    views = {}
    views['cat1'] = Category.objects.filter(status = 'active', level = 1)
    views['cat2'] = Category.objects.filter(status = 'active', level = 2)
    views['cat3'] = Category.objects.filter(status = 'active', level = 3)
    views['cat4'] = Category.objects.filter(status = 'active', level = 4)

class HomeView(BaseView):
    def get(self, request):

        # for slider
        self.views['slider'] = Slider.objects.filter(status = 'active')

        # for category
       

        # for items
        self.views['items'] = Item.objects.filter(status = 'active')

        return render(request, 'index.html', self.views)


class AboutView(BaseView):
    def get(self, request):
        return render(request, 'about.html')


class ContactView(BaseView):
    def get(self, request):
        return render(request, 'contact.html')


class ShopView(BaseView):
    def get(self, request, slug):
        category_id = Category.objects.get(slug = slug).id
        self.views['cat_items'] = Item.objects.filter(category = category_id)
        return render(request, 'shop.html', self.views)


class ItemDetailView(BaseView):
    def get(self, request, slug):
        self.views['details'] = Item.objects.filter(slug  = slug)

        item = Item.objects.get(slug = slug).category
        self.views['cat_view'] = Item.objects.filter(category = item)

        return render(request, 'product-single.html', self.views)


def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "You are registered Successfully")
            fm = SignupForm()

            return redirect('shop:signup')
    else:
        fm = SignupForm()
    return render(request, 'signup.html', {'form':fm})


def login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request = request, data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            pw = fm.cleaned_data['password'] 

            user = auth.authenticate(username = uname, password = pw)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "you are login successfully! ")
                return redirect('/')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form':fm})

def logout(request):
    auth.logout(request)
    return redirect('/')

class ItemSearchView(BaseView):
    def get(self,request):
        search = request.GET.get('search', None)
        if search:
            self.views['search_item'] = Item.objects.filter(name__icontains = search)
            self.views['search'] = search
            return render(request,'search.html', self.views)
        else:
            return redirect('shop:home')