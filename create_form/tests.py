from django.test import TestCase
from datetime import datetime
from django.contrib.auth.models import User

import create_form.models as CreateForm

class StatusTest(TestCase):
    def instanceTest(self):
        status = CreateForm.Status(name = "open")
        self.assertTrue(isinstance(status.id, int))
        self.assertTrue(isinstance(status.name, str))

class CategoryTest(TestCase):
    def instanceTest(self):
        category = CreateForm.Category(name = "Mountains")
        self.assertTrue(isinstance(category.id, int))
        self.assertTrue(isinstance(category.name, str))

# class FileTypeTest(TestCase):
#     def instanceTest(self):
#         fileType = CreateForm.FileType(id = 1, type = "txt")
#         self.assertTrue(isinstance(fileType.id, int))
#         self.assertTrue(isinstance(fileType.type, str))
#
# class FilesTest(TestCase):
#     def instanceTest(self):
#         pass
#         ## linijka nizej sie jebie
#         files = CreateForm.Files(id = 1, fileType = 1, event = 1)
#         self.assertTrue(isinstance(files.id, int))
#         self.assertTrue(isinstance(files.fileType, int))
#         self.assertTrue(isinstance(files.event, int))
#
# class ScheduleTest(TestCase):
#     def instanceTest(self):
#         pass
#         ## linijka lizej sie jebie
#         schedule = CreateForm.Schedule(id = 1, name = "Test", startDate = datetime.now(), endDate = datetime.now(), description = "Description", event = 1)
#         self.assertTrue(isinstance(schedule.id, int))
#         self.assertTrue(isinstance(schedule.name, str))
#         self.assertTrue(isinstance(schedule.startDate, datetime))
#         self.assertTrue(isinstance(schedule.enddate, datetime))
#         self.assertTrue(isinstance(schedule.Description, str))
#         self.assertTrue(isinstance(schedule.event, int))
#
# class GiftTest(TestCase):
#     def instanceTest(self):
#         pass
#         ## linijka lizej sie jebie
#         gift = CreateForm.Gift(id = 1, event = 1, name = "Gift", description = "Description", amount = 1)
#         self.assertTrue(isinstance(gift.id, int))
#         self.assertTrue(isinstance(gift.event, int))
#         self.assertTrue(isinstance(gift.name, str))
#         self.assertTrue(isinstance(gift.description, str))
#         self.assertTrue(isinstance(gift.amount, int))
#
# class OwnFieldTest(TestCase):
#     def instanceTest(self):
#         pass
#         ## linijka lizej sie jebie
#         ownField = CreateForm.OwnField(id = 1, title = "Title", description = "Description", type = "txt", event = 1)
#         self.assertTrue(isinstance(ownField.id, int))
#         self.assertTrue(isinstance(ownField.title, str))
#         self.assertTrue(isinstance(ownField.description, str))
#         self.assertTrue(isinstance(ownField.type, str))
#         self.assertTrue(isinstance(ownField.event, int))
#
# class EventTest(TestCase):
#     def strFieldsTest(self):
#         event1 = CreateForm.Event(title = "Title", location = "Krakow", description = "Description")
#         self.assertTrue(isinstance(event1.title, str))
#         self.assertTrue(isinstance(event1.location, str))
#         self.assertTrue(isinstance(event1.description, str))
#
#     def numFieldsTest(self):
#         event2 = CreateForm.Event(maxParticipants = 1, price = 2.5)
#         self.assertTrue(isinstance(event2.maxParticipants, int))
#         self.assertTrue(isinstance(event2.price, float))
#
#     def datetimeFieldsTest(self):
#         event3 = CreateForm.Event(startDate = datetime.now(), endDate = datetime.now())
#         self.assertTrue(isinstance(event3.startDate, datetime))
#         self.assertTrue(isinstance(event3.endDate, datetime))
#
#     def complexInstanceTest(self):
#         user_1 = User.objects.create_user("test")
#         event_status_1 = M.Event_status(event_status_name="open")
#         event_status_1.save()
#         event_category_1 = M.Event_category(event_category_name="Mountains")
#         event_category_1.save()
#         event_4 = M.Event(event_id=1, user_id=User.objects.get(id = user_1.id), event_status_id=event_status_1, event_category_id=event_category_1, title="Title",
#                          max_participants=1, price=2.5, location="Krakow", start_date=datetime.now(),
#                          end_date=datetime.now(), description="Description")
#         event_4.save()
#         print "tu jest event status id: " + str(event_4.event_status_id.event_status_id) + " /;"