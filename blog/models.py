from django.db import models

# Create your models here.

class Post(models.Model):
    """
    Represents a blog post in the application.

    Attributes:
        id (AutoField): A unique identifier for the post.
        title (CharField): The title of the post, limited to 140 characters.
        body (TextField): The main content of the post, with a default string.
        signature (CharField): The author's signature, limited to 140 characters, defaulting to "Calvin Hattingh".
        date (DateTimeField): The date and time when the post was created.
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body = models.TextField(default='some string')
    signature = models.CharField(max_length=140, default="Calvin Hattingh")
    date = models.DateTimeField()

    def __str__(self):
        """Return the string representation of the post, which is the title."""
        return self.title
