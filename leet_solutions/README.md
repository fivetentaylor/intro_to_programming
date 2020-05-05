# Leet Solutions!!!

Jeff and Taylor on a journey of self discovery

## Git Tutorial

```
git status
```

```
git commit
```

```
git branch
```

```
git checkout master
```

First go get the code

```
git clone git@github.com:fivetentaylor/intro_to_programming.git
cd intro_to_programming
```

```
# Assuming you just freshly cloned the repo and navigated into the folder
git checkout -b my_cool_new_branch # create a branch
git add . # add new files if there are any
git commit -a -m "something changed" # commit my changes
git push origin my_cool_new_branch
```

Then go to github and create a pull request

But wait, what if Taylor made conflicting changes with a file in Jeff's branch...

```
git pull --rebase origin master
```

Follow instructions to fix conflicts during rebase
