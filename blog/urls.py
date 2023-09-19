from django.urls import path

from blog.views import index, list_categories, detail_category, detail_post, create_category_form, create_category, \
    create_post, create_post_form, update_category, update_category_form, delete_category, HomePageView, PostDetailView, \
    PostCreateView, PostUpdateView, PostDeleteView, register_view, register_form, update_profile_view, \
    update_profile_form, ProfileDetailView, likes, read_excel

urlpatterns = [
    # path("", index, name="home"),
    path("", HomePageView.as_view(), name="home"),
    path("categories", list_categories, name="categories"),
    path("category/<int:id>", detail_category,
         name="detail_category"),
    # path("post/<int:id>", detail_post,
    #      name="detail_post"),
    path("post/<int:pk>", PostDetailView.as_view(),
         name="detail_post"),
    path("category/create_form", create_category_form,
         name="create_category_form"),
    path("category/create", create_category,
         name="create_category"),
    # path("post/create", create_post,
    #      name="create_post"),
    path("post/create", PostCreateView.as_view(),
         name="create_post"),
    path("post/create_form", create_post_form,
         name="create_post_form"),
    path("category/update", update_category,
         name="update_category"),
    path("category/update_form/<int:id>", update_category_form,
         name="update_category_form"),
    path("category/delete/<int:id>", delete_category,
         name="delete_category"),
    path("post/update/<int:pk>", PostUpdateView.as_view()
         , name="update_post_view"),
    path("post/delete/<int:pk>", PostDeleteView.as_view()
         , name="delete_post_view"),
    path("user/register", register_view,
         name="register_view"),
    path("user/register_form", register_form,
         name="register_form"),
    path("user/update_profile", update_profile_view,
         name="update_profile"),
    path("user/update_profile_form", update_profile_form,
         name="update_profile_form"),
    path("user/profile/<int:pk>", ProfileDetailView.as_view(),
         name="detail_profile"),
    path("post/likes", likes, name="likes"),
    path("upload_files", read_excel, name="upload_files"),
]
