# Edge detection and object contours

_Edges_ in an image are points where the intensity exhibits a discontinuity, changing abruptly. Detecting edges is a non trivial problem as it is not always clear where the intensity has to be considered different. There are several algorithms which have been developed for the task, but we will focus on the most famous one, the Canny detector.

_Contours_ of an object in an image are closed lines which enclose the object and are typically extracted from the edges \(which are not necessarily closed lines\).

For the code here, you need to import OpenCV and matplotlib:

```python
import cv2
from matplotlib import pyplot as plt
```

## The Canny edge detection

The Canny edge detector is the most famous of the methods for detecting edges in an image. This algorithm was developed by [J. Canny in 1986](edge-detection-and-object-contours.md#references) and is still widely used. It benefits from:

* low error rate;
* good localisation: the distance between the detected pixel edges and the real ones is minimised;
* minimal response: one detector response per edge

The steps followed are:

1. **Filter the noise**: use a gaussian filter;
2. **Find the intensity gradient**: use the Sobel operator in directions$$x$$and$$y$$;
3. **Non-maximum suppression**:  remove the pixels not considered to be part of the edge \(keep only thin lines\);
4. **Hysteresis**: use lower \($$t_l$$\) and upper \($$t_u$$\) thresholds to that, calling$$g$$the pixel's gradient,
   * $$g > t_u$$, then pixel gets accepted as edge
   * $$a = g < t_l$$, then pixel gets rejected
   * $$t_l <= g <= t_u$$, then pixel accepted as edge only if it is connected to a pixel which passes the upper threshold condition

Note that the Canny edge detection method recommends a ratio of the hysteresis threshold upper:lower between 2:1 and 3:1.

### Trying the Canny out in OpenCV

Let's use OpenCV's implementation. I'll use a photo with two pens on a red surface, and because the surface is reflecting, in one corner you can see the light reflection of something. We'll see how non-trivial the task of extracting the edges is, in terms of the dependency of the result to the thresholds used. Wikipedia illustrates this point very well.

```python
# Read image with OpenCV
image = cv2.imread('pens.jpg')

# OpenCV reads it in BGR, Matplotlib interprets it in RGB, so created a converted colourspace one
RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# also create a grayscale converted image as Canny wants single-channel input
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Showing both the original and the grayscale image

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

ax1.grid()
ax1.imshow(RGB_image)

ax2.grid()
plt.gray()
ax2.imshow(gray)

plt.show();
```

![Original image and its grayscale version](../../.gitbook/assets/cv-pens.png)

Let's do the detection

```python
# Perform a Canny edge detection: can vary the thresholds used to see differences
# the Canny method returns image with edges, we are not changing the default aperture size of the Sobel operator (3)
edged = cv2.Canny(gray, 50, 300)
```

and show the result:

```python
plt.imshow(edged)
plt.grid()
plt.show();
```

![Canny edge detection on the image](../../.gitbook/assets/canny.png)

## Contours

The retrieval of contours is, as we said, typically performed on an image where edges have already been detected, although this is not a compulsory step. The OpenCV implementation uses the algorithm described by [Suzuki and Abe](edge-detection-and-object-contours.md#references) and it returns the contours themselves, as in, the location of them, as well as their hierarchy. Based on the API, in [`findContours`](http://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=findcontours#findcontours), you can ask for only the furthermost external contours or all of them, with or without their hierarchical relationships \(which is within which\).

Note that OpenCV also gives you the opportunity to directly draw the retrieved contours on the image with method [`drawContours`](http://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=findcontours#drawcontours), and to retrieve some properties of said contours, like perimeter and area enclosed, see the [reference](edge-detection-and-object-contours.md#references).

```python
# find the contours on the edged image
# retrieving only the external ones and without compressing them

contours_edged = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cnt, hyer = contours_edged

# drawing contours on original image
# we draw them all (-1), in green ((0, 255, 0)) and with line tickness 3

img = cv2.drawContours(RGB_image, cnt, -1, (0, 255, 0), 3)

plt.imshow(img)
plt.grid()

plt.show();
```

![Contours detected in the photo](../../.gitbook/assets/cnt.png)

## References

1.  J Canny [**A computational approach to edge detection**](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.420.3300&rep=rep1&type=pdf), _IEEE Transactions on pattern analysis and machine intelligence_, 6, 1986.
2.  The OpenCV [tutorial](http://docs.opencv.org/trunk/da/d22/tutorial_py_canny.html) on Canny
3.  S Suzuki, K Abe, [**Topological Structural Analysis of Digitized Binary Images by Border Following**](http://s3.amazonaws.com/academia.edu.documents/38698235/suzuki1985.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1500731725&Signature=QpLT9aA2J4BneMQ%2FF3EauPKiZ68%3D&response-content-disposition=inline%3B%20filename%3DTopological_Structural_Analysis_of_Digit.pdf), _Computer Vision, Graphics and Image Processing_, 30, 1985
4. [Wikipedia](https://en.wikipedia.org/wiki/Edge_detection#Why_it_is_a_non-trivial_task) on why edge detection is a non-trivial task
5. A [tutorial](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html?highlight=contourarea) on OpenCv about how to retrieve some properties of contours

