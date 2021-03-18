from django.test import TestCase, SimpleTestCase, override_settings


@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):

    def test_handler_renders_template_response(self):
        response = self.client.get('/404/')
        self.assertContains(response, 'Error handler content', status_code=404
