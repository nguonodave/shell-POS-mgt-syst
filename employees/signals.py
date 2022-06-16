from django.contrib.auth.models import User
from . models import Employee

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def createEmployee(sender, instance, created, **kwargs):
    if created:        
        user = instance
        employee = Employee.objects.update_or_create(
            user=user,
            name=f'{user.first_name} {user.last_name}',
            email=user.email,            
        )        


@receiver(post_delete, sender=Employee)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()