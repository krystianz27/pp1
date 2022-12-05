def f(age, course, average):
    import json
    with open("test.json", encoding="utf-8") as file:
        data = json.load(file)

    count = 0

    for student in data:
        if student["age"] >= age:
            if "studies" in student:
                for student_course in student["studies"]["courses"]:
                    if student_course["name"] == course:
                        grade_sum = sum(student_course["grades"])
                        grade_count = len(student_course["grades"])
                        grade_average = grade_sum / grade_count

                        if grade_average >= average:
                            count += 1
    return count

print(f(21, "statistics", 4))