
RS2-hardware-Model - v2 2025-04-15 1:47pm
==============================

This dataset was exported via roboflow.com on April 15, 2025 at 3:52 AM GMT

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

The dataset includes 4094 images.
Adapter are annotated in YOLOv11 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)
* Auto-contrast via adaptive equalization

The following augmentation was applied to create 3 versions of each source image:
* Randomly crop between 0 and 80 percent of the image
* Random shear of between -30° to +30° horizontally and -30° to +30° vertically
* Random brigthness adjustment of between -70 and +70 percent
* Random exposure adjustment of between -50 and +50 percent
* Random Gaussian blur of between 0 and 7 pixels
* Salt and pepper noise was applied to 6.99 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Random shear of between -10° to +10° horizontally and -10° to +10° vertically
* Random brigthness adjustment of between -20 and +20 percent
* Random Gaussian blur of between 0 and 7.3 pixels
* Salt and pepper noise was applied to 3.74 percent of pixels


