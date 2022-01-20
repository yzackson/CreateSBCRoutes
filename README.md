# Create SBC Routes Bot

This bot was made to automate the creation of an huge amount of naps and routes in Khomp SBC to spare working time. 
<br>
<br>
## Enviroment requirements (where code will run):
---
* [Python v3.x](https://www.python.org/downloads/)
* [Pandas](https://pandas.pydata.org/) and [Selenium](https://pypi.org/project/selenium/) libraries.
* Google Chrome version 97 (no other chrome version will work until change the webdriver)
* Stable connection to the Khomp SBC
<br>
<br>
## How to run
---
1. Open the terminal or a program that runs python code
2. Navigate tyo the folder where the files are

    ![Navigate to folder](https://i.pinimg.com/originals/2a/32/ef/2a32ef1b9df94a6ee72594bd9cf14545.jpg)
3. Type ``python3 dott.py``
4. Insert the login, password, SBC IP and path of the branchs file then press enter.

    ![Insert data](https://i.pinimg.com/originals/b6/73/57/b67357d12d6b5b6693f13e89aa0f8966.jpg)
    
    _Its recommended to store the branchs list in the same directory of the bot, because the full path may contain caracters that can unable this bot to locate._
5. Just wait the bot done his job
<br>
<br>

## The branchs list format
---
This bot is waiting a .xlsx file with data disposed as shown below:
Nome | Dominio | Ramais
-----|---------|--------
branch 1 | IP branch 1 | sets branch 1 (regular expression)
branch 2 | IP branch 2 | sets branch 2 (regular expression)
branch 3 | IP branch 3 | sets branch 3 (regular expression)
branch 4 | IP branch 4 | sets branch 4 (regular expression)
...| ... | ...

_**Obs.: the headers has to be in portuguese**_

The sets range must be written using regular expression, because thats the method used to especify the route rule.

Regular expression example for the sets range:
Range | Regex 
-----|---------
322100 - 322199 | ^3221([0-9])([0-9])$
322100 - 322299 | ^(3221\|3222)([0-9])([0-9])$
322100 - 322149 | ^3221([0-4])([0-9])$
322150 - 322199 | ^3221([5-9])([0-9])$

## Logging
---
While the bot runs he outputs what is executing in the "logging.log" file at execution time. When the bot finish, you can see which routs and Naps were created, the name, IP and set ranges of it.