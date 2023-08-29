from django.shortcuts import render

# Create your views here.
from blog.models import Post, Category


def index(request):
    data = Post.objects.all()
    content = {"posts":data}
    return render(request, "index.html", content)

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
                  {"category":data,
                "error_message":error_message} )


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
    message = "new category "+name+" has been created"
    try:
        Category.objects.create(name=name)
    except:
        message = "some error there"
    return render(request, 'create_category.html',
                  {'message':message})

def create_category_form(request):
    return render(request,
                  'create_category_form.html', {})


def create_post(request):
    title = request.POST.get("post_title")
    body = request.POST.get("post_body")
    category_id = request.POST.get("category_id")
    message = "new post "+title+" has been created"
    try:
        Post.objects.create(title=title, body=body, category_id=category_id)
    except:
        message = "some error there"
    return render(request, 'create_post.html',
                  {'message':message})

def create_post_form(request):
    return render(request,
                  'create_post_form.html',
                  {"categories":Category.objects.all()})



