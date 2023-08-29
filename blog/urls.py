from django.urls import path

from blog.views import index, list_categories, detail_category, detail_post, create_category_form, create_category, \
    create_post, create_post_form, update_category, update_category_form, delete_category

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
         name="create_category"),
    path("post/create", create_post,
         name="create_post"),
path("post/create_form", create_post_form,
         name="create_post_form"),
path("category/update", update_category,
         name="update_category"),
path("category/update_form/<int:id>", update_category_form,
         name="update_category_form"),
path("category/delete/<int:id>", delete_category,
         name="delete_category"),

]