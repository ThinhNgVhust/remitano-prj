from django.test import TestCase, Client
from .models import Movie, User
# Create your tests here.
# class MovieTestCase(TestCase):
#     def setUp(self) -> None:
#         #Create some users
#         user1 = User.objects.create(username='testuser1', password='12345')
#         user2 = User.objects.create(username='testuser2', password='12345')

#         #Create some movies
#         movie1 = Movie.objects.create(link="movie1",creator = user1)
#         movie2 = Movie.objects.create(link="movie2",creator = user1)
#         movie3 = Movie.objects.create(link="movie3",creator = user1)
#         movie4 = Movie.objects.create(link="movie4",creator = user1)
#         movie5 = Movie.objects.create(link="movie1",creator = user1)
#         movie6 = Movie.objects.create(link="movie2",creator = user1)
#         movie7 = Movie.objects.create(link="movie3",creator = user1)
#         movie8 = Movie.objects.create(link="movie4",creator = user1)
#     def test_movie_count(self):
#         user1 = User.objects.get(username="testuser1")