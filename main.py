#!/bin/python
import requests
import json
import re
import bs4
import tkinter as tk

#=================================================================================
#GLOBAL VARIABLE DECLARATION SECTION
#=================================================================================


#=================================================================================
#DATA AQUISITION
#here we'll turn the JSON into actually usable lists of data
#=================================================================================

class CatalogParsingClass:
	#we are going to add a ### to the board part of the URL so that we can easily replace that part
	_CATALOG_URL = 'http://a.4cdn.org/###/catalog.json'

	def __init__(self, board='g'):
		sess = requests.session()
		raw_catalog_data = sess.get(re.sub('###', board, self._CATALOG_URL)).text
		self._json_catalog_data = json.loads(raw_catalog_data)
		self._parse_data()
	
	def _parse_data(self):
		#here we first create a list of all the threads, a list of dictionaries
		self._number_of_pages = len(self._json_catalog_data)
		self._list_all_threads = []
		for current_page in self._json_catalog_data:
			for current_thread in range(len(current_page['threads'])):
				self._list_all_threads.append(current_page['threads'][current_thread])
		#now we get more details from the threads
		self._thread_number_list = []
		self._thread_name_list = []
		self._thread_raw_comment_list = []
		self._thread_number_list = []
		self._thread_number_list = []
		#for current_thread in self._list_all_threads:
		
	
	def return_thread_info(self, thread_number):
		return self._list_all_threads[thread_number]
		
	def return_number_of_total_threads(self):
		return len(self._list_all_threads)
		
	def refresh_data(self, board='g'):
		self.__init__(board)