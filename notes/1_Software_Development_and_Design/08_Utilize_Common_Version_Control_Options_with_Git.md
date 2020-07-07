# Utilize Common Version Control Options with Git

## Clone

```
git clone https_or_ssh_path_to_repo
```

## Add/remove

Stage file for commit

```
# git add file.txt
```

Remove file from tracking

```
# git rm file.txt
```

## Commit


```
# git commit -m 'useful commit message' file.txt
```

## Push/pull

Push committed changes to remote repository

```
# git push
```

Pull changes from remote repository

```
# git pull
```


## Branch

Make parallel timelines that don't interfere with one another

```
# git branch newbranchname
```

Switch to another branch

```
# git checkout newbranchname
```

Switch back to master

```
# git checkout master
```

Combine creating a new branch and checking it out into one command

```
# git checkout -b newbranchname
```

## Merge and handling conflicts

Take modifications from one branch and combine them with existing code in another branch

Take code from branch_awesome and merge into master:

```
# git checkout master
# git merge branch_awesome
```

This may cause conflicts if changes were made to the same file in both branches.

Markers will be added to the file with conflicts to show options for resolving them.

## Undo

Update the previous commit (ONLY DO THIS IF CHANGE HASN'T BEEN PUSHED)

```
# git commit --ammend
```

Remove commits, resetting the HEAD (i.e. move the HEAD back in time)

Move the HEAD back 3 commits

```
# git reset HEAD~3
```

Move the HEAD to a specified hash

```
# git reset c482aef4
```

Create a new commit that reverses a commit while preserving all history

Roll back the last commit into a new commit on the timeline

```
# git revert HEAD
```


## Diff

Show all changes on all files since the last commit

```
# git diff
```

Show all changes on a single file since the last commit

```
# git diff file.txt
```

## Git checkout and detached HEAD

Revert to a previous commit by associated hash

```
# git checkout cf8201d
```

Now in a detached head state! No longer on the same branch. If you switch back to the previous branch, all changes have been effectively lost.
