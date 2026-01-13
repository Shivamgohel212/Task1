def to_json(x):
    if type(x) == list:
        return "[" + ", ".join(to_json(i) for i in x) + "]"

    if type(x) == dict:
        return "{" + ", ".join('"' + k + '": ' + to_json(v) for k, v in x.items()) + "}"

    return '"' + str(x) + '"'


data = {
    "name": "Amit",
    "skills": ["Python", "Java"],
    "marks": {"math": 90, "science": 85}
}
print(to_json(data))
