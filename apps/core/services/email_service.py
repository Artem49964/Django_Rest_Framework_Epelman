import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class EmailService:
    @staticmethod
    def __send_email(to: str, template_name: str, context: dict, subject=''):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_NAME'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def test_email(cls):
        cls.__send_email('artem.epelman@gmail.com', 'test_email.html', {}, 'Hello')