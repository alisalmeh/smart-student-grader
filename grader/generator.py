def get_student_data():
    students = {}
  
    print("\nEnter student names and scores.")

    while True:
        name = input("Enter student name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break

        try:
            scores_input = input("Enter 3 scores separated by space (e.g. 38 75 91): ")
            scores = list(map(int, scores_input.strip().split()))

            if len(scores) != 3:
                print("Please enter exactly 3 scores")
                continue
                            
            students[name] = scores

        except ValueError:
            print("Invalid input. Only number!")

    return students