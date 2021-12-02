from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, **options):
        # now do the things that you want with your models here
        from api.core.models import Major, Semester, User, UserProfile
        from api.event.models import Event

        Major.objects.all().delete()
        Semester.objects.all().delete()
        User.objects.all().delete()
        UserProfile.objects.all().delete()

        major1 = Major.objects.create(major="Computer Science")
        major2 = Major.objects.create(major="Data Science")
        major3 = Major.objects.create(major="Material Science")

        sem1 = Semester.objects.create(term="spring", year=2020)
        sem2 = Semester.objects.create(term="fall", year=2020)

        user1 = User.objects.create_user(
            berkeley_email="tester1@berkeley.edu",
            password= "tester1",
            first_name= "NAME",
            last_name= "SWAN",
            full_name= "테스터",
            country= "Korea",
            gender= "MAL",
            birth= "2021-08-03",
            majors= [major1.pk],
            minors= [major2.pk],

        )
        user2 = User.objects.create_user(
            berkeley_email="tester2@berkeley.edu",
            password="tester1",
            first_name="NAME",
            last_name="SWAN",
            full_name="테스터",
            country="Korea",
            gender="MAL",
            birth="2021-08-03",
            majors=[major1.pk],
            minors=[major2.pk]
        )
        userprofile1 = UserProfile.objects.create(
            user=user1,
            semester=sem2,
            points=0,
            role="BOA",
            paid_membership_fee=True
        )

        Event.objects.create(
            name="Name of the event",
            event_type="gm",
            points=50,
            owner=userprofile1,
            semester=sem2
        )