# This module implements methods that directly correspond to Twitch API requests.
#
#
#
# All returns are in the form for a dictionary.
# AUTHENTICATION required API calls are not implemented

import query


# ****************************** blocks
# AUTHENTICATION required API not implemented

# ****************************** channels
# AUTHENTICATION required API not implemented

# alternate name for another method
def channels_follows(channel, **kwargs):
	return follows_channels(channel, **kwargs)

# find information for a given channel
def channels_info(channel):
	url = 'channels/' + channel
	return query.q('get', url)

# find team objects a given belongs to
def channels_teams(channel):
	url = 'channels/' + channel + '/teams'
	return query.q('get', url)

# alternate name for another method
def channels_videos(channel, **kwargs):
	return videos_channe(channel, **kwargs)

# ****************************** chat
# get links to other chat endpoints
def chat_channel(channel):
	url = 'chat/' + channel
	return query.api('get', url)

# get chat badges for a given channel
def chat_channel_badges(channel):
	url = 'chat/' + channel + '/badges'
	return query.api('get', url)

# get a list of every emoticon object
def chat_emoticons():
	url = 'chat/emoticons'
	return query.api('get', url)

# get a list of emoticon images
def chat_emoticons_images():
	url = 'chat/emoticons_images'
	return query.api('get', url)

# ****************************** ingests
# find a list of all ingests
def ingests():
	url = 'ingests'
	return query.api('get', url)

# ****************************** search
# find channels matching given criteria
def search_channels(**kwargs):
	url = 'search/channels'
	return query.q('get', url, **kwargs)

# find games matching given criteria
def search_games(**kwargs):
	url = 'search/games'
	return query.q('get', url, **kwargs)	

# find streams matching given criteria
def search_streams(**kwargs):
	url = 'search/streams'
	return query.q('get', url, **kwargs)


# ***************************** teams
# find a list of team objects
def teams(**kwargs):
	url = 'teams'
	return query.q('get', url)

# find information for a given team objects
def teams_info(team):
	url = 'teams/' + team
	return query.q('get', url)

# ***************************** videos
# find information for a particular video
def videos(id):
	url = 'videos/' + id
	return query.q('get', url)

# find the most viewed videos for a given channel that meet criteria
def videos_channel(channel, **kwargs):
	url = 'channels/' + channel + 'videos'
	return query.q('get', url, **kwargs)

# AUTHENTICATION required API not implemented
# GET /videos/followed	Get list of videos belonging to channels user is following

# find the most viewed videos that meet criteria
def videos_top(**kwargs):
	url = 'videos/top'
	return query.q('get', url, **kwargs)







