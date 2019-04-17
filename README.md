# Marley's Mellow Moodifying

* Python

* Uses PIL (Python Imaging Library) to generate various repeating colorful pattern using the modulus operator

* Creates a mask in the shape of a bottle of Marley's Mellow Mood drink, using the pattern created in the previous as the background (examples available in moodified folder)

* Applies the mask to inputted images so the image has a "frame" around it in the shape of a bottle with the background of the generated pattern

To run:
1. Install Python 2.x and following libraries: PIL, matplotlib, os, numpy
2. Place Marleys_Mood.py, bottle.png, and the images you would like to modify in the same directory
3. Run Marleys_Mood.py, call moodify_all(), and follow the prompts
4. Output will be in moodified directory