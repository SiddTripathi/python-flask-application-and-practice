import os
import jinja2
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from dotenv import load_dotenv



load_dotenv()


DOMAIN = os.getenv("MAILGUN_DOMAIN")

template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)
def render_tempalte(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)

def send_simple_message(to,subject,html):
    message = Mail(
        from_email='siddharth.asbwork@gmail.com',
        to_emails=to,
        subject=subject,
        html_content=html)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        # sg.set_sendgrid_data_residency("eu")
        # uncomment the above line if you are sending mail using a regional EU subuser
        response = sg.send(message)
        print(response.status_code)
        print(response.html)
        print(response.headers)
    except Exception as e:
        print(str(e))
                        

def send_user_registration_email(email,username):
    return send_simple_message(
        email,
        "Successfully signed up",
        render_tempalte("email/action.html")

    )