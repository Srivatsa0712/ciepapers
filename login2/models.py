from distutils.command.upload import upload
from django.db import models

# Create your models here.

class faculty(models.Model):
    faculty_id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=100,unique=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField(max_length=200)
    Password=models.CharField(max_length=100)

    def __str__(self):
        return self.FirstName+'  '+ self.LastName
# class images(models.Model):
    # img=models.ImageField(upload_to='media\login1\images')

class admin1(models.Model):
    Username=models.CharField(max_length=100,unique=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    faculty_id=models.ForeignKey(faculty,on_delete=models.CASCADE)

    def __str__(self):
        return self.FirstName+'   '+ self.LastName

class course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=100)
    faculty_id=models.ForeignKey(faculty,on_delete=models.CASCADE)
    cie1=models.ImageField()
    cie2=models.ImageField(blank=True)
    cie3=models.ImageField(blank= True)

class committee(models.Model):
    committee_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(faculty,on_delete=models.CASCADE)
    course_id = models.ForeignKey(course,on_delete=models.CASCADE)
    # EMF=models.CharField(max_length=100)
    # cie_1 = models.TextField()
    # cie_2 = models.TextField()
    # cie_3 = models.TextField()
    


class users(models.Model):
    Username=models.CharField(unique=True,max_length=100)
    Password=models.CharField(max_length=100)

    def __str__(self):
        return self.Username

class committee1(models.Model):
    Username=models.CharField(unique=True,max_length=100)
    Password=models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.Username

class subjects(models.Model):
    name1=models.CharField(max_length=100,blank=True)
    cie1=models.ImageField(blank=True,null=True,upload_to="images/")
    cie2=models.ImageField(blank=True,null=True,upload_to="images/")
    cie3= models.ImageField(blank=True,null=True,upload_to="images/")
    name2=models.CharField(max_length=100,blank=True)
    cieI=models.ImageField(blank=True,null=True,upload_to="images/")
    cieII=models.ImageField(blank=True,null=True,upload_to="images/")
    cieIII=models.ImageField(blank=True,null=True,upload_to="images/")
    name3=models.CharField(max_length=100,blank=True)
    ciei=models.ImageField(blank=True,null=True,upload_to="images/")
    cieii=models.ImageField(blank=True,null=True,upload_to="images/")
    cieiii=models.ImageField(blank=True,null=True,upload_to="images/")
    name4=models.CharField(max_length=100,blank=True)
    cie01=models.ImageField(blank=True,null=True,upload_to="images/")
    cie02=models.ImageField(blank=True,null=True,upload_to="images/")
    cie03=models.ImageField(blank=True,null=True,upload_to="images/")
    name5=models.CharField(max_length=100,blank=True)
    cie001=models.ImageField(blank=True,null=True,upload_to="images/")
    cie002=models.ImageField(blank=True,null=True,upload_to="images/")
    cie003=models.ImageField(blank=True,null=True,upload_to="images/")

    
    