from __future__ import print_function  # In case of Python 2

import __init__ as memefarm


mf = memefarm.memefarm()  # Make a memefarm

# Print a random sentence
print("Random sentence: \"{}\"".format(mf.phrase()))

# Find a random image
i = mf.image()
print("Image found in search for '{}':".format(i.searchterm))
i.show()
