import sqlite3

import re


class Searcher():
	phone_length = 12

	def __init__(self, database):
		self.conn = sqlite3.connect(database)
		self.cursor = self.conn.cursor()


	def get_nums(self, sample):
		'''returns not more ten 10 num from data base after search sample'''

		if re.search(r'[^\+ \(\)\d" " \-]', sample):
			return 'incorrect input'
		sample_digits = ''.join(re.findall(r'\d+', sample))	
		if len(sample_digits) > self.phone_length:
			return 'incorrect input'
		if len(sample_digits) == 0:
			return 'incorrect input'
		
		query = 'select number from numbers where number like"{}%" limit 10'
		result = self.cursor.execute(query.format(
			sample_digits
			)).fetchall()
		return [x[0] for x in result]

if __name__ == '__main__':
	search = Searcher('phones.db')
	print(search.get_nums('380'))


	
