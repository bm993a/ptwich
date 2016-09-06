import query

# get a list of team object
# return a dictionary
def teams():
	url = 'teams'
	return query.q(url)

# find information for a given team object
# return a dictionary
def teams_info(team):
	url = 'teams/' + team
	return query.q(url)
