
RS2-hardware-Model - v3 2025-04-16 2:55pm
==============================

This dataset was exported via roboflow.com on April 16, 2025 at 4:56 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 4097 images.
Adapter are annotated in YOLOv11 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Fit within)
* Auto-contrast via histogram equalization

The following augmentation was applied to create 3 versions of each source image:
* Randomly crop between 0 and 30 percent of the image
* Random shear of between -7° to +7° horizontally and -8° to +8° vertically
* Random brigthness adjustment of between -25 and +25 percent
* Random exposure adjustment of between -14 and +14 percent
* Random Gaussian blur of between 0 and 4.5 pixels
* Salt and pepper noise was applied to 1.68 percent of pixels


