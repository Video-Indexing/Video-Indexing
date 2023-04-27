from video_downloader import Video_Downloader
from audios_downloader import Audio_Downloader
from whisper_model import Whisper_Model
from images_downloader import Image_Downloader
from models import *
import os
from sys import platform
from images_reco import recognize_new_image, mse
import cv2


content_path = os.getcwd()

if platform == "win32":
    last_dirs = content_path.split('\\')[-1]
    if last_dirs != 'Algo_Web_Server':
        content_path += '\Algo_Web_Server'
    
    images_path = content_path + '\Images'
    audios_path = content_path + '\Audios'
    video_path = content_path + '\\video.mp4'
else:
    last_dirs = content_path.split('/')[-1]
    if last_dirs != 'Algo_Web_Server':
        content_path += '/Algo_Web_Server'
        
    images_path = content_path + '/Images'
    audios_path = content_path + '/Audios'
    video_path = content_path + '/video.mp4'
        
    
vid_name = 'video.mp4'
seconds = 30
image_taker_pace = 15

if not os.path.exists(images_path):
    os.makedirs(images_path)

if not os.path.exists(audios_path):
    os.makedirs(audios_path)

subject_list = ['Backpropagation', 'Convolutional networks', 'Cross-entropy', 'Extension beyond sigmoid neurons',
                'Gradient descent - general', 'Network’s hyper-parameters', 'Overfitting and regularization',
                'Perceptrons', 'Sigmoid', 'Softmax', 'Stochastic gradient descent',
                'The architecture of neural networks', 'The vanishing gradient problem', 'Weight initialization', 'KNN']


def download_vid(link):
    VideoDownloader = Video_Downloader(link, content_path, vid_name)
    VideoDownloader.download_video()

def index_video(link):
    download_vid(link)
    split_audio()
    results = whisper_results()
    audio_results,classes = model_results(results)
    print(audio_results)
    images_results = recognize_images()
    final_indexing(audio_results,classes,images_results)
    # ret_dic = {"audio results": audio_results, "images results": images_results}
    ret_dic = {"audio results": audio_results} # audio tests
    # ret_dic = {"images results": images_results} # images tests.
    os.remove(video_path)
    return ret_dic


def split_audio():
    seconds = 30
    AudioDownloader = Audio_Downloader(vid_name, content_path, audios_path, seconds)
    AudioDownloader.split_audio()
    # AudioDownloader.delete_audios()


def whisper_results():
    # Use whisper model to transcripte the mp3 audios
    WhisperModel = Whisper_Model('base', audios_path)
    results = WhisperModel.text_to_speech()
    AudioDownloader = Audio_Downloader(vid_name, content_path, audios_path, seconds)
    AudioDownloader.delete_audios()
    WhisperModel.print_results()

    return results


def model_results(whisper_results):
    dic_results = {}
    # df = create_database(dataset,subject_list)
    # SVM = SVM_Text_Model(df)
    SVM = SVM_Text_Model()
    i = 0
    for chunk in whisper_results:
        print('Chunk start from:', i, ' end in:', i + seconds)
        result = SVM.svm_single_pred(chunk)
        print("*" * 50)
        key = f'{i}-{i + seconds}'
        dic_results[key] = result
        i += seconds

    return dic_results,SVM.classes


