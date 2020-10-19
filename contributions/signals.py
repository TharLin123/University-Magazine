import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contribution
from users.models import Student,Marketing_Coordinator
from datetime import timedelta

username = 'tharlinhtet.mhs@gmail.com'
password = 'Tharlin123$'

def send_mail(subject='Email Subject', body = 'How you doing?', from_email = 
'University Magazine<username>',to_email = None, html = None):
    assert isinstance(to_email,list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ",".join(to_email)
    msg['Subject'] = subject

    txt_part = MIMEText(body, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText(html,'html')
        msg.attach(html_part)
        
    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_email,msg_str)
    server.quit() 

@receiver(post_save,sender=Contribution)
def create_profile(sender,instance,created,**kwargs):
    post = Contribution.objects.all().first()
    url = f"""http://127.0.0.1:8000/contributions/detail/{post.id}"""
    receiver = []
    receiver_model = Marketing_Coordinator.objects.filter(faculty=post.author.faculty)

    for receiver_models in receiver_model:
        email = receiver_models.email
        receiver.append(email)
    date = post.date_posted + timedelta(days = 14)
    subject = 'New contribution alert!!'
    html = f"""<p><h3>{post.author.name}</h3> posted a contribution with the title 
    <h3>'{post.title}'</h3> on {post.author.faculty.get_name_display()} newsfeed. <a href='{url}'>Click</a> here to read. Don't forget 
    to make a comment within 14 days which is until <h3>{date}.</h3></p>"""

    if created:
        send_mail(subject=subject,html=html,to_email=receiver)
        
        


