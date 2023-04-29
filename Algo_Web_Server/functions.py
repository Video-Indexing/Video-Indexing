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
seconds = 120
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
    final_index = final_indexing(audio_results,classes,images_results)
    # ret_dic = {"audio results": audio_results, "images results": images_results}
    # ret_dic = {"audio results": audio_results} # audio tests
    # ret_dic = {"images results": images_results} # images tests.
    ret_dic = {"Final indexing": final_index} # final indexing tests
    os.remove(video_path)
    return ret_dic


def split_audio():
    seconds = 60
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
    class_renamed = ['Decision-Trees', 'Linear-Regression', 'Logistic-Regression', 'neural-network', 'Support-Vector-Machines', 'K-nearest-neighbors']
    audio_results = update_dict(audio_results,15)
    images_results = update_dict(images_results,15)
    final_dict = calculate_new_results(audio_results,images_results,class_renamed)
    final_dict = connect_time_slices(final_dict)
    return final_dict

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
    
def calculate_new_results(aud_dict,imgs_dict,classes):
    final_dict = {}
    multiplier = 0.2
    for key1, key2 in zip(aud_dict.keys(), imgs_dict.keys()):
        audio_array = aud_dict[key1]
        image_array = imgs_dict[key2]
        for key in image_array:
            index = classes.index(key)
            val = image_array[key]
            audio_array[index] *= (1 + (val * multiplier))
        # print(key2, value2)
        # max_index = audio_array.index(max(audio_array))
        max_index = audio_array.argmax()
        final_dict[key1] = classes[max_index]
        
    return final_dict
    
def connect_time_slices(final_dict):
    new_dict = {}
    counter = 0
    start = 0
    end = 0
    last_subject = None
    for time in final_dict:
        counter += 1
        start_time, end_time = time.split('-')
        subject = final_dict[time]
        if last_subject == None:
            last_subject = subject
        if final_dict[time] == last_subject:
           end = end_time
           if counter == len(final_dict):
                key = f'{start}-{end}'
                new_dict[key] = last_subject
           continue
        else:
            key = f'{start}-{end}'
            new_dict[key] = last_subject
            last_subject = final_dict[time]
            start = start_time
            end = end_time
            
    return new_dict
    
