from social.backends.oauth import BaseOAuth2
from bs4 import BeautifulSoup
from sherlock.models import Relative


class Twentythreeandme(BaseOAuth2):
    name = 'twentythreeandme'
    AUTHORIZATION_URL = 'https://api.23andme.com/authorize'
    ACCESS_TOKEN_URL = 'https://api.23andme.com/token'
    REDIRECT_STATE = False
    ACCESS_TOKEN_METHOD = 'POST'
    ID_KEY = 'id'
    DEFAULT_SCOPE = ['basic', 'names', 'ancestry', 'family_tree', 'relatives', 'genomes']

    def get_user_details(self, response):
        name = response.get('name') or ''
        fullname, first_name, last_name = self.get_user_names(name)
        return {'username': name,
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name}

    # user = self.request.user

    def user_data(self, access_token, *args, **kwargs):
        # response = self.get_json('https://api.23andme.com/1/names/',
        #                          headers={'Authorization': 'Bearer {}'.format(access_token)})
        family = self.get_json('https://api.23andme.com/1/relatives/',
                               headers={'Authorization': 'Bearer {}'.format(access_token)})
        print(family)
        if family:
            item = (family[0]["relatives"])
            # relative = Relative.objects.create(user=self.request.user)
            x = kwargs['user']
            for name in item:
                first = name.get("first_name")
                last = name.get("last_name")
                relationship = name.get("relationship")
                birthyear = name.get("birth_year")
                unique_id = name.get("match_id")
                location = name.get("family_locations")
                surname = name.get("family_surnames")
                similarity = name.get("similarity")
                Relative.objects.get_or_create(user=x, first_name=first, last_name=last, relationship=relationship,
                                               birth_year=birthyear, unique_id=unique_id, location=location,
                                               family_surnames=surname, similarity=similarity)
                print(last, first, relationship, birthyear, unique_id, location, surname)
        else:
            print("no family")

        # item = (ancestry[0]["ancestry"]["sub_populations"])
        # new_list = []
        # for counter, tag in enumerate(item):
        #     if tag.get("sub_populations"):
        #         new_list.append(tag.get("sub_populations"))
        #
        # for counter, tag in enumerate(new_list):
        #     print(counter, tag)
        # return response
