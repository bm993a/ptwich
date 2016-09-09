import argparse
import api

parser = argparse.ArgumentParser(description='Twitch API via command line')


parser.add_argument('action', type=str, help='which api request to preform')



parser.parse_args()

# #
# parser.add_argument('name')
# parser.add_argument('--channel', action='store_true')
