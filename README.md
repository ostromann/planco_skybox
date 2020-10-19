# Build a skybox for your Planet Coaster parks
This repository contains a python script to slice &amp; rename skybox images and make them ready to be imported to Planet Coaster.

# Requirements
You will have to install a few things to run this. 

The first thing is to get Python from here: https://www.python.org/downloads/ follow the respective links for your OS (Linux/Windows/Mac). Be sure to get a version that is larger than 3.6 (it probably works for any version > 3.0, too. but I haven't tested that.).


Once you have that, open a console window and install an image processing package for python like this:

`pip install opencv`


# Running the script
In the folder where you have the script `image_slicer.py`.
Next to it (i.e. in the same folder) you should have a folder with the images you want to have in your park. In order to get them displayed correct automatically in the game they should have the following names:
`back_00_00 \
01_back_00_00_left \
01_back_00_00_right \
01_back_00_00_front \
01_back_00_00_top \
01_back_00_00_bot \
`
...

If those are in place you can start the script by entering the next line to a console window:
`python image_slicer.py <folder_name>`
