undistort
=========

Fix perspective distortion using ImageMagick, Python and a modern browser

Required tools:
- [Python 2.x](https://www.python.org/downloads/) or [PyPy](http://pypy.org/download.html)
- [ImageMagick](http://www.imagemagick.org/script/download.php)
- Sufficiently modern browser with SVG support

How to use:
- Edit path to ImageMagick **convert** program in **undistort_gui.py**
- Run **undistort_gui.py** \<image_filename\> \<output_filename\>
  (your default browser will open with image correction interface)
- **Drag** with mouse to move and **Shift+drag** to rotate guidelines
- Mark the distorted rectangle
- Change output image width, height and/or aspect ratio
- Press **Fix** button

Released for public domain by Grom PE.


example
=======

![Undistort.py example: "Trust my Rage" by Dae-Thalin](http://i.imgur.com/Bfy1PLa.jpg)

![Undistort.py example result: "Trust my Rage" by Dae-Thalin](http://i.imgur.com/ESAtQqR.jpg)

Image ["Trust my Rage"](http://dae-thalin.deviantart.com/art/Trust-my-Rage-439926102) (c) [Dae-Thalin](http://dae-thalin.deviantart.com/), used with permission
