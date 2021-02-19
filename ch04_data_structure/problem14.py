# 14 -1
student_list = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}


def get_student_name(student_no):
    try:
        return student_list[student_no]
    except KeyError:
        return "?"


print(get_student_name(39))
print(get_student_name(241))