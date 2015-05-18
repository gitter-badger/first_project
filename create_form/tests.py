from django.test import TestCase
from datetime import datetime
from django.contrib.auth.models import User

import create_form.models as CreateForm


class ComplexTestsInitializer():
    @staticmethod
    def initialize_event_entity():
        user_1 = User.objects.create_user("test")
        event_status_1 = CreateForm.Status(name="open")
        event_status_1.save()
        event_category_1 = CreateForm.Category(name="Mountains")
        event_category_1.save()
        event_4 = CreateForm.Event(id=1, user=User.objects.get(id=user_1.id), status=event_status_1, category=event_category_1,
                                   title="Title",
                                   max_participants=1, price=2.5, location="Krakow", startDate=datetime.now(),
                                   endDate=datetime.now(), description="Description")
        event_4.save()

    @staticmethod
    def initialize_file_type_entity():
        fileType = CreateForm.FileType(id=1, type="txt")
        fileType.save()


class StatusTest(TestCase):
    def instance_test(self):
        status = CreateForm.Status(id=1, name="open")
        self.assertTrue(isinstance(status.id, int))
        self.assertTrue(isinstance(status.name, str))


class CategoryTest(TestCase):
    def instance_test(self):
        category = CreateForm.Category(id=1, name="Mountains")
        self.assertTrue(isinstance(category.id, int))
        self.assertTrue(isinstance(category.name, str))


class FileTypeTest(TestCase):
    def instance_test(self):
        file_type = CreateForm.FileType(id=1, type="txt")
        self.assertTrue(isinstance(file_type.id, int))
        self.assertTrue(isinstance(file_type.type, str))


class FilesTest(TestCase):
    def instance_test(self):
        ComplexTestsInitializer.InitializeEventEntity()
        ComplexTestsInitializer.InitializeFileTypeEntity()
        files = CreateForm.Files(id=1, file_type=CreateForm.FileType.objects.get(id=1), event=CreateForm.Event.objects.get(id=1))
        self.assertTrue(isinstance(files.id, int))
        self.assertTrue(isinstance(files.file_type, CreateForm.FileType))
        self.assertTrue(isinstance(files.event, CreateForm.Event))


class ScheduleTest(TestCase):
    def instance_test(self):
        ComplexTestsInitializer.InitializeEventEntity()
        schedule = CreateForm.Schedule(id=1, name="Test", start_date=datetime.now(), end_date=datetime.now(), description="Description",
                                       event=CreateForm.Event.objects.get(id=1))
        self.assertTrue(isinstance(schedule.id, int))
        self.assertTrue(isinstance(schedule.name, str))
        self.assertTrue(isinstance(schedule.start_date, datetime))
        self.assertTrue(isinstance(schedule.end_date, datetime))
        self.assertTrue(isinstance(schedule.description, str))
        self.assertTrue(isinstance(schedule.event, CreateForm.Event))


class GiftTest(TestCase):
    def instance_test(self):
        ComplexTestsInitializer.InitializeEventEntity()
        gift = CreateForm.Gift(id=1, event=CreateForm.Event.objects.get(id=1), name="Gift", description="Description", amount=1)
        self.assertTrue(isinstance(gift.id, int))
        self.assertTrue(isinstance(gift.event, CreateForm.Event))
        self.assertTrue(isinstance(gift.name, str))
        self.assertTrue(isinstance(gift.description, str))
        self.assertTrue(isinstance(gift.amount, int))


class OwnFieldTest(TestCase):
    def instance_test(self):
        ComplexTestsInitializer.InitializeEventEntity()
        own_field = CreateForm.OwnField(id=1, title="Title", description="Description", type="txt", event=CreateForm.Event.objects.get(id=1))
        self.assertTrue(isinstance(own_field.id, int))
        self.assertTrue(isinstance(own_field.title, str))
        self.assertTrue(isinstance(own_field.description, str))
        self.assertTrue(isinstance(own_field.type, str))
        self.assertTrue(isinstance(own_field.event, CreateForm.Event))


class EventTest(TestCase):
    def str_fields_test(self):
        event_1 = CreateForm.Event(title="Title", location="Krakow", description="Description")
        self.assertTrue(isinstance(event_1.title, str))
        self.assertTrue(isinstance(event_1.location, str))
        self.assertTrue(isinstance(event_1.description, str))

    def num_fields_test(self):
        event_2 = CreateForm.Event(max_participants=1, price=2.5)
        self.assertTrue(isinstance(event_2.max_participants, int))
        self.assertTrue(isinstance(event_2.price, float))

    def datetime_fields_test(self):
        event_3 = CreateForm.Event(start_date=datetime.now(), end_date=datetime.now())
        self.assertTrue(isinstance(event_3.start_date, datetime))
        self.assertTrue(isinstance(event_3.end_date, datetime))

    def complex_instance_test(self):
        ComplexTestsInitializer.InitializeEventEntity()
        event_4 = CreateForm.Event(id=1, user=User.objects.get(id=1), status=CreateForm.Status.objects.get(name="open"),
                                   category=CreateForm.Category.objects.get(name="Mountains"), title="Title",
                                   max_participants=1, price=2.5, location="Krakow", start_date=datetime.now(),
                                   end_date=datetime.now(), description="Description")
        event_4.save()

# print "tu jest event status id: " + str(event_4.event_status_id.event_status_id) + " /;"
if __name__ == '__main__':
    TestCase.main()