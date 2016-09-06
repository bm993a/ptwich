import query

# authentication functions are not developed


# find stream info for a given channel
# return a dictonary of a stream's info
def streams_info(channel):
	url = 'streams/' + channel
	return query.api(url, **kwargs)

# find streams promoted on Twitch
# parameters | limit | offset
# return a list of promoted streams
def streams_featured(**kwargs):
	url = 'streams/featured'
	return query.api(url, **kwargs)

# AUTHENTICATION REQUIRED: user_read
# find streams that the user is following
# parameters: limit | offset | stream_type
# return a dictionary
def streams_followed():
	url = 'streams/followed'
	return query.api(url, **kwargs)

# find streams meeting given criteria
# parameters:
# return a dictionary
def streams_search(**kwargs):
	url = 'streams/featured'
	return query.api(url, **kwargs)	

# find summary information for all streams on Twitch or for a given game
# GET /streams/featured	Get a list of featured streams
# return a dictonary
def streams_summary(**kwargs):
	url = 'streams/summary'
	return query.api(url, **kwargs)


