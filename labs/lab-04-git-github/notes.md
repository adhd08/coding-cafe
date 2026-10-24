Ans 1: The `--global` flag configures Git settings for your entire user account across all repositories on your computer, saving them in your global configuration file. If you leave it out, Git applies the configuration only to the specific local repository you are currently working in, storing it in that folder's configuration file instead.



Ans 2: When you run `ls -a` (or `ls -Force` on Windows), the hidden `.git` directory appears, which does not show up with a standard `ls`. Inside this `.git` directory are Git's internal tracking files and folders—such as `HEAD`, `config`, `description`, hooks, and the `objects` and `refs` directories—which store your repository's history, commits, and configuration metadata.



Ans 3: 5 files. Yes it does



Ans 4: After creating the `.gitignore` file, all the files and folders inside the `.venv/` virtual environment, along with any pre-compiled `\_\_pycache\_\_/` or `.pyc` files, disappeared from the untracked files list in `git status`. Git now successfully ignores them based on the rules specified in your `.gitignore` file.



Ans 5: Yes, the .gitignore file itself should be committed to your repository rather than ignored.



It needs to be tracked so that anyone else who clones or downloads your project will also ignore the same generated files, virtual environments, and system caches on their own machines.



Ans 6: `README.md` moved from "Untracked files" to "Changes to be committed" (staged) in the `git status` output. In the three-places model, it moved from the working directory into the staging area (index).



Ans 7: Git prints a summary showing the branch name you committed to (e.g., `main`), the short commit hash, and your commit message. It also displays a status line stating how many files changed and how many insertions or deletions were made (for example, \*1 file changed, 3 insertions(+)\*).



Ans 8:The first seven characters of your commit are called the short commit hash (or abbreviated commit hash). They serve as a unique, shorthand identifier for that specific commit, allowing you to easily reference, inspect, log, or revert to that exact point in your project's history without having to type out the full 40-character SHA-1 hash.



Ans 9:

