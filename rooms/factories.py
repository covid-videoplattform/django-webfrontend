import factory
from django.contrib.auth import models as auth_models
from . import models


class StaffMemberFactory(factory.Factory):
    class Meta:
        model = models.StaffMember

    name = factory.Faker('name')


# Another, different, factory for the same object
class AppointmentFactory(factory.Factory):
    class Meta:
        model = models.Appointment

    name = factory.Faker('sentence', nb_words=2)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = auth_models.User

    username = factory.Sequence(lambda n: "user_%03d" % n)
    password = factory.PostGenerationMethodCall('set_password', 'secret')

    is_superuser = False
    is_staff = True
    is_active = True
