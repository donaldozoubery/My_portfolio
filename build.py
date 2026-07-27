import os
import django
from django.core.management import call_command
from django.contrib.staticfiles.management.commands.collectstatic import Command as CollectstaticCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

print('Running collectstatic...')
call_command(CollectstaticCommand(), '--noinput', '--clear')
print('Running migrate...')
call_command('migrate', '--noinput')
print('Build completed.')
