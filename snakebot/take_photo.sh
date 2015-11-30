#!/bin/bash


fswebcam -r 640x480 --jpeg 100 --title "Print Progress :)" --shadow -set "brightness=100%" --save "$HOME/Pictures/3dprinter/photo.jpg";
exit $?;
