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
    # def __init__(self, df):
    def __init__(self):
        # df = create_database(data,data_labels)
        # random_number = random.randint(1, 150)
        # X_train, X_test, y_train, y_test = train_test_split(df['sentence'], df['class'], test_size=0.2, random_state=random_number)
        # vectorizer = TfidfVectorizer()
        # X_train = vectorizer.fit_transform(X_train)
        # X_test = vectorizer.transform(X_test)
        # svm = LinearSVC()
        # # svm = LinearSVC(multi_class='crammer_singer',penalty='l1',dual=False,tol=0.005)
        # svm.fit(X_train, y_train)
        # y_pred = svm.predict(X_test)
        # accuracy = accuracy_score(y_test, y_pred)
        # print("Training Accuracy:", accuracy)
        # with open('Algo_Web_Server/Model_dir/svm_clean_model.pkl', 'wb') as f:
        #   pickle.dump(svm, f)
        # with open('Algo_Web_Server/Model_dir/tfidf_clean_vectorizer.pkl', 'wb') as f:
        #   pickle.dump(vectorizer, f)
        # print(os.getcwd())
        
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
            # prev_output_index = np.argwhere(labels == self.previous_result)[0][0]
            # probs[0][prev_output_index] *= multiplier
            # max_index = np.argmax(probs)
            # output = labels[max_index]
            # self.previous_result = output
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

        # get the top 3 classes with the highest predicted probabilities
        # top_3_classes = probs.argsort()[0][-3:][::-1]
        print('Single pred result is:', output)
        return output
        # print('Single pred result is:', predicted_label)
        # return predicted_label


class SVC_Text_Model:
    def __init__(self, df):
        # df = create_database(data,data_labels)
        random_number = random.randint(1, 150)
        X_train, X_test, y_train, y_test = train_test_split(df['sentence'], df['class'], test_size=0.2,
                                                            random_state=random_number)
        vectorizer = TfidfVectorizer()
        X_train = vectorizer.fit_transform(X_train)
        X_test = vectorizer.transform(X_test)
        svc = SVC(kernel='linear')
        # svm = LinearSVC(multi_class='crammer_singer',penalty='l1',dual=False,tol=0.005)
        svc.fit(X_train, y_train)
        y_pred = svc.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Training Accuracy:", accuracy)
        self.svm = svc
        self.vectorizer = vectorizer

    def SVC_Single_Pred(self, text):
        new_text_transformed = self.vectorizer.transform([text])
        predicted_label = self.svc.predict(new_text_transformed)[0]
        decision_scores = self.svc.decision_function(new_text_transformed)

        # convert decision function scores to probabilities using softmax function
        probs = np.exp(decision_scores) / np.sum(np.exp(decision_scores), axis=1)

        # get the top 3 classes with the highest predicted probabilities
        # top_3_classes = probs.argsort()[0][-3:][::-1]
        print('Single pred result is:', predicted_label)


class KKN_Text_Model():
    def __init__(self, data, data_labels):
        df = create_database(data, data_labels)
        random_number = random.randint(1, 150)
        X_train, X_test, y_train, y_test = train_test_split(df['sentence'], df['class'], test_size=0.2,
                                                            random_state=random_number)
        vectorizer = TfidfVectorizer()
        X_train = vectorizer.fit_transform(X_train)
        X_test = vectorizer.transform(X_test)
        neigh = KNeighborsClassifier(n_neighbors=25)
        neigh.fit(X_train, y_train)
        y_pred = neigh.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Training Accuracy:", accuracy)
        self.knn = neigh
        self.vectorizer = vectorizer

    def KNN_Single_Pred(self, text):
        new_text_transformed = self.vectorizer.transform([text])
        predicted_label = self.knn.predict(new_text_transformed)[0]
        print('Single pred result is:', predicted_label)


