# Geoloc

**CLI Project Name**: geoloc

## Description

Based on the user input, city and state or zip, make an api all to get latitude, longitude, country, city, state...etc.
Input can be a list of strings like below:
```
Possible examples:
● geoloc-util --locations “Madison, WI” “12345”
● geoloc-util “Madison, WI” “12345” “Chicago, IL” “10001
```

```
geoloc-util "01801" "Lincoln, IN" "000" "Kovai, IN" "11111" "13214654" "adf, ad" "a,a", "", "  ", " , "
```
For the above input, the cli response is given below. 
```
Zip: 01801
Country: US
State: Woburn
Latitude: 42.4829
Longitude: -71.1574
----------------------------------------
City: Lincoln
Country: US
State: Indiana
Latitude: 40.6155947
Longitude: -86.2099948
----------------------------------------
000:Incorrect Zip code
----------------------------------------
Kovai, IN:Non existent data given, please check if the State and City are correct Kovai and IN
----------------------------------------
11111:Non existent data given, please check if the zip code is correct 11111
----------------------------------------
13214654:Incorrect Zip code
```

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Running Tests](#running-tests)
5. [Features](#features)
6. [Contribution](#contribution)
7. [License](#license)

## Prerequisites

- **Python Version**: This project requires Python 3.11 or higher. 
- **Package Manager**: Ensure you have `pip` installed, which comes with Python.

### Installing Python


1. **For macOS**:
   - You can install Python using Homebrew. Open a terminal and run:
     ```bash
     brew install python
     ```
  https://docs.brew.sh/Homebrew-and-Python
Visit the above link to get exact steps on installing python 3.11
## Installation

1. **Create a Virtual Environment**:
   It is recommended to create a virtual environment to manage dependencies. Run the following commands:

   ```bash
   # Navigate to your project directory
   cd /path/to/your/project

   # Create a virtual environment
   python3 -m venv venv

   # On macOS/Linux
   source venv/bin/activate
   
   https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html

2. **Install Poetry**:
   Once pip is installed, then run pip install poetry to from within the virtual environment
   From pycharm terminal, run the command 'poetry --version' to see the Poetry version
   It's important the poetry is installed as it would take care of all the necessary dependencies for this project
3. **Poetry build**:
   Now run the command 'pip list' to see if any dependencies are installed by default
   Next run the command 'poetry build' and this would take a few minutes for the very first time to install all the dependencies listed in the pyproject.toml file
   Once again run 'pip list' command to see if bunch of additional libraries are installed like:
     - pydantic
     - pytest
     - requests
     - typing_extensions
  
   These are just a few to list, depending on what other libraries are installed by default you might see additional 8-10 more
       

## Usage
  pip install geoloc-util
  this should install the geoloc-util to the machine and run the below command to see the output in the console.
```
  geoloc-util --locations "Boston, MA"
```
## Running tests:
  This repository is built with pytest and the packages are managed with poetry. Once the necessary dependencies are installed you can run the tests either by selecting each tests in the test class or run them as a suite by below command.

  ```
   (venv) <machine-name>:geoloc swami.padmanabhan$

```
Make sure to navigate to the geoloc folder in your local machine
```
   pytest -v -s tests/test_geo_loc.py
  ```

  after running this command, the logs will be created in the Projects/geoloc/logs [check in the main root foler]

  If running the tests, individually from the test class, then the logs will be created within the tests folder

## Features
  - Reusability: Build with multiple design principles in mind, like reusability to having methods that makes api calls for various endpoints.
  - Logs: source logs separate from test logs, however logger functionality is maintained at a common place
  - Readability: Logs are easily readable and the methods and classes follow the same
  - Pydantic: To validate the json response for field input and type is implemented for both city and zip code response
  Mock Integration: Verifying the integration of the cli by creating mock response and checking for validity

## Contribution
  Fully written and developed by Swami Padmanabhan

## License
  MIT license is used
