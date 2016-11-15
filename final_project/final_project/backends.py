from social.backends.oauth import BaseOAuth2


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
        return response
