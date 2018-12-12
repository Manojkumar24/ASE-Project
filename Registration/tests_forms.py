# from django.test import TestCase
# from Registration.forms import MyForm
#
# class MyTests(TestCase):
#
#     data = {
#         username:'username',first_name:'neeharika',last_name:'devi',email='neeharika149@gmail.com',password='gyhgy'
#         }
#
#     def test_valid_form(self):
#         form = SaveForm(self.data)
#         self.assertTrue(form.is_valid())
#
#     def test_invalid_url(self):
#         my_data = copy(self.data)
#         my_data['url'] = 'invalid url'
#         form = SaveForm(my_data)
#
#         self.assertFalse(form.is_valid())
#
#     def test_required_fields(self):
#         for field in ('title', 'url', 'tags'):
#             with self.subTest(field=field):
#                 my_data = copy(self.data)
#                 my_data[field] = ''
#                 form = SaveForm(my_data)
#
#                 self.assertFalse(form.is_valid())
#
#     def test_cleaning_tags(self):
#         form = SaveForm({'tags': 'one, two'})
#         form.is_valid()
#
#         tags = form.cleaned_data['tags']
#         self.assertIsInstance(tags, list)
#         self.assertEqual(len(tags), 2)
#         self.assertEqual(tags[1], 'two')
#
#     def test_cleaning_description(self):
#         form = SaveForm({'description': ''})
#         form.is_valid()
#
#         description = form.cleaned_data['description']
#         self.assertIsNone(description)
