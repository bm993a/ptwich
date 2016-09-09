import sys
sys.path.insert(0, '../')
import api
import unittest


channel = 'calebhart42'


# ensure api functions are able to return something other than None
class api_basic(unittest.TestCase):

	def test_channels_follows(self):
		self.assertIsNotNone(api.channels_follows(channel))

	def test_channels_info(self):
		self.assertIsNotNone(api.channels_info(channel))

	def test_channels_teams(self):
		self.assertIsNotNone(api.channels_teams(channel))

	def test_channels_videos(self):
		self.assertIsNotNone(api.channels_teams(channel))


if __name__ == '__main__':
	unittest.main()