def recognize_images():
    ImageDownloader = Image_Downloader(vid_name, content_path, images_path, image_taker_pace)
    ImageDownloader.download_images()
    prediction = {}
    i = 0
    if platform == "win32":
        df_path = os.getcwd() + "\Model_dir\embedding_ConvNeXtBase_ex2.csv"
    else:
        df_path = os.getcwd() + "/Model_dir/embedding_ConvNeXtBase_ex2.csv"
    df = pd.read_csv(df_path)

    paths_list = []
    threshold = 7

    for image in os.listdir(images_path):
        if platform == "win32":
            img_path = images_path + f"\{image}"
        else:
            img_path = images_path + f"/{image}"
        paths_list.append(img_path)

    start_time = 0
    end_time = image_taker_pace
    if len(paths_list) == 1:
        prediction[f"{start_time}-{end_time}"] = recognize_new_image(df, paths_list[0])
    elif len(paths_list) == 2:
        img1 = paths_list[0]
        img2 = paths_list[1]
        error, _ = mse(img1, img2)
        if error < threshold:
            end_time = image_taker_pace * 2
            prediction[f"{start_time}-{end_time}"] = recognize_new_image(df, paths_list[0])
        else:
            prediction[f"{start_time}-{end_time}"] = recognize_new_image(df, paths_list[0])
            end_time += image_taker_pace
            start_time += image_taker_pace
            prediction[f"{start_time}-{end_time}"] = recognize_new_image(df, paths_list[1])
    else:
        for i in range(len(paths_list)-1):
            img1 = paths_list[i]
            img2 = paths_list[i + 1]
            error, _ = mse(img1, img2)
            print("Image matching Error between the two images:", error)
            if error < threshold:
                end_time += image_taker_pace
                if i == (len(paths_list) - 2):
                    prediction[f"{start_time}-{end_time}"] = recognize_new_image(df, img1)

            else:
                prediction[f"{start_time}-{end_time}"] = recognize_new_image(df, img1)
                start_time = end_time
                end_time += image_taker_pace

    ImageDownloader.delete_images()
    return prediction


def final_indexing(audio_results,classes,images_results):
    # for key in audio_results:
    #     audio_splitted = key.split('-')
    #     audio_start = int(audio_splitted[0])
    #     audio_end = int(audio_splitted[1])
    #     for img_key in images_results:
    #         img_splitted = img_key.split('-')
    #         img_start = int(img_splitted[0])    
    #         img_end = int(img_splitted[1])
            
    #         if img_start >= audio_start and img_end <= audio_end:
    #             pass  
    audio_results = update_dict(audio_results,15)
    images_results = update_dict(images_results,15)
    print(5)
# x = '0-60'
# y = '30-45'
# res = x.split('-')
# print(res)
# print(type(res))


# def helper(L1,L2):
#     start = 0
#     end = None
#     val = 1
#     for l1_key in L1:
#         l1_splitted = l1_key.split('-')
#         l1_start = int(l1_splitted[0])
#         l1_end = int(l1_splitted[1])
#         for l2_key in L2:
#             l2_splitted = l2_key.split('-')
#             l2_start = int(l2_splitted[0])
#             l2_end = int(l2_splitted[1])
#             end = min(l1_end,l2_end)
#             if start <= l1_start and end <= l1_end:
#                 val *= L1[l1_key]
#             if start <= l2_start and end <= l2_end:
#                 val *= L1[l2_key]
                
#             start = end
#             end = max(l1_end,l2_end)

# def helper(L1,L2):
#     L1_keys = sorted(L1.keys(), key=lambda x: int(x.split('-')[0]))
#     L2_keys = sorted(L2.keys(), key=lambda x: int(x.split('-')[0]))
    

#     # Initialize the start and end times to the first key in each dictionary
#     start_time_L1, end_time_L1 = L1_keys[0].split('-')
#     start_time_L2, end_time_L2 = L2_keys[0].split('-')

#     # Loop over the keys of both dictionaries and find the overlapping time slices
#     overlapping_times = []
#     for i in range(0, len(L1_keys)):
#         # Get the start and end times of the current time slice in L1
#         current_start_L1, current_end_L1 = L1_keys[i].split('-')
        
#         # Check if the current time slice in L1 overlaps with the current time slice in L2
#         if int(current_start_L1) <= int(end_time_L2) and int(start_time_L2) <= int(current_end_L1):
#             # Calculate the start and end times of the overlapping time slice
#             overlapping_start = max(int(start_time_L1), int(start_time_L2))
#             overlapping_end = min(int(end_time_L1), int(end_time_L2))
            
#             # Add the overlapping time slice to the list
#             overlapping_times.append(f"{overlapping_start}-{overlapping_end}")
        
