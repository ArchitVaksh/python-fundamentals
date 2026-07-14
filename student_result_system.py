def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def is_pass(marks):
    return "Pass" if marks >= 40 else "Fail"


def display_result(name, marks):
    grade = calculate_grade(marks)
    status = is_pass(marks)

    result = (
        f"Name   : {name}\n"
        f"Marks  : {marks}\n"
        f"Grade  : {grade}\n"
        f"Status : {status}"
    )

    return result


print(display_result("Archit", 98))
print()
print(display_result("Rahul", 66))