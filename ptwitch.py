import argparse
import channels

parser = argparse.ArgumentParser()


#
parser.add_argument('name')
parser.add_argument('--channel', action='store_true')



#
args = parser.parse_args()

#
if args.channel:
	channel_list = channels.channel_info(args.name)
	print(channel_list)