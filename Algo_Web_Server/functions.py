from video_downloader import Video_Downloader
from audios_downloader import Audio_Downloader
from whisper_model import Whisper_Model
from images_downloader import Image_Downloader
from models import *
import os

content_path = os.getcwd()
images_path = content_path + '\Images'
audios_path = content_path + '\Audios'
vid_name = 'video.mp4'
seconds = 120

if not os.path.exists('Images'):
    os.makedirs('Images')

if not os.path.exists('Audios'):
    os.makedirs('Audios')
    
subject_list = ['Backpropagation', 'Convolutional networks', 'Cross-entropy', 'Extension beyond sigmoid neurons', 'Gradient descent - general', 'Network’s hyper-parameters', 'Overfitting and regularization', 'Perceptrons', 'Sigmoid', 'Softmax', 'Stochastic gradient descent', 'The architecture of neural networks', 'The vanishing gradient problem', 'Weight initialization','KNN']

def download_vid(link):
    VideoDownloader = Video_Downloader(link,content_path,vid_name)
    audio_lenght = VideoDownloader.download_video()
    return audio_lenght
    
def index_video(link):
    audio_lenght = download_vid(link)
    split_audio()
    results = whisper_results()
    dic_results = model_results(results)
    print(dic_results)
    # images_download()
    return dic_results

def split_audio():
    seconds = 120
    AudioDownloader = Audio_Downloader(vid_name,content_path,audios_path,seconds)
    AudioDownloader.split_audio()
    # AudioDownloader.delete_audios()
    
def whisper_results():
    # Use whisper model to transcripte the mp3 audios
    WhisperModel = Whisper_Model('base',audios_path)
    results = WhisperModel.Text_To_Speech()
    AudioDownloader = Audio_Downloader(vid_name,content_path,audios_path,seconds)
    AudioDownloader.delete_audios()
    WhisperModel.Print_Results()
    
    return results
    
def images_download():
    ImageDownloader = Image_Downloader(vid_name,content_path,images_path,30)
    ImageDownloader.Download_Images()
    # ImageDownloader.Delete_Images()
    
def model_results(whisper_results):
    dic_results = {}
    # df = create_database(dataset,subject_list)
    # SVM = SVM_Text_Model(df)
    SVM = SVM_Text_Model()
    i = 0
    for chunk in whisper_results:
        print('Chunk start from:',i,' end in:',i + seconds)
        result = SVM.SVM_Single_Pred(chunk)
        print("*"*50)
        key = f'{i}-{i+seconds}'
        dic_results[key] = result
        i += seconds
        
    return dic_results
        
        