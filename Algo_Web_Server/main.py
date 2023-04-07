import os
import whisper
import subprocess
import math
import glob
import time
from pytube import YouTube
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
import cv2
from video_downloader import Video_Downloader
from audios_downloader import Audio_Downloader
from whisper_model import Whisper_Model
from images_downloader import Image_Downloader
from models import *
from text_dataset import dataset
import pickle

content_path = os.getcwd()
images_path = content_path + '\Images'
audios_path = content_path + '\Audios'
models_path = content_path + '\Model_dir'

if not os.path.exists('Images'):
    os.makedirs('Images')

if not os.path.exists('Audios'):
    os.makedirs('Audios')
    
if not os.path.exists('Model_dir'):
    os.makedirs('Model_dir')

# Download the mp4 file    
# link = 'https://www.youtube.com/watch?v=zfiSAzpy9NM'
# link = 'https://www.youtube.com/watch?v=Jo22NeTIDKU' # Sigmoind
# # link = 'https://www.youtube.com/watch?v=4HKqjENq9OU' # KNN
# vid_name = 'video.mp4'
# VideoDownloader = Video_Downloader(link,content_path,vid_name)
# audio_lenght = VideoDownloader.download_video()

# # # Split the video to mp3 chunks and save it in the currect dir
# seconds = 120
# AudioDownloader = Audio_Downloader(vid_name,content_path,audios_path,seconds)
# AudioDownloader.split_audio()
# # AudioDownloader.delete_audios()

# # Use whisper model to transcripte the mp3 audios
# WhisperModel = Whisper_Model('base',audios_path)
# results = WhisperModel.Text_To_Speech()
# AudioDownloader.delete_audios()
# WhisperModel.Print_Results()

# Download the video images and save it in the currect dir
# ImageDownloader = Image_Downloader(vid_name,content_path,images_path,30)
# ImageDownloader.Download_Images()
# ImageDownloader.Delete_Images()

text = """
The perceptron was intended to be a machine, rather than a program, and while its first implementation was in software for the IBM 704, it was subsequently implemented in custom-built hardware as the "Mark 1 perceptron". This machine was designed for image recognition: it had an array of 400 photocells, randomly connected to the "neurons". Weights were encoded in potentiometers, and weight updates during learning were performed by electric motors.
"""

# subject_list = ['Backpropagation', 'Convolutional networks', 'Cross-entropy', 'Extension beyond sigmoid neurons', 'Gradient descent - general', 'Network’s hyper-parameters', 'Overfitting and regularization', 'Perceptrons', 'Sigmoid', 'Softmax', 'Stochastic gradient descent', 'The architecture of neural networks', 'The vanishing gradient problem', 'Weight initialization']
subject_list = ['Backpropagation', 'Convolutional networks', 'Cross-entropy', 'Extension beyond sigmoid neurons', 'Gradient descent - general', 'Network’s hyper-parameters', 'Overfitting and regularization', 'Perceptrons', 'Sigmoid', 'Softmax', 'Stochastic gradient descent', 'The architecture of neural networks', 'The vanishing gradient problem', 'Weight initialization','KNN']
# subject_list = ['Backpropagation', 'Convolutional networks', 'Cross-entropy', 'Network’s hyper-parameters', 'Overfitting and regularization', 'Perceptrons', 'Sigmoid', 'Softmax', 'Stochastic gradient descent', 'The architecture of neural networks','Weight initialization']

# df = create_database(dataset,subject_list)
# SVM = SVM_Text_Model(dataset,subject_list)
# SVM = SVM_Text_Model(df)

#################################################################
# SVM = SVM_Text_Model()
# SVM.SVM_Single_Pred(text)
#################################################################


# svm_model = SVM.svm
# with open('Model_dir/svm_model.pkl', 'wb') as f:
#     pickle.dump(svm_model, f)

# i = 0
# for chunk in results:
#     print('Chunk start from:',i,' end in:',i + seconds)
#     SVM.SVM_Single_Pred(chunk)
#     print("*"*50)
#     i += seconds
# SVM.SVM_Single_Pred(text)

# KNN = KKN_Text_Model(dataset,subject_list)
# KNN.KNN_Single_Pred(text)

# print('KNN:')
# for i in range(10):
#     KNN = KKN_Text_Model(dataset,subject_list)
# KNN.KNN_Single_Pred(text)

# print('MLP:')
# for i in range(10):
#     MLP = MLP_Text_Model(dataset,subject_list)
# MLP.MLP_Single_Pred(text)

# print('DTC:')
# for i in range(10):
#     DTC = DTC_Text_Model(dataset,subject_list)
# DTC.DTC_Single_Pred(text)

# print('ADB:')
# for i in range(10):
#     ADB = AdaBoost_Text_Model(dataset,subject_list)
# ADB.AdaBoost_Single_Pred(text)

# print('SVM:')
# SVM = SVM_Text_Model(df)
# # for i in range(10):
# #     # SVM = SVM_Text_Model(dataset,subject_list)
# #     SVM = SVM_Text_Model(df)
# SVM.SVM_Single_Pred(text)

# print('SVC:')
# for i in range(5):
#     SVC = SVC_Text_Model(df)
