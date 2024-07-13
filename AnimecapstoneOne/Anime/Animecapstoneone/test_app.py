import unittest
from flask_testing import TestCase
from app import app, db
from models import Anime

class MyTest(TestCase):

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        self.client = app.test_client()
        self.headers = {"Authorization": "Bearer your_access_token"}

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Anime List', response.data)

    def test_get_anime_from_api(self):
        response = self.client.get('/api/anime', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

    def test_anime_detail_page(self):
        anime = Anime(id=1, title="Test Anime", synopsis="Test Synopsis", score=8.5, image_url="http://example.com/image.jpg")
        db.session.add(anime)
        db.session.commit()

        response = self.client.get('/anime/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Anime', response.data)
        self.assertIn(b'Test Synopsis', response.data)

if __name__ == '__main__':
    unittest.main()

    ##
      ##create_app: This method sets up the Flask app with the test configuration.
      ##setUp: This method is called before each test to set up the database and test client.
      ##tearDown: This method is called after each test to clean up the database.
      ##test_homepage: This test checks if the homepage loads correctly and contains the text "Anime List".
      ##test_get_anime_from_api: This test checks if the /api/anime endpoint returns a 200 status code and contains data.
      ##test_anime_detail_page: This test adds an anime to the database and checks if the detail page for this anime loads correctly and contains the anime's title and synopsis.
    ##