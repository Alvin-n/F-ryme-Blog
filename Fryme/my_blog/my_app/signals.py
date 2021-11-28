from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PostModel
from django.core.mail import send_mail

print('Signal is ready')
 
@receiver(post_save, sender=PostModel)
def mail_sender(sender, instance, created, **kwargs):
    if created:
        print("creation success")
        send_mail(
            'PostModel',
            'blah blah',
            'nasibov.alvin@gmail.com',
            ['nasibov.elvin412@gmail.com'],
            fail_silently=False)