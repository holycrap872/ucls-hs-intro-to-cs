#!/usr/bin/env python3
import argparse
import csv


BOILER_INTRO = """<b>Midterm Status:</b>  Satisfactory/Above Satisfactory\n\nIn Introduction to Computer Science we have wrapped up our first unit of study in which we explore numbering systems and how computers store various types of information such as text, images, and emojis. We have now turned our focus to learning how to program in Python. This will include learning the specific syntax of Python as well as how to utilize the control structures (e.g., loops, conditionals) that are common in many other languages. These topics can often be difficult, so I encourage you to take advantage of the extra support available outside of class held in C222 every Wednesday, Thursday, and Friday."""


def produce_narrative(student_dict) -> None:
    name = student_dict["First Name"]

    hw_list = []
    for k in student_dict:
        if not any(p in k for p in ["Assignment", "Homework"]):
            continue

        try:
            hw_list.append(float(student_dict[k]))
        except:
            continue
    print(hw_list)
    hw_average = sum(hw_list) / len(hw_list)

    quiz_list = [float(student_dict[k]) for k in student_dict if k.startswith("Mastery")]
    quiz_average = sum(quiz_list) / len(quiz_list)
    if quiz_average > 100.0:
        quiz_average = 100.0

    exam_list = [float(student_dict[k]) for k in student_dict if k.startswith("Exam")]
    exam_average = sum(exam_list) / len(exam_list)

    overall_grade = float(student_dict["Overall"])

    print("-" * 80)
    print(f"{BOILER_INTRO}\n")
    print(f"- Homework Grade: {hw_average:.1f}")
    print(f"- Quizzes Grade: {quiz_average:.1f}")
    print(f"- Exam Grade: {exam_average:.1f}\n")
    print(f"Weighted overall: {overall_grade:.1f}\n")

    if overall_grade > 93:
        if 95 < hw_average and 93 < exam_average:
            print(f"{name}, you're off to a very good start. You did great on the exam and you're consistent with your homework. Keep up the good work!")
        elif 85 < hw_average < 92 and 93 < exam_average:
            print(f"{name}, you're off to a very good start. You did really well on the exam and quizzes. If you focus on being a bit more consistent with your homework, you will really excel. Keep up the good work!")
        elif 95 < hw_average and 87 < exam_average:
            print(f"{name}, you're off to a very good start. You do a great job consistently completely the homework and you did well on the exam. I encourage you, however, you come see me before the next test with any questions you might have to really push your understanding to the next level.")
        else:
            print(f"{name} grade > 95")
    elif overall_grade > 90:
        if 95 < hw_average and 85 < exam_average < 90:
            print(f"{name}, you're off to a very good start. You are very consistent with your homework and you've done well on the exams/quizzes. I encourage you to come see me if you have any questions prior to tests just to make sure to clear up any questions, but overall, you're on a good path.")
        elif 85 < hw_average < 90 and 90 < exam_average:
            print(f"{name}, you did well on the exam. I encourage you to be a bit more consistent with your homwork, though, to allow you to really expand your understanding of the material.")
        elif exam_average > 95 and 75 < hw_average and hw_average < 90:
            print(f"{name}, you did really well on the exam, showing a good understanding of the material. I encourage you to focus a bit more on consistency with your homework, though")
        else:
            print(f"{name}, TODO grade > 90")
    elif overall_grade > 83:
        if 80 < exam_average < 89 and 70 < hw_average < 90:
            print(f"{name}, I encourage you to focus a bit more on consistency with your homework. Taking the homework more seriously will allow you to see where you might have misunderstandings and come see me for clarification.")
        elif 90 < hw_average and 70 < exam_average < 80:
            print(f"{name}, I commend you on you consistently completing the homework with thoroughness and care. There was room for improvement on the exam, though, so I encourage you to come see me with any questions you might have prior to our next test.")
        else:
            print(f"{name}, TODO grade > 83")
    else:
        print(f"{name}, you're TODO")

    print("-" * 80)


def produce_grade_reports(csv_path: str) -> None:
    students = []
    with open(csv_path, "r") as csv_fp:
        reader = csv.DictReader(csv_fp)
        for row in reader:
            students.append(row)
    print(len(students))

    for student in students:
        produce_narrative(student)
        input("\n\n\n\n\nHit enter for next\n\n\n\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path to .csv file", type=str, required=True)
    args = parser.parse_args()

    produce_grade_reports(args.path)