#         # Update the start and end times of L1 for the next iteration
#         start_time_L1, end_time_L1 = current_start_L1, current_end_L1
        
#         # Check if we need to update the start and end times of L2 for the next iteration
#         if int(current_end_L1) > int(end_time_L2):
#             L2_keys.pop(0)
#             L2_first = L2_keys[0]
#             start_time_L2, end_time_L2 = L2_first.split('-')

#     print(overlapping_times)
    
L1 = {'0-30':2,
      '30-60':1.5,
      '60-90':1.75,
      '90-120':1.5,
      '120-150':2}

L2 = {'0-15':1.5,
      '15-75':2,
      '75-120':1.5,
      '120-135':2,
      '135-150':1.5}

# helper(L1,L2)

# Get the sorted keys of both dictionaries
# L1_keys = sorted(L1.keys(), key=lambda x: int(x.split('-')[0]))
# L2_keys = sorted(L2.keys(), key=lambda x: int(x.split('-')[0]))

# # Initialize the start and end times to the first key in each dictionary
# start_time_L1, end_time_L1 = L1_keys[0].split('-')
# start_time_L2, end_time_L2 = L2_keys[0].split('-')

# # Loop over the keys of both dictionaries and find the overlapping time slices
# overlapping_times = []
# for i in range(0, len(L1_keys)):
#     # Get the start and end times of the current time slice in L1
#     current_start_L1, current_end_L1 = L1_keys[i].split('-')
    
#     # Check if the current time slice in L1 overlaps with the current time slice in L2
#     if int(current_start_L1) <= int(end_time_L2) and int(start_time_L2) <= int(current_end_L1):
#         # Calculate the start and end times of the overlapping time slice
#         overlapping_start = max(int(start_time_L1), int(start_time_L2))
#         overlapping_end = min(int(end_time_L1), int(end_time_L2))
        
#         # Add the overlapping time slice to the list
#         overlapping_times.append(f"{overlapping_start}-{overlapping_end}")
    
#     # Update the start and end times of L1 for the next iteration
#     start_time_L1, end_time_L1 = current_start_L1, current_end_L1
    
#     # Check if we need to update the start and end times of L2 for the next iteration
#     if int(current_end_L1) > int(end_time_L2):
#         start_time_L2, end_time_L2 = L2_keys.pop(0).split('-')

# print(overlapping_times)

# helper(L1,L2)

# def helper2(L1,L2):
#     L1_keys = sorted(L1.keys(), key=lambda x: int(x.split('-')[0]))
#     L2_keys = sorted(L2.keys(), key=lambda x: int(x.split('-')[0]))
    
#     final_end = L1_keys[-1].split('-')[1]
#     current_end = L1_keys[0].split('-')[1]
#     current_start = 0
#     start_time_L1, end_time_L1 = L1_keys[0].split('-')
#     start_time_L2, end_time_L2 = L2_keys[0].split('-')
#     while current_end != final_end:
#         if int(end_time_L1) < int(start_time_L2) or int(end_time_L2) < int(start_time_L1):
#             break
#         else:
#             overlap_start = max(start_time_L1, start_time_L2)
#             overlap_end = min(end_time_L1, end_time_L2)
# # helper2(L1,L2)

def update_dict(original_dict, time_slice_duration):
    new_dict = {}
    for key, value in original_dict.items():
        start, end = key.split('-')
        start = int(start)
        end = int(end)
        while start < end:
            new_key = f"{start}-{start+time_slice_duration}"
            new_dict[new_key] = value
            start += time_slice_duration
    return new_dict

# L1 = {'0-30':2, '30-60':1.5, '60-90':1.75, '90-120':1.5, '120-150':2}
# L1 = update_dict(L1, 15)
# L2 = update_dict(L2, 15)

# def fuckthis(L1,L2,val):
#     new_dict = {}
#     for key in L1:
#         val *= L1[key]
#         val *= L2[key]
#         new_dict[key] = val
        
#     print(val)
        
# # print(L1)
# fuckthis(L1,L2,1)

# print(5)