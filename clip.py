"""
DO NOT DELETE THE AUTHOR COPYRIGHT
©Connor Talbot 2021 - https://github.com/con-dog/clippy

clip.py - Animate a given directory of text files.

The text files in the directory provided should be 'frames' in a sequence
to give the impression of animation.

Example:
In a directory called 'art/sea', there is a few text files:

Eg: sea_1a, sea_1b, sea_1c, sea_1d

Which clearly show a boat and a bird moving (frame by frame)

sea_1a.txt
----------
.................
........~...v....
.........../|....
.....v..../_|__..
.........\-----/.
~~~~~~~~~`~~~~~~'

sea_1b.txt
.................
.......~...v.....
........../|...\,
....v..../_|__...
........\-----/..
~~~~~~~~`~~~~~~'~

sea_1c.txt
.................
.....~...v.......
......../|.../`\.
..v..../_|__.....
......\-----/....
.~~~~~`~~~~~~'~~~

sea_1d.txt
.................
....~...v..\,/...
......./|........
.v..../_|__......
.....\-----/.....
~~~~~`~~~~~~'~~~~

Any art samples you create should be of a frame-by-frame nature,
saved to a directory under 'art' in the repo
"""

import argparse
from contextlib import ExitStack
import glob
import math
import os
import random
import sys
import time

# MOVE CURSOR
CURSOR_UP = '\033[1A'  # moves cursor up one line
CURSOR_DOWN = '\033[1B'  # moves cursor up one line
CURSOR_RESET = '\033[u'

# Create the parser
my_parser = argparse.ArgumentParser(description='Animate frames in a cli')

# Add the arguments
my_parser.add_argument(
    'Path', metavar='path', type=str, help='the relative path to the frames',
    )
my_parser.add_argument(
    'Speed', metavar='speed', type=int, help='the animation speed from 1-100'
    )
my_parser.add_argument(
    'Cycles', metavar='cycles', type=int, help='thenumber of times to cycle the'
    ' animation from 1-100'
    )

class ClipException(Exception):
    """Raise Exception if Clip class methods are misused"""
    pass

class Clip:
    """
    A class to manage all aspects of a clip
    """
    def __init__(self, frames_source_folder, animation_speed, animation_cycles):
        """Initialize instance of Tile"""
        os.system('color')  # Required to work, enables ANSI codes
        self._frames_source_folder = frames_source_folder
        self.animation_speed = 5*math.log(100/animation_speed) + 0.1
        self.animation_cycles = animation_cycles
        if not isinstance(self.animation_cycles, int):
            raise ClipException('Cycles must be an integer')
        if (self.animation_cycles < 1) or (self.animation_cycles > 1000):
            raise ClipException('Cycles must be an integer from 1-1000')

    @property
    def frames_source_folder(self):
        """Instance read only property"""
        return self._frames_source_folder

    def get_frames(self):
        """Get all the frame art from the given directory"""
        # get all .txt in dir
        filenames = glob.glob(f"{self.frames_source_folder}{'./*.txt'}")  
        with ExitStack() as stack:  # dynamically handle multi file opens/closes
            files = [stack.enter_context(open(fname)) for fname in filenames]
            if files:
                frames = []
                for f in files:  # iterate over the frame files list
                    frame = f.read().splitlines()
                    frames.append(frame)
                self.frames = frames
            else:
                raise ClipException('Path must include txt files!')

    def paint_cells(self):
        """Paint the cells in the tiles"""
        pass

    def play_clip(self):
        """Loop through a clips frames to display it to screen at the given
        speed"""
        sys.stdout.flush()
        for frame in self.frames:
            for row in frame:  # Iterate over each frames rows
                sys.stdout.write(row)
                sys.stdout.write('\n')  # newline after all cells in row shown
            # Move cursor back to top of display and draw next frame
            sys.stdout.write(CURSOR_UP*len(frame))
            time.sleep(self.animation_speed)

    def loop_clip(self):
        """Loop through the clip the given number of cycles"""
        while self.animation_cycles > 1:
            self.play_clip()
            self.animation_cycles -= 1
        os.system('cls')
        
    def run(self):
        """Call instance functions to animate the frames to the screen and cycle
        them 'x' times"""
        clip.get_frames()
        clip.play_clip()
        clip.loop_clip()


if __name__ == '__main__':
    args = my_parser.parse_args()
    path = args.Path
    cycles = int(args.Cycles)
    speed = int(args.Speed)
    if not isinstance(speed, int):
        raise ClipException('Speed must be an integer from 1-100')
    if (speed < 1) or (speed > 100):
            raise ClipException('Speed must be an integer from 1-100')
    clip = Clip(path, speed, cycles)
    clip.run()

