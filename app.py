print('Hi Git')

# steps --------
#> git init (only once per project for a new project)
##> git status (optional, just to see status of tracked/untracked and left to be committed)
#> git add .('dot') - (for all files) -OR- git add my_filename.py (for just a single file)
##> git status (optional, just to see status of tracked/untracked and left to be committed)
#> git commit -m "Name my commit here" (make sure to to leave a message with -m!!!!)
##> git status (optional, just to see status of tracked/untracked and left to be committed)

#--- when you make changes to commit
#> git add . (for mwhen you make changes)
#> git commit -m "Changes I made to the file"

#--- when you want to push (for the first time in a new repo)
#> git remote add origin https://github.com/mikegoescoding/my-repo-name.git
#> git push -u origin master

# LETS SEE WHAT HAPPENS AFTER YOU PUSH, AND COMMIT AGAIN ???? HMMMM.....

#--- when you want to push after the initial push, *** you only need to use:
#> git push


#----git pull test?
#> git pull

# the git pull test worked!! lets push it back !

#---------- reverting to latest git commit - all files
#> git diff filename.py  <--- shows differences between latest commit and current changes
#> git checkout .(dot)  <---- removes the changes
#> git status <--- to show/confirm they were removed

#---------- revert to latest git commit - single file
#> git log <-- to get log of commits
#> copy the commit code you want to revert to
#> git checkout commitcodehere -- filename.py
