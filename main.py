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

class DataAcquisitionClass:
	def __init__(self, board):
		sess = requests.session()
		catalog_json_data_from_4chin = sess.get(re.sub('###', board, CATALOG_URL)).text