import argparse
import api

parser = argparse.ArgumentParser(description='Twitch API via command line')
parser.add_argument('action', type=str, help='which api request to preform')
subparsers = parser.add_subparsers(dest='subcommand')


# related to api.channels_follows
p_channel_follows = subparses.add_parser('channels_follows')
p_channel_follows = add.argument('-l', '--limit', action='store_true', type=int,
  help='max number of results')
p_channel_follows = add.argument('-c', '--cursor', action='store_true',
  help='link from a previous request for pagination)
p_channel_follows = add.argument('-d', '--direction', choices=['asc', 'desc'], action='store_true',
  help='sorting based on creation date')

# related to api.channels_info
p_channel_info = subparsers.add_parser('channels_info')
p_channel_info.add_argument('channel', type=string, help='twitch channl id')


# setup is done - parse the command
args = parser.parse_args()


if args.subcommand == 'channel_follows':
  print(args.subcommand.channel)
if args.subcommand == 'channel_info':
  print(args.subcommand.limit)


