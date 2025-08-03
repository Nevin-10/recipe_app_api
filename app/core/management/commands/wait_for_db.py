"""Django commands to wait for database to be availabe completely"""
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write("Waiting for database..")
        # BaseCommand Methods self.stdout.write()
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                # self.check() is method of BaseCommand
                db_up = True
                """When Database is Available True
                  and Break while else,keep on doing."""
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database Unavailabe.. Waiting one second')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
