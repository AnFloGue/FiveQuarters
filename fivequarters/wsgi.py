import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fivequarters.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    print(f"An error occurred: {e}")