import query

# authentication functions are not developed

# REQUIRES AUTHENTICATION
# find a list of users subscribed to a channel
# return a dictionary
def subscriptions_channel():
	url = 'channels/' + channel + 'subscriptions'
	return query.q(url)

# REQUIRES AUTHENTICATION
# check if a user is subscribed to a channel
# return a dicionary
def subscriptions_check(channel, user):
	url = 'channels/' + channel + '/subscriptions/' + 'user'
	return query.q(url)

