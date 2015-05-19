from django.test import TestCase, Client

# Create your tests here.
from create_form.models import OwnField
import create_form.models as CreateForm
from create_form.tests import ComplexTestsInitializer
from form_response.models import RegistrationInstance, FormFieldInstance, RegistrationInstanceGifts


class RegistrationInstanceTest(TestCase):
    def test_instance(self):
        ComplexTestsInitializer.initialize_event_entity()
        gift = CreateForm.Gift(id=1, event=CreateForm.Event.objects.get(id=1), name="Gift", description="Description", amount=1)
        gift.save()
        registration_instance = RegistrationInstance(id=1, event_assessment=3.0, event=CreateForm.Event.objects.get(id=1))
        registration_instance.save()
        reg_in_gift = RegistrationInstanceGifts(registration_instance=RegistrationInstance.objects.get(id=1),
                                                gift=CreateForm.Gift.objects.get(id=1), amount=5)
        reg_in_gift.save()
        registration_instance = RegistrationInstance(id=1, event_assessment=3.0, event=CreateForm.Event.objects.get(id=1))
        self.assertEqual(RegistrationInstanceGifts.objects.get(registration_instance=registration_instance), reg_in_gift)
        self.assertEqual(RegistrationInstanceGifts.objects.get(gift=gift), reg_in_gift)
        self.assertTrue(isinstance(registration_instance.id, int))
        self.assertTrue(isinstance(registration_instance.event_assessment, float))
        self.assertTrue(isinstance(registration_instance.event, CreateForm.Event))
        self.assertTrue(isinstance(registration_instance.event_fraudulent, bool))
        self.assertTrue(isinstance(registration_instance.registration_confirmed, bool))


class RegistrationInstanceGiftsTest(TestCase):
    def test_instance(self):
        ComplexTestsInitializer.initialize_event_entity()
        gift = CreateForm.Gift(id=1, event=CreateForm.Event.objects.get(id=1), name="Gift", description="Description", amount=1)
        gift.save()
        registration_instance = RegistrationInstance(id=1, event_assessment=3.0, event=CreateForm.Event.objects.get(id=1))
        registration_instance.save()
        reg_in_gift = RegistrationInstanceGifts(registration_instance=RegistrationInstance.objects.get(id=1),
                                                gift=CreateForm.Gift.objects.get(id=1), amount=5)
        self.assertTrue(isinstance(reg_in_gift.amount, int))
        self.assertTrue(isinstance(reg_in_gift.registration_instance, RegistrationInstance))
        self.assertTrue(isinstance(reg_in_gift.gift, CreateForm.Gift))


class FormFieldInstanceTest(TestCase):
    def test_instance(self):
        ComplexTestsInitializer.initialize_event_entity()
        own_field = OwnField(id=1, title="Title", description="Description", field_type="txt", event=CreateForm.Event.objects.get(id=1))
        own_field.save()
        registration_instance = RegistrationInstance(id=1, event_assessment=3.0, event=CreateForm.Event.objects.get(id=1))
        registration_instance.save()
        form_field_instance = FormFieldInstance(id=1, form_field=OwnField.objects.get(id=1), value='terefere', registration_instance=RegistrationInstance.objects.get(id=1))
        self.assertTrue(isinstance(form_field_instance.id, int))
        self.assertTrue(isinstance(form_field_instance.form_field, OwnField))
        self.assertTrue(isinstance(form_field_instance.value, str))
        self.assertTrue(isinstance(form_field_instance.registration_instance, RegistrationInstance))


if __name__ == '__main__':
    TestCase.main()