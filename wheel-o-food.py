#!/usr/bin/env python

# Name:         wheel-o-food.py
# Authors:      Michael Albert, Matthew Sheridan
# Date:         01 May 2016
# Revision:     02 May 2016
# Licence:      Beer-Ware License, Revision 42

"""Usage:
  wheel-o-food.py
  wheel-o-food.py -h | --help
  wheel-o-food.py --version

Options:
  -h --help  Show this help message.
  --version  Display program version number.
"""

__authors__ = "Matthew Sheridan"
__credits__ = ["Michael Albert", "Matthew Sheridan"]
__date__    = "01 May 2016"
__version__ = "0.2"
__status__  = "Development"

import os
import sys
from operator import itemgetter
import random
import shutil
import time
from configobj import ConfigObj
from docopt import docopt
from foodobj import FoodObj

if __name__ == "__main__":
    args = docopt(__doc__, help=True, version=__version__)
    config = ConfigObj("config.ini")
    config_in = config["Kitchen"]
    config_out = config["Takeout"]

    # (term_h, term_w) = os.get_terminal_size()
    # print(term_w)

    count = 5000

    # Add foods to global list.
    # The keys in food_options are FoodObjs; the values are their respective tally.
    global_options = []
    food_options   = dict()
    for category in config:
        for kind in config[category]:
            for item in config[category][kind]:
                new_food = FoodObj(kind, item)
                if category.lower() == "takeout":
                    new_food["takeout"] = True
                global_options.append(new_food)

    # Randomly select seven food options to use and add to dict.
    while len(food_options) < 7:
        temp = random.choice(list(global_options))
        food_options[temp] = 0

    try:
        # Run the countdown!
        for a in range(count):
            # Increment a random food option:
            food_options[random.choice(list(food_options))] += 1

            # Display running progress:
            sys.stdout.write("\r" + str(int((count - a) / 100)) + "  ")

            for option in food_options:
                name = option["name"][:8]
                if food_options[option] == max(food_options.values()):
                    name = name.upper()
                sys.stdout.write(name + ": " + str(food_options[option]) + "  ")
            time.sleep(0.01)
        print("")
    except KeyboardInterrupt:
        print("\nDon't be a quitter!")

    # Deliver the verdict:
    food_sorted = sorted(food_options, key=food_options.get, reverse=True)
    print("\nTonight, you will eat:\n" + str(food_sorted[0]))
