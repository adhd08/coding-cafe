1. What did pwd print?
   pwd printed the path of my current working directory. It shows the location of the folder I am currently working in.

2. What did ls -Force show that plain ls did not?
   ls -Force showed hidden files and folders that were not displayed by plain ls. It also displayed the normal file information such as Mode, Length, and LastWriteTime.

3. Pick one line from ls. What do you think the Mode column means?
   The Mode column shows the type and attributes of the item. For example, d----- means the item is a directory, while a mode beginning with - represents a file.

4. Why does that work from where you are standing? Which kind of path is coding-cafe\week02?
   coding-cafe\week02 works because my current working directory is the parent location containing the coding-cafe folder. It is a relative path because it does not begin with a drive letter and root such as C:\.

5. mv did two different jobs above. What were they?
   mv was first used to move README-backup.md from the coding-cafe folder into week01. It was then used to rename README-backup.md to old-readme.md inside week01.

6. How many folders are on your PATH?
   There are 18 entries in my PATH. They include folders such as C:\Windows\System32, C:\msys64\ucrt64\bin, C:\MinGW\bin, and the VS Code bin directory.

7. Exactly where does your python live?
   The Source column shows that my Python installation is located at:
           C:\msys64\ucrt64\bin\python.exe

8. Compare your answer to 7 with the person next to you. Are they the same?
   Our answers were different because Python can be installed in different locations on different computers. The operating system, installation method, and individual user's configuration can all affect where Python is located.

9. What exactly did the shell say? Explain using PATH.
   PowerShell said that pyton was not recognized as a command. This means PowerShell searched the locations listed in the PATH environment variable but could not find a program matching that command name; in this case, the main problem was the typo.

10. .venv did not appear with plain ls. Why not?
    .venv did not appear with plain ls because it is a hidden directory. PowerShell's plain ls does not show hidden items, while ls -Force does.

11. What changed about your prompt?
    The prompt changed by showing (.venv) at the beginning. This indicates that the Python virtual environment has been activated.

12. Compare this with what you wrote down for question 7.
    No, the path was different. Before activation, python pointed to my normal Python installation, while inside .venv it pointed to the Python executable inside .venv\Scripts; this shows that activating the virtual environment modified my PATH so that its Python is found first.

13. What is in the second list that was not in the first?
    The second list contains the requests package, which was not present in the first list. It was added by running pip install requests inside the virtual environment.

14. Where does python point now?
    After running deactivate, python pointed back to my original Python installation outside the virtual environment. This shows that deactivating the environment removed its location from the front of my PATH.

15. What does -Recurse do?
    The -Recurse flag makes PowerShell perform the command on the specified directory and all of its subdirectories and their contents. For example, ls -Recurse coding-cafe displays the files and folders inside coding-cafe, including those nested in week01 and week02.

16. What is the difference between Ctrl+C and Ctrl+Z?
    Ctrl+C interrupts the currently running program, while Ctrl+Z followed by Enter sends an end-of-input signal in the Python session. In the assignment, Ctrl+C interrupts Python and Ctrl+Z followed by Enter exits the input session.