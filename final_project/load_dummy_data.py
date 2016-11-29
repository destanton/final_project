import requests
from django.contrib.auth.models import User
from sherlock.models import About, Profile
from random import choice

hospitals = ['John Doe Memorial Hospital', 'St. Saint Hospital',
             'Mayo Clinic', 'Northwestern Memorial Hospital',
             'Mary Black Memorial Hospital', 'UCLA Medical Center',
             'Johns Hopkins Hospital', 'General Hospital',
             'Sacred Heart Hospital', 'Duke Hospital']

def create_data():
    pic_links = []
    url = "https://randomuser.me/api/?nat=us&results=10"
    results = requests.get(url).json()
    all_res = results["results"]
    for res in all_res:
        x = User.objects.create_user(username=res['login']['username'], password="safepass")
        Profile.objects.filter(user=x).update(first_name=res['name']['first'], last_name=res['name']['last'], gender=res['gender'])
        About.objects.filter(user=x).update(birthdate=res['dob'][:10], city_of_birth=res['location']['city'], state_of_birth=res['location']['state'], birth_hospital=choice(hospitals))
        prof = Profile.objects.get(user=x)
        about = About.objects.get(user=x)
        pic_links.append(res['picture']['large'])


['https://randomuser.me/api/portraits/men/16.jpg', 'https://randomuser.me/api/portraits/men/98.jpg', 'https://randomuser.me/api/portraits/men
/62.jpg', 'https://randomuser.me/api/portraits/women/77.jpg', 'https://randomuser.me/api/portraits/women/10.jpg', 'https://randomuser.me/api/
portraits/men/8.jpg', 'https://randomuser.me/api/portraits/men/97.jpg', 'https://randomuser.me/api/portraits/women/78.jpg', 'https://randomus
er.me/api/portraits/men/2.jpg', 'https://randomuser.me/api/portraits/men/34.jpg']

['https://randomuser.me/api/portraits/women/26.jpg', 'https://randomuser.me/api/portraits/women/65.jpg', 'https://randomuser.me/api/portraits
/men/13.jpg', 'https://randomuser.me/api/portraits/men/57.jpg', 'https://randomuser.me/api/portraits/men/32.jpg', 'https://randomuser.me/api/
portraits/women/38.jpg', 'https://randomuser.me/api/portraits/men/27.jpg', 'https://randomuser.me/api/portraits/women/26.jpg', 'https://rando
muser.me/api/portraits/men/75.jpg', 'https://randomuser.me/api/portraits/women/59.jpg']
