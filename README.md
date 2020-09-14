# Pharmb.io Web Source Repository

[![Build Status](https://travis-ci.org/pharmbio/pharmbio-web.svg?branch=master)](https://travis-ci.org/pharmbio/pharmbio-web)

The Static ([Hugo](https://gohugo.io)) website for [pharmb.io](https://pharmb.io).

## Local development
```bash
hugo server
``` 

## Automated publishing

When making changes please follow these steps:

 1. Clone this repo
 
    ```bash
    git clone git@github.com:pharmbio/pharmbio-web.git
    ```
    or if you already have a clone of this repo
    ```bash
    git checkout master
    git pull
    ```
 2. Create a new branch with your name and what you are changing `name/topic-of-change`
 
    ```bash
    git checkout -b kalle/update-my-profile
    ```
 3. Make your edits
 4. Push your edits to a new branch *in this repo* (Important! otherwise it will not work)
 
    ```bash
    git push -u origin kalle/update-my-profile
    ```
 5. Create a Pull Request (PR) on GitHub and select `base:master <- compare:kalle/update-my-profile`
 6. Check that the PR build status is passed (green)
    If not got to step 3 and repeate
 7. Ask for it to be merged (jonalv, olas)
 8. Done!

Note that you are supposed to work with this repository only. Don't fork the
repo, as the encryption stuff in the travis build will not work then.

## Notes

(Don't mix this repository with the public HTML version, which is located in
[github.com/pharmbio/pharmbio.github.io](https://github.com/pharmbio/pharmbio.github.io),
and which you are not supposed to edit directly).
