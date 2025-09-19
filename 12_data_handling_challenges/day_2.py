def collect_student_data():
    students: dict[str, float] = {}
    while True:
        name = input("Enter the student name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        if name in students:
            print("Student already exists.")
            continue
        
        try:
            marks = float(input(f"Enter marks for {name}: "))
            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100.")
            students[name] = marks
        except ValueError as e:
            print(e)
    return students

def display_report(students: dict[str, float]):
    if not students:
        print("No students found.")
        return
    
    marks = list(students.values())
    max_mark = max(marks)
    min_mark = min(marks)
    total = sum(marks)
    average = total / len(marks)
    
    topper = [name for name , score in students.items() if score == max_mark]
    lower = [name for name , score in students.items() if score == min_mark]

    print(f"Topper: {', '.join(topper)}")
    print(f"Lower: {', '.join(lower)}")
    print(f"Total: {total}")
    print(f"Average: {average}")


students = collect_student_data()
display_report(students)