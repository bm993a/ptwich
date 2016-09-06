import urllib.request
import json

_base_url = 'https://api.twitch.tv/kraken/'

class Query:
	def __init__(self, url_action):
		self.url = _base_url + url_action
		self.parameters = dict()


	# add parameters to the query
	# parameter | dictionary of paramters and corresponding values
	def add_parameters(self, passed):
		self.parameters = dict()
		for key, value in passed.items():
			self.parameters[key] = value

	# connect to the Twitch API with the desired query
	def fetch(self):
		# form the full url
		to_submit = self.url + '?'

		# base + ?, between + &
		for key, value in self.parameters.items():
			to_submit = to_submit + key + '=' + value + '&' 

		print(to_submit)

		# submit the url
		response = urllib.request.urlopen(to_submit)
		data = response.read().decode('utf-8')
		data = json.loads(data)

		return data


def api(url, **kwargs):
	q = Query(url)

	# process and add parameters
	for key, value in kwargs.items():
		kwargs[key] = str(value)
	q.add_parameters(kwargs)

	data = q.fetch()
	return data


