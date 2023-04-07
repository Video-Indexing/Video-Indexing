import os
import whisper


class Whisper_Model:
    def __init__(self,version,audio_path):
        self.version = version
        self.model = whisper.load_model(version)
        self.audio_path = audio_path
        self.text_array = []
        
    def Text_To_Speech(self):
        for file_name in sorted(os.scandir(self.audio_path), key=lambda f: f.stat().st_ctime):
            file = os.path.join(self.audio_path, file_name)
            # send the mp3 file into whisper
            result = self.model.transcribe(file)
            text = result["text"]
            
            # save the text in our array
            self.text_array.append(text)
        
        return self.text_array
            
    def Print_Chunks(self):
        counter = 1    
        for text in self.text_array:
            print('Chunk number:',counter,' Text:',text)
            print('**'*20)
            counter += 1
            
    def Print_Entire_Text(self):
        for text in self.text_array:
            print(text)
            
    def Print_Results(self):
        self.Print_Chunks()
        # self.Print_Entire_Text()