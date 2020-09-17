# Face Anonymizer using OpenCV- Mask image and Gaussian Blur
This repository contains code to hide a face from images and videos. It uses HaarCascade for face and eyes- detection and with some image processing operations it replaces the face with a mask, or a gaussian blur.

#### Author: [Nikhil](https://github.com/nixkhil)

### Modes of utility:
- Images to Masked Images

```
import faceanon
facemask.image_mask(input_img_array,mask_img_array)
```
- Images to Masked Images, passing locations of the haarcascade files as function arguments
```
import faceanon
facemask.image_mask(input_img_array,mask_img_array,'/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_frontalface_default.xml','/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_eye.xml')
```

*Takes numpy arrays of input image and mask image and returns numpy array of the output masked image*
- Videos to Masked Videos

```
import faceanon
facemask.video_mask("inputfile.avi","outputfile.avi",mask_img_array,'/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_frontalface_default.xml','/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_eye.xml',640,360)#haarcascade files can still be passed as function arguments in the same sequence, 640,360 are the dimensions of the video
```

- Videos to Masked Videos, not specifying dimensions and haarcascade file locations
```
import faceanon
facemask.video_mask("inputfile.avi","outputfile.avi",mask_img_array)#default dimensions are 848,480 
```
*Takes .avi input file,output file name and numpy array of the mask image and produces .avi video file after applying mask*

### Sample Output for Images and Videos:

- Mask Image Used:

[![Working Demonstration](https://github.com/nixkhil/Face-Anon/blob/master/mask.jpg)](https://github.com/nixkhil/Face-Anon/blob/master/mask.jpg)

- Output Masked Image:

[![Working Demonstration](https://github.com/nixkhil/Face-Anon/blob/master/output.jpg)](https://github.com/nixkhil/Face-Anon/blob/master/output.jpg)

- Output Masked Video:
[![Working Demonstration](https://github.com/nixkhil/Face-Anon/blob/master/output.gif)](https://github.com/nixkhil/Face-Anon/blob/master/output.gif)

### Important: In videos few frames might be dropped while applying the mask. Audio is lost from video files.

```python
Copyright (c) 2020 Nikhil
Website: https://github.com/nixkhil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
