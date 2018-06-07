from django.db import models
from django.db.models import (Model, DO_NOTHING,
    IntegerField, BooleanField, CharField,
    DecimalField,
    ForeignKey, OneToOneField)

from django.contrib.auth.models import User

class Upload(Model):
    filename = CharField(max_length=1000, null=True)

    def __str__(s):
        return "<Upload filename: '%s'>" % s.filename

class Customer(Model):

    STATUS_NEW = "new"
    STATUS_CANCELLED = "canceled"

    PURCHASE_STATUS_CHOICES = (
        (STATUS_NEW, "New"),
        (STATUS_CANCELLED, "Cancelled")
        )

    customer_id = IntegerField(null=True, db_index=True)
    first_name = CharField(max_length=1000, null=True)
    last_name = CharField(max_length=1000, null=True)
    address = CharField(max_length=1000, null=True)
    state = CharField(max_length=2, null=True)
    zipcode = IntegerField(null=True)

    purchase_status = CharField(max_length=100, null=True,
                                choices=PURCHASE_STATUS_CHOICES)

    upload = ForeignKey(Upload, null=True, on_delete=DO_NOTHING)

    def __str__(s):
        return str({a: b for a,b in s.__dict__.items() if a != '_state'})

class Product(Model):

    customer = ForeignKey(Customer, null=True, on_delete=DO_NOTHING)

    product_id = IntegerField(null=True, db_index=True)
    name = CharField(max_length=1000, null=True)
    price = DecimalField(decimal_places=2, default=0, max_digits=17)

    time = models.DateTimeField(null=True)

    upload = ForeignKey(Upload, null=True, on_delete=DO_NOTHING)

    def __str__(s):
        return str({a: b for a,b in s.__dict__.items() if a != '_state'})

