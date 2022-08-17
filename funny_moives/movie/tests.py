from django.test import TestCase, Client
import json
from .models import Movie, User
# Create your tests here.
class MovieTestCase(TestCase):
    def setUp(self) -> None:
        #Create some users
        user1 = User.objects.create(username='testuser1', password='12345')
        user2 = User.objects.create(username='testuser2', password='12345')

        #Create some movies
        movie1 = Movie.objects.create(link="Y8vQRFkP0-o",creator = user1)
        movie2 = Movie.objects.create(link="Y8vQRFkP0-o",creator = user1)
        movie3 = Movie.objects.create(link="Y8vQRFkP0-o",creator = user1)
        movie4 = Movie.objects.create(link="Y8vQRFkP0-o",creator = user1)
        movie5 = Movie.objects.create(link="Y8vQRFkP0-o",creator = user2)
        movie6 = Movie.objects.create(link="Y8vQRFkP0-o",creator = user2)
        movie7 = Movie.objects.create(link="Y8vQRFkP0-o",creator = user2)
        movie8 = Movie.objects.create(link="Y8vQRFkP0-o",creator = user2)

    def test_movie_count(self):
        movies = Movie.objects.all().count()
        self.assertEqual(movies,8)

    def test_movie_by_user1(self):
        user1_movies = Movie.objects.filter(creator__username ="testuser1").count()
        self.assertEqual(user1_movies,4)

    def test_movie_by_user1(self):
        user2_movies = Movie.objects.filter(creator__username ="testuser2").count()
        self.assertEqual(user2_movies,4)


    def test_login_successed(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        result = c.login(username= 'testuser', password= '12345')#hashed passowrd
        self.assertTrue(result)
        response = c.post('/login', {'username': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code,302)

    def test_register(self):
        c = Client()
        response = c.post('/register', {"email":"thinhbka.nguyenvan@gmail.com",'username': 'john', 'password': 'smith','confirmation':"smith"})
        self.assertEqual(response.status_code,302)
        
    def test_load_page(self):
        c = Client()
        response = c.get('') #go to index
        self.assertEqual(response.status_code,200)
   