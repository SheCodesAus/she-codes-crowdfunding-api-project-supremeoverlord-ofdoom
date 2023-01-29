from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() #give me the user model that you set in settings

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True) #always use auto_now_add=True with date_created = models.DateTimeField
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='owner_projects'
        )
    
    # liked_by = models.ManyToManyField(
    #     User,
    #     related_name='liked_projects'
    # )
    @property
    def total(self):
        return self.pledges.aggregate(sum=models.Sum('amount'))['sum']

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="pledges")
    supporter_public = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # using CASCADE so if you delete the project, then it will delete the pledges
        related_name='supporter_public_pledges')
    supporter_private= models.ForeignKey(
    User,
    on_delete=models.CASCADE,  # using CASCADE so if you delete the project, then it will delete the pledges
    related_name='supporter_private_pledges'
    )

