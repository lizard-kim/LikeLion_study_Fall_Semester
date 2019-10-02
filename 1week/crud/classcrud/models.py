from django.db import models

# python manage.py makemigrations : python code --> DB
# python manage.py migrate : accept my model to DB

class ClassBlog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) # auto input
    updated_at = models.DateTimeField(auto_now=True) # auto input
    body = models.TextField()

    def __str__(self): # make class data to text(string) / in admin page, we can see titles by this method
        return self.title

# after this step, we should accept this model to admin.py