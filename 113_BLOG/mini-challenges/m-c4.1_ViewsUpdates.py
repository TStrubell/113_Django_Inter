# Mini Challenge 3: Update PostCreateView, PostListView, PostUpdateView, and PostDetailView

#Update the views mentioned above to handle/display the new attribute status.

#Criteria:

#1. PostCreateView and PostUpdateView should display a dropdown menu on the form to select a status
#2. PostListView and PostDetail should display the status of the post

#Hint: You'll need to modify views and templates.

#==========================================================#

from django.urls import reverse_lazy


Place inside view.py:

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "status"]
    template_name = "posts/post_form.html"
    success_url = reverse_lazy("post_list")


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content", "status"]
    template_name = "posts/post_form.html"
    success_url = reverse_lazy("post_list")

class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

