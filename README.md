# Simple script to get Stealthwatch alarm definition

I was not able to find any Stealthwatch API for Alarm's definitions. But there is a [guide](https://www.cisco.com/c/dam/en/us/td/docs/security/stealthwatch/management_console/securit_events_alarm_categories/SW_7_2_Security_Events_and_Alarm_Categories_DV_1_0.pdf): "Security Events and Alarm Categories {ver}".

I decided to create a kind of API and parsed PDF into the JSON file with information about Alarms. Simple and easy to use.

<!-- TABLE OF CONTENTS -->
## Table of Contents
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Contact](#contact)

## Built With
* Python3

<!-- GETTING STARTED -->
## Getting Started

### Clone the repository
```sh
git clone https://github.com/dagolovach/stealthwatch-alarms.git 
```

### Create a virtual enviroment
```sh
% python3 -m venv vevn
% . venv/bin/activate
```

### Install modules from requirements.txt
```sh
% pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage
* Getting the list of all Alarms

```sh
% python3 define_alarm.py --list
```
<img width="300" alt="Screen Shot 2020-05-17 at 10 17 06 PM" src="https://user-images.githubusercontent.com/39305133/82171165-27468d80-988c-11ea-8fa4-8a5401ea7551.png">

* Getting the list of all alarms with TCP in the name
```sh
% python3 define_alarm.py tcp 
```
<img width="600" alt="Screen Shot 2020-05-17 at 10 18 32 PM" src="https://user-images.githubusercontent.com/39305133/82171244-59f08600-988c-11ea-93e5-173b1c7d858a.png">

* Getting info for specific Alarm
```sh
% python3 define_alarm.py udp-flood
% python3 define_alarm.py "udp flood"
```
<img width="600" alt="Screen Shot 2020-05-17 at 10 19 08 PM" src="https://user-images.githubusercontent.com/39305133/82171271-7096dd00-988c-11ea-8f79-84c0364e8f79.png">

<!-- CONTACT -->
## Contact
* Created by Dmitry Golovach
* Web: [https://dagolovachgolovach.com](https://dmitrygolovach.com) 
* Twitter: [@dagolovach](https://twitter.com/dagolovach)
* LinkedIn: [@dmitrygolovach](https://www.linkedin.com/in/dmitrygolovach/)

- feel free to contact me!


