import query

# find channels matching given criteria
# paramaters: query or q  (required) | limit | offset
# return a dictionary of matching channels
def search_channels(**kwargs):
	url = 'search/channels'
	return query.q(url, **kwargs)

# find games matching given criteria
# parameters: query or q (required) | type (required) | live
# return a dictionary of matching games
def search_games(**kwargs):
	url = 'search/games'
	return query.q(url, **kwargs)	

# find streams matching given criteria
# paramaters: query or q  (required) | limit | offset | hls
# return a dictionary of matching streams
def search_streams(**kwargs):
	url = 'search/streams'
	return query.q(url, **kwargs)
