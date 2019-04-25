from phone_search import Searcher

import pytest


def test_output_length():
	search = Searcher('phones.db')
	assert len(search.get_nums('380')) <= 10

def test_input_length():
	search = Searcher('phones.db')
	assert search.get_nums('38050640654615465') == "incorrect input"

def test_parenth_input():
	search = Searcher('phones.db')
	for i in search.get_nums('380(50)5'):
		assert i.startswith('38050') 

def test_space_input():
	search = Searcher('phones.db')
	for i in search.get_nums('380 50 5)'):
		assert i.startswith('380505') 

def test_dash_input():
	search = Searcher('phones.db')
	for i in search.get_nums('380-50-5'):
		assert i.startswith('380505') 

def test_plus_input():
	search = Searcher('phones.db')
	for i in search.get_nums('+380-50-5)'):
		assert i.startswith('380505') 

def test_mixed_input():
	search = Searcher('phones.db')
	for i in search.get_nums('+380(50) 565-71-51'):
		assert i.startswith('380505657151')

def test_miss_input():
	"""'O'-letter instead of zero """

	search = Searcher('phones.db')
	assert search.get_nums('+38O (50) 565-71-51') == "incorrect input"
	