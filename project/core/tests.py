import os
import sys
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
from django.core.management import execute_from_command_line
settings.DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME':':memory:', 'SUPPORTS_TRANSACTIONS': 'False', 'TEST_NAME': os.path.join(project_path, 'test_sqlite.db'),}}
from django.core.management import call_command
import django
django.setup()
#call_command('syncdb', interactive=True)

from core.score import compute_scores
from core.models import Activity, TimeUnit
from mock import Mock, patch
from django.test import TestCase


def mock_pereare():
    raise Exception


class MyTest(TestCase):
    def setUp(self):
        from django.core.management import call_command
        django.setup()
        #call_command('syncdb', interactive=True)

    @patch('core.score.some_pereare', mock_pereare)
    def test_activity_created_anyway(self):
        compute_scores()
        activity = Activity.objects.get(name='django coding')
        print activity

    def tearDown(self):
       pass



'''
from unittest import TestCase
from mock import Mock, patch
from score import compute_scores
from django.core.management import call_command
from django.db.models import loading
loading.cache.loaded = False
call_command('syncdb', verbosity=0)

def mock_pereare():
    raise Exception

mock_objects = Mock(get=Mock, get_or_create=Mock)

class MockActivity(Mock):
    objects = mock_objects


class MockTimeUnit(Mock):
    objects = mock_objects


class TimeUnitTests(TestCase):
    def setUp(self):
        pass

    @patch('models.Activity', MockActivity)
    @patch('models.TimeUnit', MockTimeUnit)
    @patch('score.some_pereare', mock_pereare)
    def test_activity_created_anyway(self):
        compute_scores()

    def tearDown(self):
        pass
'''