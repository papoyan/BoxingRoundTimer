#!/usr/bin/env python

import sh
import sys
import time
import random

combinations = (
			    '1 2',
			    '1 2 3',
			    '1 2 3 4',
			    '1 1 2 3',
			    '1 2 3 2',
			    '1 2 5 2',
			    '1 6 3 2',
			    '1 1 2',
			    '1 1 down 2',
			    '1 2 down 2',
			    '1 1 2 down 2',
			    '1 1 body body',
			    '1 2 back 2',
			    '1 2 1 2',
			    '2 3 2',
			    '1 2 3 3',
			    )

def play_sound(words, rate=250):
	sh.say(words, '-r %d' % rate)
	
def play_random_combo():
	combo_id = random.randint(0,len(combinations)-1)
	play_sound(combinations[combo_id])

def get_seconds_since_epoc():
	return time.mktime(time.gmtime())

def do_round(round_number, length=3):
	print 'round %d' % round_number
	play_sound('round %d' % round_number, 200)
	time.sleep(1.5)
	length_in_seconds = (length * 60.0)
	start = get_seconds_since_epoc()
	while length_in_seconds >= (get_seconds_since_epoc()-start):		
		try:			
			play_random_combo()
			time.sleep(1.35)
		except KeyboardInterrupt:
			print 'ctrl+c pressed. Ending it early huh? Pffft bitch made.'
			sys.exit(1)

	
def help():
	print '%s <number of rounds>' % sys.argv[0]
	sys.exit(2)
	
if __name__ == '__main__':
	
	try:
		number_of_rounds = int(sys.argv[1])
	except IndexError:
		help()
	except ValueError:
		help()
		
	for round_number in range(0, number_of_rounds):
		do_round(round_number+1)
