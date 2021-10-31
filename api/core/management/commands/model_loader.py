from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, **options):
        # now do the things that you want with your models here
        from api.core.models import Major, Semester, User

        Major.objects.create(major="Computer Science")
        Major.objects.create(major="Data Science")
        Major.objects.create(major="Material Science")

        Semester.objects.create(term="spring", year=2020)
        Semester.objects.create(term="fall", year=2020)

        User.objects.create_user(
            berkeley_email="tester1@berkeley.edu",
            password= "tester1",
            first_name= "NAME",
            last_name= "SWAN",
            full_name= "테스터",
            country= "Korea",
            gender= "MAL",
            birth= "2021-08-03",
            majors= [1],
            minors= [2]
        )
        User.objects.create_user(
            berkeley_email="tester2@berkeley.edu",
            password="tester1",
            first_name="NAME",
            last_name="SWAN",
            full_name="테스터",
            country="Korea",
            gender="MAL",
            birth="2021-08-03",
            majors=[1],
            minors=[2]
        )