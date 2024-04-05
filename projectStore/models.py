from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your models here.
class SignupForm(UserCreationForm):
       class Meta:
        model = User
        fields = ['username','password1','password2']

class LoginForm(forms.Form):
       username = forms.CharField()
       password = forms.CharField(widget=forms.PasswordInput)


class Category(models.Model):
    name = models.CharField(max_length = 150,blank=True,null=True)
    def __str__(self) :
      return self.name
    
class Product(models.Model):
    name = models.CharField(max_length = 150,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField( upload_to='projectStore/static/images', default=0)
    price = models.FloatField(blank=True,null=True)
    company = models.CharField(max_length = 150,blank=True,null=True)
    digitalItems =  models.BooleanField(null=True)
    offerprice= models.IntegerField(null=True,blank=True)
    
    def __str__(self) :
        return self.name

    @staticmethod 
    def get_category_Info(get_id):
                     
                   if get_id:
                         return Product.objects.filter(category=get_id)
                   else:
                         return Product.objects.all()


     
class Customer(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
     name = models.CharField(max_length=150,null=True)
     email = models.CharField(max_length=200,null=True)

     def __str__(self) :
          return self.name 
    
class Order(models.Model):
     customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
     ordered_time = models.DateTimeField(auto_now_add=True)
     complete = models.BooleanField(null=True,blank=True)
     transction_id = models.CharField(max_length=150,null=True)
     def __str__(self):
          return str(self.id)
     
     @property
     def get_cart_total(self):
         orderitems = self.orderitem_set.all()
         total = sum([item.get_total for item in orderitems])
         return total
     @property
     def get_cart_items(self):
         orderitems = self.orderitem_set.all()
         total = sum([item.quantity  for item in orderitems])
         return total  
     
class OrderedItem(models.Model):
     product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
     order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
     quantity = models.IntegerField(default=0,null=True,blank=True)
     items_date_added = models.DateTimeField(auto_now_add=True)
     
    
     @property
     def get_total(self):
          total = self.product.price*self.quantity
          return total

     def __str__(self) :
          return str(self.product)
     
class DeliveryAddress(models.Model):
     customer= models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
     order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
     address = models.CharField(max_length=150,null=True)
     state  = models.CharField(max_length=150,null=True)
     city = models.CharField(max_length=150,null=True)
     pinCode = models.CharField(max_length=10)
     items_date_added = models.DateTimeField(auto_now_add=True)


class NewCollection(models.Model):
    name = models.CharField(max_length = 150,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField( upload_to='projectStore/static/images', default=0)
    price = models.FloatField(blank=True,null=True)
    company = models.CharField(max_length = 150,blank=True,null=True)
    digitalItems =  models.BooleanField(null=True)
    
    
    def __str__(self) :
        return self.name

class WomenCollection(models.Model):
    name = models.CharField(max_length = 150,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField( upload_to='projectStore/static/images', default=0)
    price = models.FloatField(blank=True,null=True)
    company = models.CharField(max_length = 150,blank=True,null=True)
    digitalItems =  models.BooleanField(null=True)
    
    
    def __str__(self) :
        return self.name
    
class MenCollection(models.Model):
    name = models.CharField(max_length = 150,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField( upload_to='projectStore/static/images', default=0)
    price = models.FloatField(blank=True,null=True)
    company = models.CharField(max_length = 150,blank=True,null=True)
    digitalItems =  models.BooleanField(null=True)
    
    
    def __str__(self) :
        return self.name
    
class KidsCollection(models.Model):
    name = models.CharField(max_length = 150,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField( upload_to='projectStore/static/images', default=0)
    price = models.FloatField(blank=True,null=True)
    company = models.CharField(max_length = 150,blank=True,null=True)
    digitalItems =  models.BooleanField(null=True)
    
    
    def __str__(self) :
        return self.name

class MotorSportCollection(models.Model):
    name = models.CharField(max_length = 150,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField( upload_to='projectStore/static/images', default=0)
    price = models.FloatField(blank=True,null=True)
    company = models.CharField(max_length = 150,blank=True,null=True)
    digitalItems =  models.BooleanField(null=True)
    
    
    def __str__(self) :
        return self.name

class SportCollection(models.Model):
    name = models.CharField(max_length = 150,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField( upload_to='projectStore/static/images', default=0)
    price = models.FloatField(blank=True,null=True)
    company = models.CharField(max_length = 150,blank=True,null=True)
    digitalItems =  models.BooleanField(null=True)
    
    
    def __str__(self) :
        return self.name

