# This module implements methods that directly correspond to Twitch API requests.
#
#
#
# All returns are in the form for a dictionary.

# *********** incomplete - query needs to be updated before this file can be worked
# ***** get the library requests

# http://stackoverflow.com/questions/5842096/python-3-urllib-post-submit


# POST, GET are default - PUT & DELETE need to be added
#But we can override this get_method() function to get DELETE request:
#req = urllib.request.Request(new_url)
#req.get_method = lambda: "DELETE"


import urllib.request, urllib.parse, urllib.error




#import query


#GET /feed/:channel/posts	Get channel feed posts
#POST /feed/:channel/posts	Create post
#GET /feed/:channel/posts/:id	Get post
#DELETE /feed/:channel/posts/:id	Delete post
#POST /feed/:channel/posts/:id/reactions	Create reaction to post
#DELETE /feed/:channel/posts/:id/reactions	Delete reaction


# AUTHENTICATION (optional) channel_feed_read
# find posts belonging to a given channel
def feed_channel(channel, **kwargs):
  url = '/feed/' + channel + '/posts'

# AUTHENTICATION (required) channel_feed_edit
# create a post for a given channels feed
def feed_post(channel, **kwargs):
  url = 'feed/' + channel + '/posts'
  
# AUTHENTICATION (optional) channel_feed_read
#
#def feed

# AUTHENTICATION (required) channel_feed_edit
# delete a post for a given id
#def feed_delete(channel, id, **kwargs):
#  url = 'feed/' + channel + '/posts/' + id + '/reactions'

# def feed_reaction_add()
# def feed_reaction_delete()
