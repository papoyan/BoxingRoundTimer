#!/usr/bin/env python

import sh
import sys
import time
import random
import bisect

combinations = {
        '1 2': 5.0,
        '1 2 3': 4.5,
        '1 1 2 3': 4.0,
        '1 2 3 2': 4.2,
        '1 1 2': 3.5,
        '1 1 2 down 2': 3.5,
        '1 2 down 2': 3.5,
        '1 2 3 3': 3.2,
        '1 2 back 2': 2.2,
        '1 2 body body': 2.0,
        '1 2 3 4': 2.0,
        '1 2 1 2': 1.5,
        '2 3 2': 1.0,
        }

def play_sound(words, rate=220):
    sh.say(words, '-r %d' % rate)

def select_combo():

    items = combinations.keys()

    mysum = 0
    breakpoints = [] 

    for i in items:
        mysum += combinations[i]
        breakpoints.append(mysum)

    score = random.random() * breakpoints[-1]
    i = bisect.bisect(breakpoints, score)
    return items[i] 

def play_combo():
    play_sound(select_combo())

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
            play_combo()
            time.sleep(1.8)
        except KeyboardInterrupt:
            print 'Ending it early huh? Pffft bitch made.'
            sys.exit(0)

    print 'round %d COMPLETE\n\n' % round_number
    play_sound('round %d complete' % round_number, 200)

    
def help():
    print '%s <number of rounds>' % sys.argv[0]
    sys.exit(2)

def main():
    wait_period = 60
    try:
        number_of_rounds = int(sys.argv[1])
    except IndexError:
        help()
    except ValueError:
        help()

    for round_number in range(0, number_of_rounds):
        do_round(round_number+1)
        time.sleep(wait_period-10)
        print '10 seconds'
        play_sound('10 seconds')
        time.sleep(10)

if __name__ == '__main__':
    main()
