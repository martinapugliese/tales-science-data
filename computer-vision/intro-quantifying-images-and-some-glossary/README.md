# Intro: quantifying images & some glossary

_Under the name "Computer vision" \(CV\) goes that set of techniques which allow us to manipulate and extract numerical data, and higher-level information, from an image, via a computer. This section will explain the basics of the field and then deal into more details, outlining the concepts that CV tackles. Nowadays, there is a division in the field in regards to "traditional" CV \(the set of techniques which is not based on the use of Neural Networks/Deep Learning\) and more state-of-the-art methods based on ANNs. We will touch on both sides._

Computer Vision is very interesting -  it's about writing code to manipulate and use images and it allows for many applications. Have a read at the two blogs in the [references](./#references) for a bit on the relation between Computer Vision and Machine Learning/Deep Learning.

For the code here in this project, we will use [OpenCV](http://docs.opencv.org/3.2.0/) through its Python bindings. For the part regarding ANNs, we will make use of [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/).

The glossary below is meant to contain basic definitions used all over the chapter.

## Some glossary

### Bimodal image

An image with two peaks in the intensity histogram.

### Binary image

Is an image with pixels which can only take values 0 or 1.

### Intensity

The intensity is the pixel value and is defined for grayscale images, where it is an 8-bit integer, hence taking values in the range \[0:255\], where 0 is black and 255 is white. It is sometimes referred to as _brightness_.

### Colour

For coloured images, colour is given as a vector of 3 components of intensity. For example in the RGB values are the intensities for red, green and blue.

### Contrast

Is the difference between maximum and minimum pixel intensities.

### ROI \(Region of Interest\)

A part of image selected for a purpose, like cropping around it or cutting it out.

## Formalism

Some notes on the formalism used are written in this page:

{% page-ref page="notes-on-the-formalism.md" %}

## References

1.  A good and super brief outline of the history of the field and its relation to Machine Learning in T Malisiewicz's [blog](http://www.computervisionblog.com/2015/03/deep-learning-vs-machine-learning-vs.html)
2.  An even better and more detailed outline of the development of Computer Vision and its relation to Deep Learning, from the same [blog](http://www.computervisionblog.com/2015/01/from-feature-descriptors-to-deep.html) above

