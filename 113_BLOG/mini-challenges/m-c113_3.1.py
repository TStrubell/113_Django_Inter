# MINI CHALLENGE 2: STATUS MODEL
# 
# Create a new model above the Post model called: "Status". The criteria for the model's attributes are:

# 1. A charfield attribute called name that it's unique and a maximun of 128 chars
# 2. A charfield attribute called description with a help text that says "Write a description about the status" and a maximum of 200 chars.

# Make sure to add the to string method.

# STATUS MODEL
class Status(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True
    )
    description = models.CharField(
        max_length=200,
        help_text="Write a description about the status"
    )

    def __str__(self):
        return self.name

# POST MODEL
class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def __str__(self):
        return self.title


# Create sample fixtures (JSON format) and  & posts/fixtures/post_fixture.json

## Place the following JSON data in posts/fixtures/status_fixture.json
[
    {
        "model": "posts.status",
        "pk": 1,
        "fields": {
            "name": "Draft",
            "description": "Post is still being written"
        }
    },
    {
        "model": "posts.status",
        "pk": 2,
        "fields": {
            "name": "Published",
            "description": "Post is visible to all users"
        }
    },
    {
        "model": "posts.status",
        "pk": 3,
        "fields": {
            "name": "Archived",
            "description": "Post is no longer active"
        }
    }
]

## Place the following JSON data in posts/fixtures/post_fixture.json
[
    {
        "model": "posts.post",
        "pk": 1,
        "fields": {
            "title": "My First Post",
            "content": "This is the content of the first post.",
            "status": 2
        }
    },
    {
        "model": "posts.post",
        "pk": 2,
        "fields": {
            "title": "Work in Progress",
            "content": "Draft content goes here.",
            "status": 1
        }
    },
    {
        "model": "posts.post",
        "pk": 3,
        "fields": {
            "title": "Old Announcement",
            "content": "This post has been archived.",
            "status": 3
        }
    }
]

# LOAD FIXTURES: 
    # RUN: py manage.py loaddata status_fixture.json
    # RUN: py manage.py loaddata post_fixture.json 