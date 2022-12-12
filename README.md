# depth info extraction  
## Introduction  
Depth Cam experiment notebook for PWO audio mocap. This is a notebook experiment aiding extraction of x/y/z positions of subjects from camera frames to help patial synchronization of audio and image in Ambisonic sound fields

### Research questions

1. what precision can be achieved using an RGBD camera for subject following
2. How does this compare to other methods
    - algorithmic RGB (openCV)
    - AI-drive (methodf's like alphapose or openpose
3. what are the problems with this method

## folder structure
### scripts
in teh scripts folder, only one asset is present at the time.
It is used to aid in the mapping of multiple detected persions to a single entity. It prses a text file generated from the other script with the actual tracking and writes a new one with filtered IDs. It is obsoleted by a new method but worked very well before the addition of AI to do subject classification
    .# parse text file
    .# 3 1 660 824 414 938 -1 -1 -1 -1 
    .# frame number, person_id, x, y, width, height, confidence, xmin, ymin, xmax, ymax
it filters the person_id to remove double IDs. 

