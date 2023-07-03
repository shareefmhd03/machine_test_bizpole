
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings

def send_email(subject, message, recipient):#third party service

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] =settings.EMAIL_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    sender = {"name":"Tester","email":"Noreply@bizpole.com"}
    html_content = message
    to = [{"email":recipient,"name":"Jane Doe"}]
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
    {"success":True}





User = get_user_model()


class CustomAuthBackend(ModelBackend):
    def authenticate(self, username,password):
        try:
            user = User.objects.filter(username=username).first()
        except User.DoesNotExist:
            return None
        if user != None:
            if user.check_password(password):
                return user
            else:
                return None
        else:
            return None
            