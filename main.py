#!/bin/python
import requests
import json
import re
import tkinter as tk

#=================================================================================
#GLOBAL VARIABLE DECLARATION SECTION
#=================================================================================

#we are going to add a ### to the board part of the URL so that we can easily replace that part
CATALOG_URL = 'http://a.4cdn.org/###/catalog.json'
THREAD_LIST_URL = 'http://a.4cdn.org/###/threads.json'

#=================================================================================
#DATA AQUISITION
#here we'll turn the JSON into actually usable lists of data
#=================================================================================

class CatalogParsingClass:
	def __init__(self, board):
		sess = requests.session()
		raw_catalog_data = sess.get(re.sub('###', board, CATALOG_URL)).text
		self._json_catalog_data = json.loads(raw_catalog_data)
		self._parse_data()
	
	def _parse_data(self):
		self._number_of_pages = len(self._json_catalog_data)
		self._list_all_threads = []
		for current_page in self._json_catalog_data:
			for current_thread in range(len(current_page['threads'])):
				self._list_all_threads.append(current_page[current_thread])
		print(self._list_all_threads)