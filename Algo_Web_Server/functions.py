from video_downloader import Video_Downloader
from audios_downloader import Audio_Downloader
from whisper_model import Whisper_Model
from images_downloader import Image_Downloader
from models import *
import os
from sys import platform
from images_reco import recognize_new_image


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
    audio_results = model_results(results)
    # print(audio_results)
    images_results = recognize_images()
    ret_dic = {"audio results": audio_results, "images results": images_results}
    # ret_dic = {"audio results": audio_results} # audio tests
    # ret_dic = {"images results": images_results} # images tests.
    os.remove(video_path)
    return ret_dic


def split_audio():
    seconds = 120
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

    return dic_results


def recognize_images():
    ImageDownloader = Image_Downloader(vid_name, content_path, images_path, 20)
    ImageDownloader.download_images()
    prediction = {}
    i = 0
    if platform == "win32":
        df_path = os.getcwd() + "\Model_dir\embedding_ConvNeXtBase_ex2.csv"
    else:
        df_path = os.getcwd() + "/Model_dir/embedding_ConvNeXtBase_ex2.csv"
    df = pd.read_csv(df_path)
    for image in os.listdir(images_path):
        if platform == "win32":
            img_path = images_path + f"\{image}"
        else:
            img_path = images_path + f"/{image}"
        prediction[str(i)] = recognize_new_image(df, img_path)
        i += 1

    ImageDownloader.delete_images()
    return prediction

