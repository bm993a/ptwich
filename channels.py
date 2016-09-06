# API function requiring OAuth are not currently included

import query

# find the editors of the channel
# return a list of the channel's editors
def channel_editors(channel):
	url = 'channels/' + channel
	return query.api(url)

# find the followers of a channel
# return a list of the channel's followers
# parameters: cursor | direction | limit
def channel_followers(channel, **kwargs):
	url = 'channels/' + channel + '/follows'
	return query.api(url, **kwargs)

# find information about a channel
# return a dictionary of the JSON response
def channel_info(channel):
	url = 'channels/' + channel
	return query.api(url)

# find videos assoicated with the channel
# return a dictionary of the JSON response
# parameters:  broadcasts | hls | limit | offset
def channel_videos(channel, **kwargs):
	url = 'channels/' + channel + '/videos'
	return query.api(url)
