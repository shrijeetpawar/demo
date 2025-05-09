import csv
from django.core.management.base import BaseCommand
from banks.models import Bank, Branch

class Command(BaseCommand):
    help = 'Loads bank data from CSV'

    def handle(self, *args, **kwargs):
        # Load Banks
        with open('bank.csv') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                Bank.objects.get_or_create(id=row[0], name=row[1])

        # Load Branches
        with open('branch.csv') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                bank = Bank.objects.get(id=row[1])
                Branch.objects.get_or_create(
                    ifsc=row[0],
                    defaults={
                        'branch': row[2],
                        'address': row[3],
                        'city': row[4],
                        'district': row[5],
                        'state': row[6],
                        'bank': bank
                    }
                )