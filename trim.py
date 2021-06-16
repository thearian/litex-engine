from empath import Empath
import time

ta = Empath()
text = open('file.txt','rt').read()

start = time.time()

def get_paragraph_weight(data):
    subjects = data["subjects"]
    subjects = [ {name: subjects[name]} for name in subjects if subjects[name] > 0]
    return {
        "data": data,
        "weight": len(subjects),
        "paragraph": data["paragraph"]
    }

# Stage 1: paragraph analyze and getting subjects
paragraph_subjects = [ {"subjects":ta.analyze(paragraph), "paragraph":paragraph} for paragraph in text.split("\n") if paragraph ]
# Stage 2: set weight for paragraphs
paragraph_weights = list(map(get_paragraph_weight ,paragraph_subjects))

result = {
    "data": None,
    "weight": 0,
}
for data in paragraph_weights:
    if (result["weight"] < data["weight"]) :
        result = data


print(
    result["paragraph"], "\n",
    time.time() - start
)