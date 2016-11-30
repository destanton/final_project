import requests
from django.contrib.auth.models import User
from sherlock.models import About, Profile
from random import choice

hospitals = ['John Doe Memorial Hospital', 'St. Saint Hospital',
             'Mayo Clinic', 'Northwestern Memorial Hospital',
             'Mary Black Memorial Hospital', 'UCLA Medical Center',
             'Johns Hopkins Hospital', 'General Hospital',
             'Sacred Heart Hospital', 'Duke Hospital']


# def create_data():
#     pic_links = []
#     url = "https://randomuser.me/api/?nat=us&results=10"
#     results = requests.get(url).json()
#     all_res = results["results"]
#     for res in all_res:
#         x = User.objects.create_user(username=res['login']['username'], password="safepass")
#         Profile.objects.filter(user=x).update(first_name=res['name']['first'], last_name=res['name']['last'], gender=res['gender'])
#         About.objects.filter(user=x).update(birthdate=res['dob'][:10], city_of_birth=res['location']['city'], state_of_birth=res['location']['state'], birth_hospital=choice(hospitals))
#         prof = Profile.objects.get(user=x)
#         about = About.objects.get(user=x)
#         pic_links.append(res['picture']['large'])

EYE_COLOR = [
    'Black',
    'Blue',
    'Brown',
    'Gray',
    'Green',
    'Hazel',
    'Other'
]

FAMILY = ['Cousin',
    'Child',
    'Parent',
    'Sibling',
    'Aunt',
    'Uncle',
    'Grandparent'
]

about = User.objects.all()

for x in about:
    About.objects.filter(user=x).update(eye_color=choice(EYE_COLOR), searching_for=choice(FAMILY))
    y = About.objects.get(user=x)
    print(y.eye_color, y.searching_for)
