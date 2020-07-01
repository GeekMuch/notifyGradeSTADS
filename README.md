# Grade notifier 
Notifies by playing a YouTube video when a new grade is added.

## Description
When a new graded is added to the list while the script is running, a YouTube video will play. The notifier refreshes every 420 seconds(7 min) until a new grade is up.  It uses selenium to get the information, which also is a requirement. The YouTube link can be changed as well as the two links for the STADS login page and the STADS result page(according to your university). Enjoy the spaghetti! 

## Requirements
The notifier is written in Python 3.

- [Any version of Python3](https://www.python.org/downloads/)
- Required dependencies can be found [here](https://github.com/GeekMuch/notifyGradeSTADS/blob/master/requirements.txt)
    -```pip install -r /path/to/requirements.txt```
