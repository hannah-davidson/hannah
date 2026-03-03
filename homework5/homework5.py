# Homework 1 + 2 Review
# 3.1 Vocabulary Review
# 1. Git is a version control system that you can use locally, while GitHub is a web-based platform where you can host your repository online and have a remote version control system.
# 2. The terminal is the application that acts as a text-based interface to the computer's operating system. The command line is a specific line of text within the terminal interface where you enter commands.
# 3. A local repository is one that is only on your computer, while a remote repository is one that exists on the internet.
# 4. Version control is a system that allows you to track the history of files over time.
# 5. In Git, the staging area is the intermediate step between the working directory and the local repository.
# 6. git add: moves changes from working directory into staging area
# 7. git commit: saves the project's currently staged changes to the local repository
# 8. git push: uploads local repository commits to a remote repository.
# 9. git status: displays the current state of working directory and staging area
# 10. git pull: downloads content from a remote repository to integrate the changes into local branch
# 11. pwd: prints working directory
# 12. ls: lists contents of directory
# 13. cd: changes directory you are working in
# 14. nano: command for creating or editing configuration and text files directly in the terminal
# 15. touch: creates a new file using the command line
# 16. mv: moves file from one directory to another
# 17. rm: removes a file from the directory
# 18. cat: short for concatenate, it prints all of the conents of a file.

# 3.2 Directory Tree
# 1. pwd
# 2. ls
# 3. cd python_decal/brianna_repo
# 4. mv homework.py ~/python_decal/judy_decal/homework
# 5. cd ~/python_decal/judy_decal/homework
# 6. cat homework.py
# 7. git add, git commit, git push
# 8. The error means that the local repository's history has diverged from the remote's. To fix this, use git pull to "pull" from the remote repository, then git push to psuh these changes to your copy locally.
# 9. ~/Recents

# Homework 3 Review
# 4.1 Data Types
def checkDataType(input):
    return type(input)
print(checkDataType(3.15))
print(checkDataType(True))

def evenOrOdd(int):
    if int % 2 != 0:
        return "Odd"
    else:
        return "Even"
print(evenOrOdd(4))

numbers = [1,2,3,4,5]
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sumWithLoop(numbers))

# Homework 4 Review
def duplicateList(list):
    return [item for item in list for item in [item] * 2]
lst = ['a','b','c']
print(duplicateList(lst))

# No colon after the def line.

print(evenOrOdd(512))