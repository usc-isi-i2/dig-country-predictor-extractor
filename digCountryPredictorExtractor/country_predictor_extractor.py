# -*- coding: utf-8 -*-
import copy

from itertools import ifilter
from itertools import tee
from itertools import chain
from itertools import izip
from digExtractor.extractor import Extractor


class CountryPredictorExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = 'cities'
        self.city_to_country = {}
        self.metadata = {"extractor": "CountryPredictorExtractor"}

    def get_city_to_country(self):
        return self.city_to_country

    def set_city_to_country(self, city_to_country):
        if not isinstance(city_to_country, dict):
            raise ValueError("city_to_country must be a dict")
        self.city_to_country = city_to_country
        return self


    def extract(self, doc):
        try:
            extracts = list()
            cities = doc['cities']
            #todo 
            #extracts.append()

            return list(frozenset(extracts))

        except:
            return list()

    def get_metadata(self):
        """Returns a copy of the metadata that characterizes this extractor"""
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        """Overwrite the metadata that characterizes this extractor"""
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        """Return a scalar or ordered list of fields to rename to"""
        return self.renamed_input_fields
