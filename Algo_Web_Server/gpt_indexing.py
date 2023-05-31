import openai
from apikey import api_key as ak
from apikey import api_key2 as ak2
from apikey import api_key3 as ak3
import ast
import os
import json
# openai.api_key = ak

api_key_list = [ak,ak2,ak3]


my_subject_list = ["Introduction","Conclusion","Points", "Lines", "Planes" ,"Midpoint", "Distance Formulas",

  "Classify Angles" , "Classify Polygons", "Perimeter", "Circumference", "Area", " Conditional Statements","Pairs of Lines", "Pairs of Angles", "Parallel Lines", "Transversals","Triangle Sum Properties", "Congruent by SSS", "Congruent by SAS", "Congruent by ASA",
  "Congruent by AAS", "Equilateral Triangles","Perpendicular Bisectors", "Angle Bisectors of Triangles", "Medians", "Altitudes","Similar Polygons", "Triangles Similar by AA", "Triangles Similar by SSS", "Triangles Similar by SAS","Sine Ratio", "Cosine Ratio", "Tangent Ratio"]

chunkk = "And we know it looks something like this, but when you identify a line, you want to use two points that are on the line. Like, say, for example, if you have a point x and y that are on the line, the way you write at the notation, it's kind of like a pictograph, you know, or a picture, like,"


def send_prompt(subjects,chunks,api_key):
    openai.api_key = api_key
    subjects_str = ""
    for sub in  subjects:
        subjects_str += sub + "\n"
        
    # prompt = f"""
    # lets play game - rules:
    # 1. you get as input json key - chunk number and value : {chunks}, and subjects list -\n {subjects_str}.
    # 2. output(the value that you return as answer) give me back json in single line that the key is the chunk number and
    #     the value is the subject that you choose as the most fit to relate with this chunk from the list that you get.
    # 3. one more rule and the most important - you can't chose anything except subjects from the subjects list!
    # """
    
    prompt = f"""Given a JSON object with numerical keys and text values extracted from a video, your goal is to classify the text using a known subject list. The output should be a JSON object containing a single subject from the list corresponding to the input key-value pairs. If there is no exact match for a text, you can use previously classified subjects to classify the unknown subject. However, if the subject is already known, classify it regularly without considering the previous subjects. The output format should be in the form of a dictionary where the numerical keys represent the input keys, and the values represent the classified subjects.
    Subject List: {subjects_str}
    Input JSON: {chunks}
    Example output:
    {{"1": "Scale Factor","2": "Angle Angle Similarity","3": "Similar Triangles"}}
    Please ensure that the output consists solely of the JSON object with the classified subjects.
    """

    
    
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.3,
        messages=[
            {"role": "user",
             "content": prompt}]
    )

    response = str(output["choices"][0]["message"]["content"])
    results = ast.literal_eval(response)

    json_result = {}
    
    for i in results:
        if str(results[i]) in subjects:
            json_result[i] = str(results[i])
        else:
            json_result[i] = results[i]
            
    json_result = remove_unknown(json_result)

    return json_result



def gpt_index_video(chunks:list,subjects):
    dict_list = []
    dict_counter = 0
    chunk_dict = {}
    counter = 1
    for chunk in chunks:
        if dict_counter % 15 == 0:
            new_dict = {}
            dict_list.append(new_dict)
        # chunk_dict[counter] = chunk
        new_dict[counter] = chunk
        counter += 1
        dict_counter += 1
        
    # results = send_prompt(subjects, chunk_dict)
    api_counter = 0
    results_dict = {}
    for dic in dict_list:
        api_key = api_key_list[api_counter//3]
        res = send_prompt(subjects, dic,api_key)
        results_dict.update(res)
        api_counter += 1
    print(results_dict)
        
    return results_dict



def remove_unknown(results: dict):
    new_results = results.copy()
    keys = results.keys()
    for key in keys:
        if new_results[key] == 'Not Similar':
            new_results[key] = new_results[str(int(key)-1)]
            
    return new_results

            


# new_chunks = ["forever and ever like on this flat surface at that level. But when you label a plane you can either use like a capital letter like it will indicate in like the one of the corners of the plane. So for example I could call this plane M or what you can do is you can pick ",
#  "Three points that are not in a straight line. Say for example, like if this is a, b, and c, I could write this as plain, a, b, c. That's another way to do it. But you want to make sure that they're not in a straight line. Now why? Why do you not want them to be in a straight line? "]
