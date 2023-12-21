## Prerequisites

* Python Version 3.11
* pip

## Setup

In a terminal from the Banjo_Kazooie_Randomizer root folder, run the following:

python3 -m pip install -r requirements.txt

python setup.py install

## Run

\path\to\python3.exe \path\to\randomizer\Banjo_Kazooie_Randomizer.py

example: C:\Users\USERNAME\AppData\Local\Programs\Python\Python311\python.exe .\randomizer\Banjo_Kazooie_Randomizer.py

## Repository Notes

Branches:
* main
  - Functioning code; Ready for potential release
  - Pull request must be approved by a Code Owner
* develop
  - Collaborative testing environment
  - Pull request must be approved by a Code Owner
* function/*
  - Branches for adding a base functionality of the randomizer
    - Ex: Being able to swap Banjo-Kazooie's model
  - Merge into develop; Delete this branch once its code has been merged into main
* feature/*
  - Branches for adding a feature to an existing function the randomizer
    - Ex: Adding a preset model to swap with Banjo-Kazooie's model
  - Merge into develop; Delete this branch once its code has been merged into main
* bug_fix/*
  - Branches for fixing bugs in the randomizer
    - Ex: Fixing an issue with a specific Banjo-Kazooie swap model preset
  - Merge into develop; Delete this branch once its code has been merged into main

Docs:
* Logic explanations
* Reasonings for doing/not doing things a certain way
* Explanation of overall file integrations
* Not meant for individual file explanations (should be in file PyDocs at top of file)

Randomizer:
* Files and folders for modifying the Banjo-Kazooie ROM
* Python files should have PyDoc strings for an overview of the file, including:
  - Purpose
  - Workflow
  - Dependencies
  - ToDo's

Tests:
* Tests directory reflects the Randomizer directory, as long as the path contains a script file
* Tests directory contains a folder called "test_files" for dummy files the tests can edit and check against
* Test files start with "test_" followed by the name of the file being tested
* Tests should cover success cases, failure cases, and branch options as best as possible

XDelta:
* Contains command line and user interface versions of the XDelta program
* Used for people who want a verified copy of their ROM (typically for racing purposes)

GitIgnore:
* Typical Python GitIgnore. Additionally includes:
  - The "do_not_commit" directory (for any files a developer wishes to not commit)
  - All directories/files created during setup.py
  - The "extracted_files" directory