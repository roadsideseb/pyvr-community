# -*- coding: utf-8 -*-
import os
import sys

sys.stdout = sys.stderr
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'community.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
