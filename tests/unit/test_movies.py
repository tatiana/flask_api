import json
import unittest

from venus.main import app


class MoviesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_list_movies(self):
        response = self.app.get('/movies')
        self.assertEqual(response.status_code, 200)
        body = eval(response.get_data())
        self.assertTrue(isinstance(body, list))
        self.assertEqual(len(body), 260)
        one_item = {
            "score": "9.2",
            "votes_count": "1171520",
            "id": 0,
            "title": "The Shawshank Redemption (1994)"
        }
        self.assertIn(one_item, body)

    def test_get_a_movie(self):
        response = self.app.get('/movies/2')
        self.assertEqual(response.status_code, 200)
        body = eval(response.get_data())
        expected_body = {
            "score": "9.0",
            "votes_count": "535889",
            "id": 2,
            "title": "The Godfather: Part II (1974)"
        }
        self.assertEqual(body, expected_body)

    def test_post_a_movie(self):
        sample_movie = {
            "score": "10.0",
            "votes_count": "1000000000000000000000000000",
            "title": "Friday Zip"
        }
        response = self.app.post('/movies', data=sample_movie)
        self.assertEqual(response.status_code, 200)
        response_after = self.app.get('/movies')
        list_all_movies = eval(response_after.get_data())

        exists = False
        for movie in list_all_movies:
            if movie["title"] == "Friday Zip":
                exists = True
                break

        self.assertTrue(exists)
