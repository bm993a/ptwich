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
	return follows_channel(channel, **kwargs)

# find information for a given channel
def channels_info(channel):
	url = 'channels/' + channel
	return query.api('get', url)

# find team objects a given belongs to
def channels_teams(channel):
	url = 'channels/' + channel + '/teams'
	return query.api('get', url)

# alternate name for another method
def channels_videos(channel, **kwargs):
	return videos_channel(channel, **kwargs)

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

# ****************************** feeds
# AUTHENTICATION required API not implemented

# AUTHENTICATION optional and not impleted
# find feed posts for a given channel
def feed_channel(channel, **kwags):
	url = 'feed/' + channel + '/posts'
	return query.api('get', url)

# AUTHENTICATION optional and not impleted
# find a post for a given channel
def feed_post_info(channel, id):
	url = 'feed/' + channel + '/posts/ + id'
	return query.api('get', url)

# ****************************** follows
# AUTHENTICATION required API not implemented

# find followers of a given channel
def follows_channel(channel):
	url = 'channels/' + channel + '/follows'
	return query.api('get', url)

# find if a user follows a given channel | provide extra info if the user does
def follows_user_channel(user, channel):
	url = 'users/' + user + '/follows/channels/' + channel
	return query.api('get', url)

# find a list of channels a user follows
def follows_user(user, **kwargs):
	url = 'users/' + user + '/follows/channels'
	return query.api('get', url)

# ****************************** games

# find games based on the number of viewers
def games_top(**kwargs):
	url = 'games/top'
	return query.api('get', url, **kwargs)

# ****************************** ingests
# find a list of all ingests
def ingests():
	url = 'ingests'
	return query.api('get', url)

# ***************************** root

# AUTHENTICATION optional and not impleted
# find information about the API and authentication status
def root():
	url = ''
	return query.api('get', url)

# ****************************** search
# find channels matching given criteria
def search_channels(**kwargs):
	url = 'search/channels'
	return query.api('get', url, **kwargs)

# find games matching given criteria
def search_games(**kwargs):
	url = 'search/games'
	return query.api('get', url, **kwargs)	

# find streams matching given criteria
def search_streams(**kwargs):
	url = 'search/streams'
	return query.api('get', url, **kwargs)
# ***************************** streams
# AUTHENTICATION required API not implemented

# find a list of streams with optional criteria
def streams(**kwargs):
	url = 'streams'
	return query.api('get', url, **kwargs)

# find a list of featured (promoted) streams
def streams_featured(**kwargs):
	url = 'streams/featured'
	return query.api('get', url, **kwargs)

# find information about a stream for a given channel, if it is online
def streams_info(channel):
	url = 'streams/' + channel
	return query.api('get', url)
	
# find a summary of current streams or for a given game
def streams_summary(**kwargs):
	url = 'streams/summary'
	return query.api('get', url, **kwargs)

# ***************************** subscriptions
# AUTHENTICATION required API not implemented

# ***************************** teams
# find a list of team objects
def teams(**kwargs):
	url = 'teams'
	return query.api('get', url)

# find information for a given team objects
def teams_info(team):
	url = 'teams/' + team
	return query.api('get', url)
# ***************************** users
# AUTHENTICATION required API not implemented

# find information for given user
def users_info(user):
	url = 'users/' + user
	return query.api('get', url)

# ***************************** videos
# AUTHENTICATION required API not implemented

# find information for a particular video
def videos(id):
	url = 'videos/' + id
	return query.api('get', url)

# find the most viewed videos for a given channel that meet criteria
def videos_channel(channel, **kwargs):
	url = 'channels/' + channel + 'videos'
	return query.api('get', url, **kwargs)

# find the most viewed videos that meet criteria
def videos_top(**kwargs):
	url = 'videos/top'
	return query.api('get', url, **kwargs)







