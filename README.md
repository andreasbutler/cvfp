# cvfp
Computer Vision Final Project - ASL Parsing

Andreas Butler, Jonathan Colen, and Philip Yu

Python Files:

- confusionmatrix.py - generates and prints a confusion matrix on the test dataset given the model with name 'letter_classifier.h5'
- nlp.py - utility for generating the nlpDictionary.txt file from words.txt
- nlpPredictor.py - wrapper class for nlp.py. Reads in nlpDictionary.txt and provides predictions given input
- super_example.py - runs live input with a Kinect and recognizes off of the input with NLP integrated
- the_whole_project.py - trains the neural network on the depth dataset

Extra Files:

- confOut.txt - output file containing the confusion matrix
- confusionmatrix.xlsx - more readable confusion matrix Excel file
- letter_classifier.h5 - the model parameters for the trained neural network
- nlpDictionary.txt - dictionary file for loading into nlpPredictor.py
- words.txt - word corpus for nlp.py to create a dictionary file

Old Python Files:

- move_files.py - utility for unpacking one of the datasets we downloaded
- nlpTester.py - used for testing purposes
- separate_save_frames.py - saves and sorts frames of a video given an annotations file containing classifications and timestamps
    - This file was made in the event we needed to generate more data from video. Would be useful for the future
- separate_train_validate.py - splits up the dataset into training and validation sets
- space_vid_capture.py - attempt at capturing stereo images using a webcam
- test_video_capture.py - early method of recognizing off of webcam input
- unpack_depth_images.py - sorting images from the depth dataset into folders for training

