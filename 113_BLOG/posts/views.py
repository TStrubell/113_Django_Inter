# posts/views.py

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    View
)
from .forms import CommentForm
from .models import Post, Status
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin

# Create your own view here.
class PostListView(ListView):   # GET Request --> Multiple Objects (e.g., List of Posts)
    # template_name attribute renders specific html file
    template_name = "posts/list.html"
    # model attribute lets Django know from which model (table) to retrieve data from
    model = Post
    # context_object_name attribute allows us to change the name on how we call it inside of the templates
    context_object_name = "posts"

# SELECT * FROM posts

class PostDetailView(LoginRequiredMixin, DetailView):   # GET Request --> Single Object
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = self.object.comments.all()
        return context

class PostCommentFormView(SingleObjectMixin, FormView):
    template_name = "posts/detail.html"
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.save() # needs a PK before the many-to-many .add() below works
        comment.posts.add(self.object)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.pk})

class PostCreateView(LoginRequiredMixin, CreateView): # POST Request -> New Object / Empty form (HTML)
    template_name = "posts/new.html"
    model = Post
    # fields attribute is a list that allow us to enable/disable the inputs to render in the form
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        # This function help us to run some validations before we create the object
        print (form)
        form. instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView): # POST Request -> A form to update an existing object
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(LoginRequiredMixin, DeleteView): # POST Request -> A form to handle the delete functionality
    template_name = "posts/delete.html"
    model = Post
    # success_url attribute allow us to redirect the user to another view if the request is successful
    success_url = reverse_lazy("post_list")

