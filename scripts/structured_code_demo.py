# -----------------------------
# Imports (none needed here)
# -----------------------------

# -----------------------------
# Configuration / Setup
# -----------------------------
student_names = ["Arun", "Bala", "Charan"]
marks = [85, 72, 90]

# -----------------------------
# Helper Functions
# -----------------------------

def calculate_average(marks_list):
    """Calculate average marks"""
    total_marks = sum(marks_list)
    average_marks = total_marks / len(marks_list)
    return average_marks


def get_grade(score):
    """Return grade based on score"""
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"


def display_student_results(names, scores):
    """Display student names with grades"""
    for i in range(len(names)):
        grade = get_grade(scores[i])
        print(f"{names[i]} scored {scores[i]} -> Grade {grade}")


# -----------------------------
# Main Execution
# -----------------------------
def main():
    print("Student Results:\n")

    # Display individual results
    display_student_results(student_names, marks)

    # Calculate and display average
    avg = calculate_average(marks)
    print(f"\nClass Average: {avg}")


# -----------------------------
# Program Entry Point
# -----------------------------
if __name__ == "__main__":
    main()