from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from project import settings


class Command(BaseCommand):
    help = 'Test'

    def handle(self, *args, **options):
        subject = 'Custom Command Test Email'
        message = 'Muvvafiqiyatli bajarildi.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['orzimurodyusupov2004@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list)
            self.stdout.write(self.style.SUCCESS('Emailga yuborildi!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error sending email: {e}'))
