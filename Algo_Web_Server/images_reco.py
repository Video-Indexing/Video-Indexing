import os
import sys

from tensorflow.keras.applications.convnext import ConvNeXtBase, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors


def return_image_embedding(model, img_path, label=None):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    curr_df = pd.DataFrame(preds[0]).T
    if label is not None:
        curr_df["label"] = label
    return curr_df


def predict_single_img_knn(model, image, df, num_of_neigh):
    y = df["label"]
    x = df.drop("label", axis=1)
    knn = NearestNeighbors(n_neighbors=num_of_neigh, metric="cosine")
    knn.fit(x, y)
    img_emb = pd.DataFrame(return_image_embedding(model, image))
    res = knn.kneighbors(img_emb)
    neigh_label_arr = []
    for idx in res[1]:
        s = y.iloc[idx]
        neigh_label_arr = list(s)
    desicion = majority_voting(neigh_label_arr)
    return desicion


def majority_voting(prediction_label_arr):
    counter = 0
    label = prediction_label_arr[0]

    for element in prediction_label_arr:
        curr_frequency = prediction_label_arr.count(element)
        if curr_frequency > counter:
            counter = curr_frequency
            label = element

    return label


def recognize_new_image(df_path, img_to_rec):
    df = pd.read_csv(df_path)
    model = ConvNeXtBase(include_top=False, weights='imagenet', pooling='avg')
    k = 5
    prediction = predict_single_img_knn(model, img_to_rec, df, k)
    return prediction


if __name__ == "__main__":
    content_path = os.getcwd()
    pred = recognize_new_image(content_path + "\Model_dir\embedding_ConvNeXtBase_ex2.csv", content_path + "\Support-Vector-Machines1.jpg")
    print(pred)

