from django.core.management.base import BaseCommand
from blog.models import Blog
from django.core.management import call_command


class Command(BaseCommand):
    help = "delete all data from database and fill some data"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Blog.objects.all().delete()
        call_command("loaddata", "blog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
