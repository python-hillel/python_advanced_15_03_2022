from datetime import timedelta, time, datetime

from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware

from quiz.models import Result

today_start = make_aware(datetime.combine(timezone.now(), time()))
today_end = make_aware(datetime.combine(timezone.now() + timedelta(1), time()))


class Command(BaseCommand):
    help = "Send Today's Report to Admins"

    def handle(self, *args, **options):
        results = Result.objects.filter(update_timestamp__range=(today_start, today_end), state=1)

        if results:
            message = ""

            for result in results:
                message += f"{result} \n"

            subject = f"Report from {today_start.strftime('%Y-%m-%d')} " \
                      f"to {today_end.strftime('%Y-%m-%d')}"

            mail_admins(subject=subject, message=message, html_message=None)

            self.stdout.write("E-mail Report was sent.")
        else:
            self.stdout.write("No orders confirmed today.")
