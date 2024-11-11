# TODO решите задачу
import json
def task() -> float:
    summ = 0
    with open("input.json") as f:
        python_sw = json.load(f)
        for i in python_sw:
            summ += (i.get("score") * i.get("weight"))
    return round(summ, 3)


print(task())
