#! /usr/bin/python

import os
from sys import argv
from math import ceil

DEBUG = True

if len(argv) != 4: # show example usage:
    print 'Wrong number of arguments:', len(argv) - 1,  "(need 3) example usage:"
    print "python " + argv[0] + "  text.txt  200  out.jpg"
    exit(-1)

# process arguments:
text_file   = argv[1]
image_width = argv[2]
out_file    = argv[3]
tmp_file    = text_file + "_with_padding.tmp"

# get total pixel count from number of caracters:
try:
    pix_count = os.path.getsize(text_file)*8
    if DEBUG:
        print "pix_count:", pix_count
except:
    print "wrong file:", text_file
    exit(-1)

# get line count from pixel count (up rounded):
try:
    line_count = int(ceil(1. * pix_count / int(image_width)))
    if DEBUG:
        print "line_count:", line_count
        print "image_width:", image_width
except:
    print "wrong image_width:", image_width
    exit(-1)

# add padding at the end of the file:
padding = "?" * (int(image_width)/8)
command_string = "echo $(cat " + text_file + ") " + padding + " > " + tmp_file
os.system(command_string)
if DEBUG:
    print command_string

# build the bitmap: (TODO: reverse the bits in each byte)
command_string = "convert -size "                                 \
                + image_width + "x" + str(line_count) + " mono:"  \
                + tmp_file + " " + out_file

os.system(command_string)
if DEBUG:
    print command_string

# delete tmp file:
if not DEBUG:
    os.system("rm " + tmp_file)

