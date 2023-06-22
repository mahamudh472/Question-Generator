from django.db import models

# Create your models here.
class Short_question(models.Model):
    ques = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.ques
    
class Comp_question(models.Model):
    ques = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.ques