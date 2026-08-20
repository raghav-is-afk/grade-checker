#grading program with loop to allow multiple inputs until user decides to quit


while True:
    user_input = input("Enter your score (or type 'q' to quit): ")

    if user_input.lower() == 'q':
        print("Program stopped.")
        break

    score = int(user_input)

    if 90 <= score <= 100:
        grade = 'A'
    elif 80 <= score <= 89:
        grade = 'B'
    elif 70 <= score <= 79:
        grade = 'C'
    elif 60 <= score <= 69:
        grade = 'D'
        if score == 69:
            print('haha you cheeky bastard')
    elif 50 <= score <= 59:
        grade = 'F'
    else:
        print('You have FAILED')
        continue   # skip printing grade if failed

    print(f'Your grade is {grade}\n')
