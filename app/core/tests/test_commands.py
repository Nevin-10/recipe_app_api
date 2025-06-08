"""

Testing custom django commands
TDD
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check') #Providing path directly, Command.check provided by BaseCommand

class CommandTests(SimpleTestCase):
    """Testing Commands"""

    def test_wait_for_db_ready(self, patched_check):
        """If database ready, we are testing what wait_for_db does(MOCK BEHAVIOUR)"""

        patched_check.return_value=True
        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])

