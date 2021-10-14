# Youtube Search from command-line
This is a command line interface for openig a query on YOUTUBE

## Usage

Run like 

```
ytseach.py [-h] [-n NUMBER] query
```
- Put your query under ```query``` argument
- ```-n``` flag for opening the nth video
- ```-h``` for displaying a help

## Requirements

Make sure that you have 
1. Selenium installed 
    - If not install by running ```pip install selenium```
2. [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) installed
3. [Geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.30.0) installed
4. Add the path of Geckodriver in the this code 