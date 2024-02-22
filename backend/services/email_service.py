import smtplib

from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import config as settings

class Mailer:
    '''
        Mailer class to send emails
    '''

    def send_client_email(self, email_parameters: dict):
        '''
            Send email
        '''

        server = smtplib.SMTP_SSL(settings.MAIL_HOST, 465)
        server.login(settings.MAIL_FROM_ADDRESS, settings.MAIL_PASSWORD)
        
        msg = MIMEMultipart()
        msg['Subject'] = email_parameters["subject"]
        msg['From'] = formataddr(('Sujeet Singh', settings.MAIL_FROM_ADDRESS))

        client_email = email_parameters.get('client_email', [])
        msg['To'] = ', '.join(client_email)

        html = email_parameters['content']
        part2 = MIMEText(html.encode('utf-8'), 'html', 'utf-8')
        msg.attach(part2)

        images = email_parameters.get('images', [])

        if images:
            for each_image in images:
                image_path = each_image['path']
                cid = each_image['cid']
                
                with open(image_path, mode='rb') as f:
                    image = MIMEImage(f.read())
                    image.add_header('Content-ID', f"<{cid}>")
                    msg.attach(image)


        server.sendmail(settings.MAIL_FROM_ADDRESS, client_email + [settings.MAIL_BCC], msg.as_string())
