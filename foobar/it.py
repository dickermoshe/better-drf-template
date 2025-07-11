import os

import django
from django.urls import resolve

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foobar.settings")
django.setup()
resolve("/health/")
