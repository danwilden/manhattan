from django.db import models


class Business(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    owner_email = models.EmailField()
    business_type = models.CharField(max_length=200)


    def __str__(self):
        #String representation of the models
        return self.name


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    business = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    def __str__(self):
        #String representation of the models
        return self.name


class item_types(models.Model):
    id = models.AutoField(primary_key=True)
    item_type = models.CharField(max_length=200)
    item = models.CharField(max_length=200)

    def __str__(self):
        #String representation of the models
        return self.name
