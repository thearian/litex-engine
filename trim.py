from empath import Empath
import time

ta = Empath()
text = open('file.txt','rt').read()

start = time.time()

def cout_paragraph_subjects(data):
    subjects = data["subjects"]
    subjects = [ {name: subjects[name]} for name in subjects if subjects[name] > 0]
    return {
        "data": data,
        "weight": len(subjects),
        "paragraph": data["paragraph"]
    }

def sum_paragraph_subjects_weights(data):
    subjects = data["subjects"]
    subjects = [ {name: subjects[name]} for name in subjects if subjects[name] > 0]
    weight = 0
    for name in data["subjects"]:
        weight += data["subjects"][name]
    return {
        "data": data,
        "weight": weight,
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

# Stage 1: paragraph analyze and getting subjects
paragraph_subjects = [ {"subjects":ta.analyze(paragraph), "paragraph":paragraph} for paragraph in text.split("\n") if paragraph ]
# Stage 2: set weight for paragraphs
paragraph_weights_1 = list(map(cout_paragraph_subjects ,paragraph_subjects))
paragraph_weights_2 = list(map(sum_paragraph_subjects_weights ,paragraph_subjects))
# Stage 3: trimming the best part
litex_1 = get_best_by_weight(paragraph_weights_1)
litex_2 = get_best_by_weight(paragraph_weights_2)

print(litex_1["paragraph"],"\n")
print(litex_2["paragraph"],"\n")
print(time.time() - start)