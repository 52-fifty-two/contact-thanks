import threading

from services.email_service import Mailer

from jinja2 import Environment, FileSystemLoader

env = Environment()
env.loader = FileSystemLoader('services/templates/thanks')
template = env.get_template("thanks.html")

class MainService:
    '''
        Main Service class
    '''

    SUBJECT = 'Thanks for connecting with me!'

    def __init__(self):
        pass
    
    def get_content_images(self):
        '''
            Get content images
        '''

        IMAGES = [
            {
                'path': 'services/templates/thanks/images/facebook2x.png',
                'cid': 'facebook_icon'
            },
            {
                'path': 'services/templates/thanks/images/instagram2x.png',
                'cid': 'instagram_icon'
            },
            {
                'path': 'services/templates/thanks/images/linkedin2x.png',
                'cid': 'linkedin_icon'
            },
            {
                'path': 'services/templates/thanks/images/twitter2x.png',
                'cid': 'twitter_icon'
            },
            {
                'path': 'services/templates/thanks/images/website2x.png',
                'cid': 'website_icon'
            }
        ]

        return IMAGES

    def get_email_subject(self):
        '''
            Get email subject
        '''

        subject = MainService.SUBJECT
        return subject

    def get_email_template_content(self, username: str):
        '''
            Get email template content
        '''

        return template.render(username=username)

    def process_sending_email(self, email_parameters: dict):
        '''
            Setup email parameters and send email
        '''

        email_parameters = {
            'client_email': [email_parameters['email']],
            'images': self.get_content_images(),
            'subject': self.get_email_subject(),
            'content': self.get_email_template_content(username=email_parameters['username'])
        }

        print('Run the thread to send the email!')
        email_thread = threading.Thread(target=Mailer().send_client_email, args=(email_parameters,))
        email_thread.start()
