##==================================
## AWS Machine Learning Foundation Course
## Lesson - 2: Software Engineering Practices Pt II
## Year: 2020
## Sub-lesson: Unit Tests 
##===================================
def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    return 0 if (launch_day - current_day) < 0 else (launch_day - current_day)