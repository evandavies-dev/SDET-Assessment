# SDET-Assessment
API Test - Automation Exercise

## Overview

Description: This repository contains an automated python-based test collection that validates API routes/resources exposed by https://jsonplaceholder.typicode.com.
I have used parameterized tests to more efficiently validate all existing routes and how they react to different requests (GET, POST, PUT, PATCH, and DELETE). To help organize the data for these tests I have included a file called resources.py that lists details for each route such as element counts and field compositions, as well as testing data such as route-specific payloads, potential filterable keys, new id values for the POST tests, and expected comment counts.

Assumptions: 
I am assuming that because the website does not persist data pushed or deleted, that I cannot check if anything has actually been deleted from the server outside of trusting the successful 200-code that is returned after a successful DELETE request.

Scope of testing:
I have done my best to cover all basic requests (GET, POST, PUT, PATCH, and DELETE) for each available route/resources as well as a few potential edge cases (invalid routes)

## Execution Instructions

I used the windows program Git Bash (https://gitforwindows.org/) because I am primarilly used to using a bash environment, but I have provided instructions for both Git Bash, as well as Powershell if that is more convenient.
The test results will automatically be shown at the end of the test run.

### Git Bash Execution Instructions
1. Change directory to the project (cd SDET-Assessment)

2. Run the following command:
python3 -m venv .venv

3. The client should show you are now in a virtual environment though the output ((.venv) ). Run the following command:
source .venv/Scripts/activate

4. Run the following command:
pip install -r requirements.txt

5. Run the test collection with the following command:
pytest

### Powershell Execution Instructions
1. Change directory to the project folder with the following command:
    cd SDET-Assessment

2. Create a virtual environment with the following command: 
python -m venv .venv

3. Activate the virtual environment with the following command:
.\.venv\Scripts\Activate.ps1

4. Install dependencies with the following command:
python -m pip install -r requirements.txt

5. Run the test collection with the following command:
python -m pytest

## Coverage Summary:
I have included tests that cover the following areas:
- Positive/Successful results for all GET, POST, PUT, PATCH, and DELETE requests, for all available routes (posts, comments, albums, photos, todos and users)
- Validating the field structures/order of returned values from all requests
- Testing invalid routes (routes outside of the 6 listed on the website)
- Testing filtered route paths (routes that contain a filterable key value)
- Testing nested route paths (/albums/1/posts, /users/1/albums, etc)

In these tests I have validation checking for correct json field structures, status codes and returned field values matching expected results.

## Other notes:
I combined all the tests to one file due to time constraints, but if given more time I would have organized tests based on function (requests, nested routes, filtered routes, etc).