class MLP_Text_Model():
    def __init__(self, data, data_labels):
        df = create_database(data, data_labels)
        random_number = random.randint(1, 150)
        X_train, X_test, y_train, y_test = train_test_split(df['sentence'], df['class'], test_size=0.2,
                                                            random_state=random_number)
        vectorizer = TfidfVectorizer()
        X_train = vectorizer.fit_transform(X_train)
        X_test = vectorizer.transform(X_test)
        clf = MLPClassifier(random_state=random_number, max_iter=200, activation='tanh', learning_rate_init=0.005).fit(
            X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Training Accuracy:", accuracy)
        self.clf = clf
        self.vectorizer = vectorizer

    def MLP_Single_Pred(self, text):
        new_text_transformed = self.vectorizer.transform([text])
        predicted_label = self.clf.predict(new_text_transformed)[0]
        print('Single pred result is:', predicted_label)


class DTC_Text_Model():
    def __init__(self, data, data_labels):
        df = create_database(data, data_labels)
        random_number = random.randint(1, 150)
        X_train, X_test, y_train, y_test = train_test_split(df['sentence'], df['class'], test_size=0.2,
                                                            random_state=random_number)
        vectorizer = TfidfVectorizer()
        X_train = vectorizer.fit_transform(X_train)
        X_test = vectorizer.transform(X_test)
        clf = DecisionTreeClassifier(random_state=random_number)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Training Accuracy:", accuracy)
        self.clf = clf
        self.vectorizer = vectorizer

    def DTC_Single_Pred(self, text):
        new_text_transformed = self.vectorizer.transform([text])
        predicted_label = self.clf.predict(new_text_transformed)[0]
        print('Single pred result is:', predicted_label)


class AdaBoost_Text_Model():
    def __init__(self, data, data_labels):
        df = create_database(data, data_labels)
        random_number = random.randint(1, 150)
        X_train, X_test, y_train, y_test = train_test_split(df['sentence'], df['class'], test_size=0.2,
                                                            random_state=random_number)
        vectorizer = TfidfVectorizer()
        X_train = vectorizer.fit_transform(X_train)
        X_test = vectorizer.transform(X_test)
        clf = AdaBoostClassifier(n_estimators=100, random_state=random_number, learning_rate=0.1)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Training Accuracy:", accuracy)
        self.clf = clf
        self.vectorizer = vectorizer

    def AdaBoost_Single_Pred(self, text):
        new_text_transformed = self.vectorizer.transform([text])
        predicted_label = self.clf.predict(new_text_transformed)[0]
        print('Single pred result is:', predicted_label)

# class SGD_Text_Model():
#     def __init__(self, df):
#         random_number = random.randint(1, 150)
#         X_train, X_test, y_train, y_test = train_test_split(df['sentence'], df['class'], test_size=0.2,
#                                                             random_state=random_number)
#         vectorizer = TfidfVectorizer()
#         X_train = vectorizer.fit_transform(X_train)
#         X_test = vectorizer.transform(X_test)
#         clf = SGDClassifier(loss='hinge', alpha=0.0001, random_state=42)
#         clf.fit(X_train, y_train)
#         y_pred = clf.predict(X_test)
#         accuracy = accuracy_score(y_test, y_pred)
#         print("Training Accuracy:", accuracy)
#         self.clf = clf
#         self.vectorizer = vectorizer

#     def SGD_Single_Pred(self, text):
#         new_text_transformed = self.vectorizer.transform([text])
#         predicted_label = self.clf.predict(new_text_transformed)[0]
#         print('Single pred result is:', predicted_label)


# df = create_database(dataset, data_labels)


# vid_text = [
#     "Stack Quest, Stack Quest, Stack Quest, Stack Quest. Hello and welcome to Stack Quest. Stack Quest is brought to you by the friendly folks in the genetics department at the University of North Carolina at Chapel Hill. Today we're going to be talking about the Cane-Nearest Neighbors Algorithm, which is a super simple way to classify data. In a nutshell, if you already had a lot of data that defined these cell types, we could use it to decide which type of cell this guy is. Let's see it in action. Step 1. Start with a data set with known categories. In this case, we have different cell types from an intestinal tumor. We then cluster that data. In this case, we used PCA. Step 2. Add a new cell with unknown category to the plot. We don't know this cell's category because it was taken from another tumor where the cells were not properly sorted. So what we want to do is we want to classify this new cell. We want to figure out what cell it's most similar to and then we're going to call it that type of cell. Step 3. We classify the new cell by looking at the nearest annotated cells, i.e., the nearest neighbors. If the k in k nearest neighbors is equal to 1, then we will only use the nearest neighbor to define the category. In this case, the category is green because the nearest neighbor is already known to be the green cell type. If k equals 11, we would use the 11 nearest neighbors. In this case, we would use the nearest neighbor's.",
#     "The category is still green because the 11 cells that are closest to the unknown cell are already green. Now the new cell is somewhere more interesting. It's about halfway between the green and the red cells. If k equals 11 and the new cells between two or more categories, we simply pick the category that gets the most votes. In this case, seven nearest neighbors are red. Three nearest neighbors are orange. One nearest neighbor is green. Since red got the most votes, the final assignment is red. This same principle applies to heat maps. This heat map was drawn with the same data and clustered using hierarchical clustering. If our new cell ended up in the middle of the light blue cluster and, if k equals 1, we just look at the nearest cell and that cell is light blue. So we classify the unknown cell as a light blue cell. If k equals 5, we'd look at the five nearest cells, which are also light blue. So we'd still classify the unknown cell as light blue. If the new cell ended up closer to the edge of the light blue cells and k equals 11, then we take a vote. Seven nearest neighbors are light blue and four are light green. So we'd still go with light blue. If the new cell is right between two categories, well, if k is odd, then we can avoid a lot of ties. If we still get a tied vote, we can flip a coin or decide not to assign the cell to a category. Before we go, let's talk about a little machine learning slash data.",
#     "terminology. The data used for the initial clustering, the data where we know the category is in advance, is called training data. Bam! A few thoughts on picking a value for K. There is no physical or biological way to determine the best value for K, so you may have to try out a few values before settling on one. Do this by pretending part of the training data is unknown. And then what you do is you categorize that unknown data using the K nearest neighbor algorithm and you assess how good the new categories match what you know already. Low values for K, like K equals 1 or K equals 2, can be noisy and subject to the effects of outliers. Large values for K smooth over things, but you don't want K to be so large that it can be a category with only a few samples in it will always be outvoted by other categories. Hooray! We've made it to the end of another exciting stat quest. If you like this stat quest, go ahead and subscribe to my channel and you'll see more like it. And, if you have any ideas of things you'd like me to do a stat quest on, feel free to put those ideas in the comments. Okay, that's it. Tune in next time for another exciting stat quest."
# ]

# # SGD = SGD_Text_Model(df)
# # for text in vid_text:
# #     result = SGD.SGD_Single_Pred(text)

# SVM = SVM_Text_Model()
# for text in vid_text:
#     result = SVM.svm_single_pred(text)