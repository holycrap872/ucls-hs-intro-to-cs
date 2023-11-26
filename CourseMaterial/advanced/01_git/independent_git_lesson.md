# Git Lesson

Git is another fundamental tool in a programmer's tool belt. It allows users to
easily save their work and look back (revert) if they every make a mistake. It
also allows users to easily experiment (branch) with new code so it doesn't
interfere or break existing code. Finally, it provides a means by which
programmers can collaborate, allowing projects to move quickly and integrate the
skills of all.

This lesson involves several rounds of research, reflection, and application.

## Research Part 1:

Take the Microsoft Learn "intro to git" course. The course is available at
https://learn.microsoft.com/en-us/training/modules/intro-to-git/ . You will need
to create a microsoft account to access the tutorial (should be free), but you
_should not_ need to use their Azure sandbox. Instead, you can do all of the
commands on your own personal laptop. Whenever you see the phrase "Cloud Shell",
simply use your local version of shell.

> Make sure to watch the `Introduction to Git Recap` video.

## Reflection Part 1:

1. If you run the command `mkdir example && cd example && git init`, what have you done?
   ```


   ```
2. The most common git commands are `status`, `add`, and `commit` - usually in that order. Why?
   ```



   ```
3. Git is often described as "a chain of diffs". Why?
   ```



   ```
4. What is the difference a tracked file and an untracked file in git?
   ```



   ```

## Research Part 1:

Now, it's time to put your skills into action in a more complex way. Complete
https://learn.microsoft.com/en-us/training/modules/create-git-project/ 

## Reflection Part 2:

1. There's a lot of information about individual commits when you run `git log`.
   In the space below, create an example `git log` entry, and explain what each
   line means.
   ```


   ```
2. What does the `.gitignore` file do?
   ```
   


   ```
3. What does the `.git` folder do?
   ```
   


   ```
4. What command is equivalent to `cp FILE1 FILE2 && git rm FILE1 && git add FILE2`?
   ```
   


   ```
5. What is the difference between `rm FILE` and `git rm FILE`?
   ```
   
   

   ```

## Application:

### TIL Repository

To demonstrate your understanding of git, you are now going to move your TIL
entries from the GoogleDoc to a git repository. To do this, you will create a
repository on UCLS's GitLab server and then push your content up.

To accomplish this, do the following steps:

1. Log into `https://gitlab.ucls.uchicago.edu` using your Google credentials
2. Create a `New project` (aka repository) called "Today I Learned"
   - The project should be **blank**
   - Make the project "slug" be `til`
   - Make sure the project is `Private`
3. Use `git clone` to pull down the newly created repository
   - Read the `README.md` file carefully, it has a lot of useful information
4. Create one file per entry that you've already created and copy in the content
   - Make sure to name the files something that is easy to understand
   - The resulting folder structure should be something like:
   ```
   - TIL Repository
      - README.md
      - shell
         - SHELL_ENTRY_FROM_TIL_GOOGLE_DOC_1.md (you can choose your own file name)
         - SHELL_ENTRY_FROM_TIL_GOOGLE_DOC_2.md (you can choose your own file name)
         - ...
      - git
         - GIT_ENTRY_FROM_TIL_GOOGLE_DOC_1.md (you can choose your own file name)
         - GIT_ENTRY_FROM_TIL_GOOGLE_DOC_2.md (you can choose your own file name)
         - ...
   ```
5. Commit your changes and push your commit up to the repository
6. Give me (erizzi) access to your respository

### Git Back



1. 
2. Clone "advanced repository"
3. Make a change to this exact worksheet with a new or improved question
4. Push your changes

### Advanced

Finish https://learngitbranching.js.org/
