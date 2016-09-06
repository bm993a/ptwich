import query


# authentication functions are not developed

# REQUIRES AUTHENTICATION
def users_emotes(channel):
	url = '/users/' + channel + '/emotes'
	return query.q(url)

# find information for a given user
# return a dictionary about a user's info
def user_info(channel):
	url = '/users/' + channel
	return query.q(url)

# REQUIRES AUTHENTICATION
def users_user():
	url = '/user'
	return query.q(url)	