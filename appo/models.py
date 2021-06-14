from django.db import models


class Reporter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
       
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    headline=models.CharField(max_length=30)
    pub_date=models.DateField()
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)
        
    
    
    
    
    
