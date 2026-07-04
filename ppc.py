def cgpa_calculator():
    print("=== PERSONAL POCKET CGPA CALCULATOR (PPC) ===")
    print("Keep track of your academic performance on the go!\n")
    
    try:
        total_semesters = int(input("How many semesters do you want to calculate for? "))
    except ValueError:
        print("Please enter a valid whole number for semesters.")
        return

    total_credit_units = 0
    total_quality_points = 0

    # Loop through each semester
    for semester in range(1, total_semesters + 1):
        print(f"\n--- Semester {semester} ---")
        try:
            num_courses = int(input(f"How many courses did you take in Semester {semester}? "))
        except ValueError:
            print("Invalid number of courses. Skipping this semester.")
            continue

        # Loop through each course in the semester
        for course in range(1, num_courses + 1):
            print(f"\nCourse {course}:")
            
            try:
                units = int(input("  Enter Course Credit Units (e.g., 2, 3, 4): "))
            except ValueError:
                print("  Invalid credit units. Setting to 0 for safety.")
                units = 0
                
            grade = input("  Enter Letter Grade (A, B, C, D, E, F): ").strip().upper()

            # Selection Control Statements to assign point values based on grade
            if grade == 'A':
                points_per_unit = 5
            elif grade == 'B':
                points_per_unit = 4
            elif grade == 'C':
                points_per_unit = 3
            elif grade == 'D':
                points_per_unit = 2
            elif grade == 'E':
                points_per_unit = 1
            elif grade == 'F':
                points_per_unit = 0
            else:
                print(f"  Warning: Unknown grade '{grade}'. Calculated as 0 points.")
                points_per_unit = 0

            # Calculate Quality Points for this course (Units * Grade Points)
            course_quality_points = units * points_per_unit
            
            # Add to cumulative totals
            total_credit_units += units
            total_quality_points += course_quality_points

    # Final CGPA Calculation (Total Quality Points / Total Credit Units)
    print("\n======================================")
    print("          FINAL CGPA REPORT           ")
    print("======================================")
    print(f"Total Credit Units Accumulated: {total_credit_units}")
    print(f"Total Quality Points Earned:    {total_quality_points}")
    
    if total_credit_units > 0:
        cgpa = total_quality_points / total_credit_units
        print(f"Your Personal Pocket CGPA is:   {round(cgpa, 2)} / 5.00")
        
        # Performance feedback selection statement
        if cgpa >= 4.50:
            print("Class: First Class! Exceptional work! 🌟")
        elif cgpa >= 3.50:
            print("Class: Second Class Upper. Strong performance! 👍")
        elif cgpa >= 2.40:
            print("Class: Second Class Lower. Good job.")
        elif cgpa >= 1.50:
            print("Class: Third Class. You can bring this up!")
        else:
            print("Class: Pass/Fail. Seek academic advice.")
    else:
        print("No valid credit units were entered, cannot compute CGPA.")
    print("======================================")

# Run the CGPA calculator
cgpa_calculator()
