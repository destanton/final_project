from social.backends.oauth import BaseOAuth2
from bs4 import BeautifulSoup


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

    def user_data(self, access_token, *args, **kwargs):
        response = self.get_json('https://api.23andme.com/1/names/',
                                 headers={'Authorization': 'Bearer {}'.format(access_token)})
        ancestry = self.get_json('https://api.23andme.com/1/ancestry/',
                                 headers={'Authorization': 'Bearer {}'.format(access_token)})
        item = (ancestry[0]["ancestry"]["sub_populations"])
        new_list = []
        for counter, tag in enumerate(item):
            if tag.get("sub_populations"):
                new_list.append(tag.get("sub_populations"))

        for counter, tag in enumerate(new_list):
            print(counter, tag)
        return response
        return new_list




# new_list = []
# parser = BeautifulSoup(ancestry)
# all_label_tags = parser.findAll('label')
#
# for counter, tag in enumerate(all_label_tags):
#     if not tag.get("label"):
#         new_list.append(tag.get("label"))
#     print(new_list)
