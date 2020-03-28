import factory
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
