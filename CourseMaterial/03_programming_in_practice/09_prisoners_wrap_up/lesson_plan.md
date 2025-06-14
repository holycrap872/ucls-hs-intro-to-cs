## Essential Questions

- How can we use lists to store complex information?
- How can we use computers to solve complex problems?

## Lesson Plan

### Setup

- Copy people's bot code into tournament and be prepared to run it
- YouTube video loaded up
    - https://youtu.be/Y0Oa4Lp5fLE?si=mJ0rgbMmDAAmMwuL&t=3027
        - 50:27 - 53:15
- `Ethical Bots Worksheet` GoogleDoc printed out
    - https://docs.google.com/document/d/1Y1NmVivQTx39OA9RNYZytmFFvYmFDOKJHDhmTNzPyBE
    - Printed out because they need space to write/draw

### Actual Lesson

- Quick, two question quiz on Biology of Prisoner's Dilemma "reading"
    - "What are social species better at detecting" -> cheating, altruism
    - "What would tit-for-tat do if the person's history is ...."
- Review
    - Lists
    - Lists vs. strings
    - Purpose of lists
- Talk about bio lecture
    - Why is this question important in biology?
    - Why is tit-for-tat a good strategy
    - How drive to extinction?
- Tournament time
    - Talk through tournament code
    - Do big tournament of all bots
        - Winner gets candy
    - Talk through winner's code
    - Winning individually vs. winning globally
- Show YouTube video on tit-for-tat weakness
    - https://youtu.be/Y0Oa4Lp5fLE?si=mJ0rgbMmDAAmMwuL&t=3027
        - End at "vulnerable to signal error"
    - What does this say about code vs. humans?
    - How could we simulate this in our tournament?
- Break up into groups of 2-3
    - What would be code for each of the following:
        - "Eye for an eye"
        - "Turn the other cheek"
        - "Do unto others as you would have others do unto you"
    - Hand out `Ethical Bots Worksheet`
- Soap box
    - Humans evolved to see cheating by others
    - Sometimes signals get crossed
    - Eye for an eye is too "selfish"
    - Ethics requires us to break these cycles
- Rest of class
    - If done, can work on something else
    - If not, finish

### Homework

- TIL entry on code of "tit-for-tat"
    ```python
    def tit_for_tat(my_choices, other_choices):
        if len(my_choices) == 0:
            return "cooperate"
        elif other_choices[-1] == "defect":
            return "defect"
        else:
            return "cooperate"
    ```