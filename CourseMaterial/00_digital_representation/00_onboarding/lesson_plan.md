## Essential Questions

- What are the topics covered by the course?
- What are the expectations of the class?

## Lesson Plan

The goal of this class is to set the standards and expectations for the rest
of the year. The class is intentionally boring to make clear that this class is
closer in tenor to a math class than a "fun elective".

### Setup

- 2x photo rosters printed out
    - One for attendance
    - One for "emergency book"
- Proper dates put into "Appointment Assignment"
- Dates added to Google Appointment Calendar that match those dates
- `onboarding_questionnaire` GoogleDoc printed out
    - https://docs.google.com/document/d/1bW9b2NI0djoE6E-tIGxNxXCssTkwl12l5mdgXjBWh_E

### Actual Lesson

- Introduction
    - Get everyone's name
    - Introduce self
        - AWS spiel
        - Show website stuff
- Explain goals of course
    - Independence, confidence, thinking of computers as a tool
- Syllabus
    - Talk through syllabus
        - Emphasize if need help, come find me
        - 9th graders need to show independence
    - Things understand
    - Things don't understand
- Course overview
    - Walk-through of class
    - Any questions?
- Reiterate goals of course
- Rules of the class (just as important as content)
    - Read through list:
        - Clean up space before you leave
        - Push in chairs before you leave
        - Raise hand before speaking
        - Don't touch anyone else
        - No unapproved video games
    - Any suggestions on what we should add/change?
    - Have everyone sign/big nod to agree
- Discipline ladder
    - Name on board
    - Name underlined on board
    - Letter grade drop in participation for week
    - Letter grade drop in participation for week
    - Email to parents
    - Trip to office
- Field trip to CS office
    - Practice pushing in chairs and cleaning up before leaving
- Explain homework
    - Sign up for appointment with me via Google Calendar
    - Prove that you can make appointment
    - Prove that you can find me
    - Note: Not an actual 15m meeting, a lot of students get confused by this
- If have time:
    - Recursion:
        - Who's heard of recursion?
        - Define it
        - Can help art
            - Show Sierpinski triangle and explain it
            - Show picture of a tree
            - Go to https://codepen.io/hippiefuturist/full/NRWOxM
                - Make sure branches recursive levels are initially set to 0
            - Show recursion program with turtles
                ```
                from turtle import *

                def do_something_2(cur_size, num_levels):
                    if num_levels <= 1:
                        for i in range(3):
                        forward(10)
                        right(120)
                    else:
                        pensize(num_levels)
                        forward(cur_size)
                        left(30)
                        do_something_2(cur_size / 2, num_levels - 1)
                        right(60)
                        do_something_2(cur_size / 2, num_levels - 1)
                        left(30)
                        back(cur_size)

                # speed(0)  # Uncomment this line to make the turtle go fast
                left(90)
                backward(50)
                do_something_2(100.0, 5)
                ```
- Distribute "getting to know you" sheet
    - `onboarding_questionnaire`

### Homework

```
FIRST: Make sure you're using your UCLS Google account. You **MUST** use your
UCLS Google account to make this appointment or you will not get credit for this
assignment.

SECOND: Go to the Schoology page for this course and navigate into the
"Administration" folder. Click on the "Appointment Calendar" link.

THIRD: Setup a **FAKE** appointment to see your instructor sometime on either
September 14th (Saturday), September 15th (Sunday), or September 21st (Saturday).
This is a fake appointment, so you should not actually come in for it but you
should **remember the time** of the appointment.

FOURTH: Drop by the Computer Science office and tell me the time of your
appointment so I can verify that you have your timezone setup correctly. If I am
NOT THERE, write you name and your appointment time on the whiteboard by my
desk.

This will **prove** that you know how to use my appointment calendar AND you
know where the Computer Science office is located, so there is no excuse for not
utilizing this resource in the future.
```

> Note: Make sure to replace existing dates w/ correct dates AND to set up calendar
