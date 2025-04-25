## Essential Questions:

- How can we use arrays to make decisions over time
- How can computers be used to solve problems in other disciplines

## Lesson Plan

### Setup

- Homework posted in Schoology:
    - Watch: https://youtu.be/Y0Oa4Lp5fLE?si=cP7lJUbUYiwVXoNh&t=2090
        - 34:50 - 48:43
- `./prisoners_warm_up.py` loaded up for demo purposes

### Actual Lesson

- Opening problem
    - ```python
      def do_something(words):
          ret = []
          for word in words:
              if len(word) == 4:
                  ret.append(word)
          return len(ret)

      if __name__ == "__main__":
          l = ["This", "is", "string", "list"]
          result = do_something(l)
          print(result)
      ```
    - Iteration chart
- Review
    - Lists vs. Strings
    - `.append()`
- Explain homework
    - Stanford bio class about prisoner's dilemma in evolution
    - Listen and be prepared for two question reading quiz
- Pivot to review of prisoner's dilemma worksheet
    - What do we remember?
    - How are lists being used?
- Walk through `./prisoners_warm_up.py` (from Problem 3 of worksheet)
    - What is it doing?
    - How could we add another round?
    - How could we change the behavior and what would happen?
        - Jerk bot
        - Con-man bot (array length)
    - Step through using debugger
- Continue worksheet
    - Explain that it is an encoding of this game
    - Slowly work up to building your own bot in Python
    - Will play all the big bots against each other in an "arena"
- Go!

### Homework

- Finish `Python Lists Two Worksheet` (if long block)
- Watch video and prepare for "reading quiz"
