from django.conf import settings
from haystack.backends.elasticsearch_backend import (ElasticsearchSearchBackend,
    ElasticsearchSearchEngine)

class MyElasticBackend(ElasticsearchSearchBackend):

    def __init__(self, connection_alias, **connection_options):
        super().__init__(connection_alias, **connection_options)
        MY_SETTINGS = {
            'settings': {
                "analysis": {
                    "analyzer": {
                        "ngram_analyzer": {
                            "type": "custom",
                            "tokenizer": "lowercase",
                            "filter": ["haystack_ngram"]
                        },
                        "edgengram_analyzer": {
                            "type": "custom",
                            "tokenizer": "lowercase",
                            "filter": ["haystack_edgengram"]
                        }
                    },
                    "tokenizer": {
                        "haystack_ngram_tokenizer": {
                            "type": "nGram",
                            "min_gram": 2,
                            "max_gram": 15,
                        },
                        "haystack_edgengram_tokenizer": {
                            "type": "edgeNGram",
                            "min_gram": 3,
                            "max_gram": 15,
                            "side": "front"
                        }
                    },
                    "filter": {
                        "haystack_ngram": {
                            "type": "nGram",
                            "min_gram": 2,
                            "max_gram": 15
                        },
                        "haystack_edgengram": {
                            "type": "edgeNGram",
                            "min_gram": 2,
                            "max_gram": 15
                        }
                    }
                }
            }
        }
        setattr(self, 'DEFAULT_SETTINGS', MY_SETTINGS)


class ConfigurableElasticSearchEngine(ElasticsearchSearchEngine):
    backend = MyElasticBackend
