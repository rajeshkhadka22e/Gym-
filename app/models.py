# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=500, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_products')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=233, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=500, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)  # Corrected to auto_now=True

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title
    




class Contact(models.Model):
    name=models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    description = models.TextField()


    def __str__(self):
        return self.name
    


class Enrollment(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    MEMBERSHIP_CHOICES = [
        ('basic', 'Basic Plan'),
        ('premium', 'Premium Plan'),
        ('vip', 'VIP Plan'),
    ]

    FullName = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12)
    dob = models.DateField(verbose_name='Date of Birth')

    # Membership Plan Selection
    membership_plan = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES)

    # Trainer Selection (assuming you have a Trainer model)
    Selecttrainer = models.CharField(max_length=25)

    # Reference for how they found you
    reference = models.CharField(max_length=255, blank=True)
    payment_status = models.CharField(max_length=55,blank=True, null=True)
    price = models.IntegerField(blank=True,null=True)
    DueDate = models.DateTimeField(blank=True,null=True)
    # Address field
    address = models.TextField()
    timestamp =models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.FullName



class Trainer(models.Model):
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    salary = models.IntegerField()
    def __str__(self):
        return self.name
    

class MenbershipPlan(models.Model):
    plan = models.CharField(max_length=185)
    price = models.IntegerField()
    def __str__(self):
        return str(self.plan)
    

    