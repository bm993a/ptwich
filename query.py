import requests

_base_url = 'https://api.twitch.tv/kraken/'



class Query:
	def __init__(self, action, url):
		self.action = action.lower()
		self.parameters = dict()
		self.url = _base_url + url

	# add parameters to the query
	# parameter | dictionary of paramters and corresponding values
	def add_parameters(self, passed):
		self.parameters = dict()
		for key, value in passed.items():
			self.parameters[key] = value

	def fetch(self):
		# form the full url
		to_submit = self.url + '?'
		for key, value in self.parameters.items():
			to_submit = to_submit + key + '=' + value + '&' 

		if self.action == 'get':
			response = requests.get(to_submit)
		elif self.action == 'post':
			response = requests.post(to_submit)
		elif self.action == 'put':
			response = requests.put(to_submit)
		elif self.action == 'delete':
			response = requests.delete(to_submit)	

		# check for a failure
		if response.status_code != requests.codes.ok:
			pass

		return response.json()		


def api(action, url, **kwargs):
	q = Query(action, url)

	# process and add parameters
	for key, value in kwargs.items():
		kwargs[key] = str(value)
	q.add_parameters(kwargs)

	data = q.fetch()
	return data







