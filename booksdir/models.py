from django.db import models

class Author(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
     
    def __str__(self):
        return self.fname + l.name

class Publisher(models.Model):
    publisher = models.CharField(max_length=30)

    def __str__(self):
        return self.publisher


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ManyToManyField(Author)
    pub_date = models.DateField(null=True)
    summary = models.TextField(max_length=5000,null=True)
    price = models.DecimalField(max_digits=65,decimal_places=2)
    link = models.URLField(max_length=300,null=True)
    img = models.URLField(max_length=300,null=True)
    publisher = models.ManyToManyField(Publisher)

    def __str__(self):
        return self.title


