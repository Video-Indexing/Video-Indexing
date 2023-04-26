import os
from sys import platform

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
import pickle
from sklearn.linear_model import SGDClassifier
from text_dataset import *


def create_database(data, data_labels):
    new_data = {'sentence': [], 'class': []}
    i = 0
    for sub in data:
        for text in sub:
            new_data['sentence'].append(text)
            new_data['class'].append(data_labels[i])
        i += 1

    df = pd.DataFrame(new_data)
    return df


class SVM_Text_Model:
    def __init__(self):
        
        # Algo_Web_Server
        if platform == "win32":
            # svm_path = os.getcwd() + "/Model_dir/svm_clean_model.pkl"
            # tfidf_path = os.getcwd() + "/Model_dir/tfidf_clean_vectorizer.pkl"
            svm_path = "Algo_Web_Server\Model_dir\svm_clean_model.pkl"
            tfidf_path = "Algo_Web_Server\Model_dir\\tfidf_clean_vectorizer.pkl"
        else:
            svm_path = os.getcwd() + "/Model_dir/svm_clean_model.pkl"
            tfidf_path = os.getcwd() + "/Model_dir/tfidf_clean_vectorizer.pkl"
            # svm_path = "Algo_Web_Server\Model_dir\svm_clean_model.pkl"
            # tfidf_path = "Algo_Web_Server\Model_dir\\tfidf_clean_vectorizer.pkl"
        with open(svm_path, 'rb') as f:
            svm = pickle.load(f)

        with open(tfidf_path, 'rb') as f:
            vectorizer = pickle.load(f)
        self.svm = svm
        self.vectorizer = vectorizer
        self.previous_result = 'None'
        self.prev_list = []

    def svm_single_pred(self, text):
        multiplier = 1.35
        size = 3
        labels = self.svm.classes_
        
        new_text_transformed = self.vectorizer.transform([text])
        predicted_label = self.svm.predict(new_text_transformed)[0]
        decision_scores = self.svm.decision_function(new_text_transformed)

        # convert decision function scores to probabilities using softmax function
        probs = np.exp(decision_scores) / np.sum(np.exp(decision_scores), axis=1)
        if self.previous_result == 'None':
            max_index = np.argmax(probs)
            output = labels[max_index]
            self.previous_result = output
            self.prev_list.append(output)
        else:
            for prev in self.prev_list:
                prev_output_index = np.argwhere(labels == prev)[0][0]
                probs[0][prev_output_index] *= multiplier
            max_index = np.argmax(probs)
            output = labels[max_index]
            self.previous_result = output
            if len(self.prev_list) == size:
                self.prev_list.pop(0)
                self.prev_list.append(output)
            else:
                self.prev_list.append(output)

        print('Single pred result is:', output)
        return output
    
        # print('Single pred result is:', predicted_label)
        # return predicted_label
