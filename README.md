# A python script that allows user to use Google(or search query of your choice) with out leaving the Terminal

This Project is one of the many examples of how python can be used to automate repetitive things.

## Description
In this particular project **s** is used as a command to search things

For example ~ s "search phrase" will search on google with emphasis on 4 sites stackoverflow,medium,stackexchange


## How to use this project locally

1. Clone this project in your desired folder
2. Change directory to "Terminal_Search"
3. Open browser.py
4. Add any website you want in "valid_websites" list
5. Change the "browser_path" to your browser destination
    5.1 Windows
        5.1.2 browser_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe $s'
    5.2 Linux
        5.2.1 browser_path = '/usr/bin/google-chrome $s'
    5.3 MacOS
        5.3.1 browser_path = 'open -a /Applications/Google\Chrome/app $s'

### How to change the alias from "s" to whatever you want (For linux users only)

1. Open your Terminal
2. If Your using Bash
    2.1 Type "vim ~/.bashrc"
    2.2 copy paste "alias <your desired command> = <the file location to browser.py>"
3. If Your using Fish
    3.1 Type "alias <your desired command> = <the file location to browser.py>"
    3.2 Then Type "funcsave <alias name>"
    