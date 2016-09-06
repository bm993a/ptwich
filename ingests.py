import query

# return a list of Twitch ingests
def ingests():
	url = 'ingests'
	return query.api(url)
