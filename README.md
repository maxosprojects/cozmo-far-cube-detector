A pre-trained custom HOG (Histogram of Oriented Gradients) detector to detect Cozmo cubes on a greater distance than SDK is capable of.

The detector needs `dlib` installed, e.g.:
```
pip3 install --user dlib
```

Visualization of the pre-trained model (detector):

![Visualization](https://github.com/maxosprojects/cozmo-far-cube-detector/raw/master/detector-visualization.png)

The `example.py` displays Cozmo's video feed with bounding boxes for cubes. It does not detect which cube it is, only bounding boxes (if you look at Cozmo's feed the markers on the cubes indeed are too noisy at distance to be identified).

There is a faster HOG detector implementation that I'll be looking to implement in python, but even `dlib` is good enough with its ~200ms/image on a reasonably performant computer.
Another improvement could be done by employing cubes' lights and some simple opencv functions.
