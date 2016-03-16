from json import dumps
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.utils import override_settings

from door.models import get_hackerspace_door

DOOR_KEY = 'KEY123'


@override_settings(DOOR_KEY=DOOR_KEY)
class DoorAPITest(TestCase):
    post_url = reverse('door_post')

    def json_post(self, data):
        return self.client.post(
            self.post_url,
            dumps(data),
            content_type='text/json'
        )

    def test_wrong_method(self):
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, 405)

        response = self.client.put(self.post_url, {})
        self.assertEqual(response.status_code, 405)

        response = self.client.delete(self.post_url)
        self.assertEqual(response.status_code, 405)

    def test_post_no_key(self):
        response = self.json_post({
            "status": True
        })
        self.assertEqual(response.status_code, 400)

    def test_post_wrong_key(self):
        response = self.json_post({
            "status": True,
            "key": "LOLKEY"
        })
        self.assertEqual(response.status_code, 400)

    def test_post_garbage(self):
        response = self.json_post({
            "status": "adsdsgdsgads",
            "key": DOOR_KEY
        })
        self.assertEqual(response.status_code, 400)

    def test_correct_post(self):
        response = self.json_post({
            "status": True,
            "key": DOOR_KEY
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(get_hackerspace_door().is_open)

        self.assertEqual(get_hackerspace_door().data_set.count(), 1)

    def test_open_close(self):
        self.json_post({
            "status": True,  # open
            "key": DOOR_KEY
        })

        self.json_post({
            "status": False,  # close
            "key": DOOR_KEY
        })

        self.assertEqual(get_hackerspace_door().data_set.count(), 1)
        self.assertFalse(get_hackerspace_door().is_open)
