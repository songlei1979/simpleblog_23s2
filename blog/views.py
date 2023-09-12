from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post, Category, Profile


def index(request):
    data = Post.objects.all()
    content = {"posts": data}
    return render(request, "index.html", content)

# class HomePageView(TemplateView):
#     # template
#     template_name = "home.html"
#
#     # return data
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_posts'] = Post.objects.all()[0:5]
#         return context

class HomePageView(ListView):
    template_name = "home.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "detail_post_view.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "create_post_view.html"
    model = Post
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = "update_post_view.html"
    model = Post
    form_class = PostForm


class PostDeleteView(DeleteView):
    template_name = "delete_post_view.html"
    model = Post
    success_url = reverse_lazy("home")

def list_categories(request):
    data = Category.objects.all()
    content = {'categories': data}
    return render(request, "list_categories.html", content)


def detail_category(request, id):
    error_message = ""
    try:
        data = Category.objects.get(id=id)
    except Category.DoesNotExist:
        error_message = "The category does not exist"
        data = None
    return render(request, "detail_category.html",
                  {"category": data,
                   "error_message": error_message})


def detail_post(request, id):
    error_message = ""
    try:
        data = Post.objects.get(id=id)
    except Post.DoesNotExist:
        error_message = "The category does not exist"
        data = None
    return render(request, "detail_post.html",
                  {"post": data,
                   "error_message": error_message})


def create_category(request):
    name = request.POST.get("category_name")
    message = "new category " + name + " has been created"
    try:
        Category.objects.create(name=name)
    except:
        message = "some error there"
    return render(request, 'create_category.html',
                  {'message': message})


def create_category_form(request):
    return render(request,
                  'create_category_form.html', {})


def create_post(request):
    title = request.POST.get("post_title")
    body = request.POST.get("post_body")
    category_id = request.POST.get("category_id")
    message = "new post " + title + " has been created"
    try:
        Post.objects.create(title=title, body=body, category_id=category_id)
    except:
        message = "some error there"
    return render(request, 'create_post.html',
                  {'message': message})


def create_post_form(request):
    return render(request,
                  'create_post_form.html',
                  {"categories": Category.objects.all()})


def update_category(request):
    name = request.POST.get("category_name")
    id = request.POST.get("category_id")
    message = "the category " + name + " has been updated"
    try:
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
    except:
        message = "some error there"
    return render(request, 'update_category.html',
                  {'message': message})


def update_category_form(request, id):
    message = ""
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        message = "something wrong"
    return render(request,
                  'update_category_form.html',
                  {"category": category, "message": message})


def delete_category(request, id):
    message = ""
    print("id:"+str(id))
    try:
        print("get")
        category = Category.objects.get(id=id)
        print(category.name)
        category.delete()
    except Category.DoesNotExist:
        message = "something wrong"
    return HttpResponseRedirect(reverse('categories'))


def register_view(request):
    # Django User
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    password = request.POST.get("password")
    email = request.POST.get("email")
    # Profile Model
    address = request.POST.get("address")
    phone_number = request.POST.get("phone_number")
    web_page = request.POST.get("web_page")
    message = "user has been created"
    try:
        user = User.objects.create(first_name=first_name,
                                   last_name=last_name,
                                   email=email)
        user.set_password(password)
        user.save()
        try:
            profile = Profile.objects.create(user=user, address=address
                                             , phone_number=phone_number
                                             , web_page=web_page)
        except:
            message = "Cannot create profile for this user"
    except:
        message = "Cannot create this user"

    return render(request, 'register_user.html',
                  {'message': message})



