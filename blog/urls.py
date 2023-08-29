from django.urls import path

from blog.views import index, list_categories, detail_category, detail_post, create_category_form, create_category

urlpatterns = [
    path("", index, name="home"),
    path("categories", list_categories, name="categories"),
    path("category/<int:id>", detail_category,
         name="detail_category"),
    path("post/<int:id>", detail_post,
         name="detail_post"),
    path("category/create_form", create_category_form,
         name="create_category_form"),
    path("category/create", create_category,
         name="create_category")

]