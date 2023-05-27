import openai
from apikey import api_key as ak
import ast
import os
import json
openai.api_key = ak


my_subject_list = ["Introduction","Conclusion","Points", "Lines", "Planes" ,"Midpoint", "Distance Formulas",

  "Classify Angles" , "Classify Polygons", "Perimeter", "Circumference", "Area", " Conditional Statements","Pairs of Lines", "Pairs of Angles", "Parallel Lines", "Transversals","Triangle Sum Properties", "Congruent by SSS", "Congruent by SAS", "Congruent by ASA",
  "Congruent by AAS", "Equilateral Triangles","Perpendicular Bisectors", "Angle Bisectors of Triangles", "Medians", "Altitudes","Similar Polygons", "Triangles Similar by AA", "Triangles Similar by SSS", "Triangles Similar by SAS","Sine Ratio", "Cosine Ratio", "Tangent Ratio"]

chunkk = "And we know it looks something like this, but when you identify a line, you want to use two points that are on the line. Like, say, for example, if you have a point x and y that are on the line, the way you write at the notation, it's kind of like a pictograph, you know, or a picture, like,"


def send_prompt(subjects,chunks):
    subjects_str = ""
    for sub in  subjects:
        subjects_str += sub + "\n"
    prompt = f"""
    lets play game - rules:
    1. you get as input json key - chunk number and value : {chunks}, and subjects list -\n {subjects_str}.
    2. output(the value that you return as answer) give me back json in single line that the key is the chunk number and
        the value is the subject that you choose as the most fit to relate with this chunk from the list that you get.
    3. one more rule and the most important - you can't chose anything except subjects from the subjects list!
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

    return json_result


# new_chunks = ["forever and ever like on this flat surface at that level. But when you label a plane you can either use like a capital letter like it will indicate in like the one of the corners of the plane. So for example I could call this plane M or what you can do is you can pick ",
#  "Three points that are not in a straight line. Say for example, like if this is a, b, and c, I could write this as plain, a, b, c. That's another way to do it. But you want to make sure that they're not in a straight line. Now why? Why do you not want them to be in a straight line? "]


def gpt_index_video(chunks:list,subjects):
    chunk_dict = {}
    counter = 1
    for chunk in chunks:
        chunk_dict[counter] = chunk
        counter += 1
        
    results = send_prompt(subjects, chunk_dict)
    print(results)
        
    return results


# gpt_index_video(new_chunks,my_subject_list)


