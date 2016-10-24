import os
import sys
import codecs

import unittest

import json
import pygtrie as trie
from digDictionaryExtractor.populate_trie import populate_trie
from digDictionaryExtractor.name_dictionary_extractor import get_name_dictionary_extractor
from digExtractor.extractor_processor import ExtractorProcessor


class TestCountryPredictorExtractor(unittest.TestCase):

    def load_file(self, filename):
        names_file = os.path.join(os.path.dirname(__file__), filename)
        names = json.load(codecs.open(names_file, 'r', 'utf-8'))
        return names

    def test_country_predictory_extractor(self):
        city_to_country = self.load_file("city_to_country.json")
        doc = {"cities":["seattle", "san francisco", "bogota", "minneapolis"]} # load ad as dictionary
        e = CountryPredictorExtractor().set_city_to_country(city_to_country)
        ep = ExtractorProcessor().set_input_fields(
            'cities').set_output_field('country').set_extractor(e)

        updated_doc = ep.extract(doc)
        self.assertEquals(updated_doc['country'][0]['value'], list(['usa']))

if __name__ == '__main__':
    unittest.main()
