from empath import Empath
from sys import argv

ta = Empath()

def cout_paragraph_subjects(data):
    subjects = data["subjects"]
    return {
        "subjects": subjects,
        "weight": len(subjects),
        "paragraph": data["paragraph"]
    }

def sum_paragraph_subjects_weights(data):
    subjects = data["subjects"]
    weight = 0
    for subject in subjects:
        weight += subject[1]
    return {
        "subjects": subjects,
        "weight": int(weight),
        "paragraph": data["paragraph"]
    }

def get_best_by_weight(data):
    result = {
        "weight": 0,
    }
    for selected_data in data:
        if (result["weight"] < selected_data["weight"]) :
            result = selected_data
    return result

def dict_to_list(converting_dict):
    converted_list = []
    for key in converting_dict:
        converted_list.append([
            key,
            converting_dict[key]
        ])
    return converted_list

def trim_text(text):
    # Stage 1: paragraph analyze and getting subjects
    paragraph_subjects = [
        {
            "subjects":[
                item
                for item in dict_to_list(
                    ta.analyze(paragraph)
                )
                if item[1] > 0
            ],
            "paragraph":paragraph
        }
        for paragraph in text.split(".")
        if paragraph
    ]
    # Stage 2: set weight for paragraphs
    paragraph_weights = []
    paragraph_weights.append(
        list(map(cout_paragraph_subjects ,paragraph_subjects))
    )
    paragraph_weights.append(
        list(map(sum_paragraph_subjects_weights ,paragraph_subjects))
    )
    # Stage 3: trimming the best part
    trimes = []
    for weight_data in paragraph_weights:
        trimed = get_best_by_weight(weight_data)
        if trimed in paragraph_weights: continue
        trimes.append(trimed)
    return trimes

if len(argv) > 1:
    text = argv[1]
    print(
        trim_text(text)
    )
