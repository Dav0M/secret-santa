# secret_santa

A python script that handles secret santa assignments based on people and optional exclusions. Built with Python and the standard library.

## Install and Setup
Uses the standard library, so there are no dependencies.

Populate the santaData.json file with particpants and their respective information using the template for the script. Names in the exclusion list must match another participants name. 
```
{
    "Person" : {
        "name" : "Person",
        "email" : "email@email.com",
        "exclude" : ["Person 2"]
    },
    ...
}
```

Then, fill in your email and password within the `santaMail.py` file.
- Your email can be filled in as is
- For your password, follow steps outlined in the solution [here](https://stackoverflow.com/questions/72577189/gmail-smtp-server-stopped-working-as-it-no-longer-support-less-secure-apps) to get a usable password. 
    - Google stopped supporting "Less Secure Apps" and replaced it with a different option, so your usual password will no longer work.

To run the script and send the emails:

`python secretSanta.py`

## Reflection
The motivation for this project was to create a solution for secret santa assignments without the use of third-party applications or websites. My friends and I have been doing a secret santa for a few years now and it gets tiresome giving up personal information and emails to a third-party when I can just handle it myself.

Originally, the program used a `.csv` file for data and the [yagmail](https://pypi.org/project/yagmail/) library for email functionality, but they were both more trouble than they were worth compared to `.json` and the standard library. 

The final logic, however, stayed mostly the same between the iterations. At first, I decided to determine who to assign a giftee to by random choice or in order, but that quickly breaks when considering exclusions sets for each participant. The solution I came to was choosing the next santa based on the least amount of potential giftees. There are some conditions and states where this also fails, but as long as the exclusions list isn't extreme it should run fine.

## Plans
I do intend to give this some kind of interface and make it interactive before the next secret santa cycle. Until then, it's functionality through the terminal will suffice.