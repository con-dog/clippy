
<p align="center"><img src="media/clippy_watermarked.gif" height="300" width="500"></p>

# clippy
Create and play coloured 🟥🟩🟦 or color-less ⬛️⬜️ animated ASCII-art in the command line! 

clippy can help if you are wanting to;
- Develop a rogue-like ASCII game
- Develop word games (animate text)
- Develeop TUI's or CUI's
- Develop a Terminal screensaver
- Create animated logos for your scripts
- Make ASCII-art
- Make coloured ASCII art
- Make animated ASCII art

## Example Animations ##

1) txt to clip!
2) animated script logo
3) coloured vs colourless
4) animated vs non-animated


| Get this clip | From this txt file/s! |
| -------- | ---------- |
|<p align="center"><img src="media/sea.gif" height="300" width="500"></p>|<p align="center">.................<br>........~...v....<br>.........../&#124;....<br>.....v..../_&#124;__..<br>.........&#92;-----/.<br>~~~~~~~~~`~~~~~~'</p>|

## How clippy works ##
clippy looks at all the txt files in a directory, and sequentially prints each file to the console in the same line/column position.

Each txt file acts as a 'frame' of the clip; Minor variations between these text files creates the animation! 

## Make your own animations ##
### Steps ###
1) Create a sub-directory inside the 'art' directory. Give it a meaningful name eg: "Sailing_boat" for a sailing boat animation
2) Create a base/template txt file. Your ASCII-art template will live in here. Do it yourself or get ideas from https://www.asciiart.eu/
  Eg: your base might have some ASCII-art like this in it (or anything you want!)
<p align="center">.................<br>........~...v....<br>.........../&#124;....<br>.....v..../_&#124;__..<br>.........&#92;-----/.<br>~~~~~~~~~`~~~~~~'</p>

3) Make multiple copies of this file and in each copy, make some minor changes, for example below I've shifted the boat left, and added a seagull: Tip: You can add as many frames and variations as you want. The more the better!
<p align="center">.....\,/.........<br>~...v............<br>.../&#124;............<br>../_|__..........<br>.\-----/.........<br>~`~~~~~~'~~~~~~~~</p>

4) Run clip.py and pass the relative path of the directory containing your txt files (frames), pass it the speed (1-100), and pass it the number of cycles to run (1-1000)
5) Enjoy and contribute your art here! Submit a pull request of your art to this repo!

## ROADMAP ##
1) Build library of ASCII-art and animated ASCII-art
2) Auto-colour terminal art 
3) Generative ASCII-art
