import query

# authentication functions are not developed

# find the most viewed videos that meet criteria
# parameters: broadcasts | hls | limit | offset
# return a dictionary 
def videos_channel(channel, **kwargs):
	url = 'channels/' + channel + 'videos'
	return query.q(url, **kwargs)

# find information for a particular video
# return a dictionary
def videos_info(id):
	url = 'videos/' + id
	return query.q(url)

# AUTHENTICATION REQUIRED: user_read
# find videos for channels a user follows
# return a dictionary
def videos_followed(id):
	url = 'videos/followed/' + id
	return query.q(url)

# find the most viewed videos that meet criteria
# parameters: limit | offset | game | period
# return a dictionary 
def videos_top(**kwargs):
	url = 'videos/top'
	return query.q(url, **kwargs)

