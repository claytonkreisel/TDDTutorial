# Test-Driven Development Tutorial

In this project we explore how to write apps using test driven-development. This project includes a few different packages that would all be their own root projects in actually app development. This is a monolith using one package management instance (`poetry`) to manage the packages for several different modules, each of which are a tutorial to help train and exercise in TDD principles.

In the following tutorials you will develop a solution using `python` and will write appropriate tests in order to automatically test your code. This is called `unit` testing. We will also talk about `e2e` or `functional` testing as well.

## Getting Started

In order to be able to develop locally on this project you must have a few things installed. The first thing you need to have installed is `python v3.10.9`. That is the version that this codebase is written on.

### Install `pyenv` and `python v3.10.4`

The best way to manage your python versions is to have a python virtual environment installed called `pyenv`. In order to install `pyenv` you can visit [this link](https://github.com/pyenv/pyenv#installation).

If you are using a mac then you can install this using `brew` assuming `brew` is installed on your machine. You can run the following commands in order to install `pyenv`

```bash
brew update
brew install pyenv
```

Once this is done you can then run the following commands to get the right version of python installed and then to use that version for the project.

```bash
pyenv install 3.10.4
pyenv local 3.10.4
```

This should set your local version to `3.10.4`. You can confirm this by running `pyenv local` this should return the version of `3.10.4` if installed correctly.

### Install `poetry` package manager

In lue of `pip` we are going to use a different package manager on this project called `poetry`. `poetry` is much like `yarn` is to `npm` if you are familiar with `js` development. It is simply a different (and in my opinion better) package manager for `python` based projects.

In order to install poetry you can use [this link](https://python-poetry.org/docs/).

However, this command should get you going.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

If you are on a macOS you may have to `poetry` to your `bash` or `zsh` profile and then restart your terminal in order to use the `poetry` command.