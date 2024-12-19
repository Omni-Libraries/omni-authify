import os
from dotenv import load_dotenv

load_dotenv()



OMNI_AUTHIFY = {
    'PROVIDERS':{
        'facebook':{
            'client_id':os.getenv('FACEBOOK_CLIENT_ID'),
            'client_secret':os.getenv('FACEBOOK_CLIENT_SECRET'),
            'redirect_uri':os.getenv('FACEBOOK_REDIRECT_URI'),
            'state':os.getenv('FACEBOOK_STATE'), # optional
            'scope':os.getenv('FACEBOOK_SCOPE'),  # by default | add other FB app permissions you have!
            'fields':os.getenv('FACEBOOK_FIELDS')
        },
        'github':{
            'client_id':os.getenv('GITHUB_CLIENT_ID'),
            'client_secret':os.getenv('GITHUB_CLIENT_SECRET'),
            'redirect_uri':os.getenv('GITHUB_CLIENT_REDIRECT_URI'),
            'scope':os.getenv('GITHUB_CLIENT_SCOPE'),
        },
        'google':{
            'client_id':os.getenv('GOOGLE_CLIENT_ID'),
            'client_secret':os.getenv('GOOGLE_CLIENT_SECRET'),
            'redirect_uri':os.getenv('GOOGLE_REDIRECT_URI'),
            'state':os.getenv('GOOGLE_STATE'), # optional
            'scope':os.getenv('GOOGLE_SCOPE')
        },
        'linkedin':{
            'client_id':os.getenv('LINKEDIN_CLIENT_ID'),
            'client_secret':os.getenv('LINKEDIN_CLIENT_SECRET'),
            'redirect_uri':os.getenv('LINKEDIN_REDIRECT_URI'),
            'scope':os.getenv('LINKEDIN_SCOPE')
        }

        # Add other providers here if needed
    }
}