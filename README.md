
# Logs Analysis Project 
part of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

### By Hector Rosario

## Project purpose
To write SQL queries to answer the following questions about a PostgreSQL
database containing the logs of a fictional newspaper website.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Required Libraries and Dependencies
The project code requires the following software:

* Python 3
* psycopg2 
* PostgreSQL 

You can run the project in a Vagrant managed virtual machine (VM) which includes
all the required dependencies (see below for how to run the VM). For this you
will need [Vagrant](https://www.vagrantup.com/downloads) and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) software installed on
your system.

## Project contents
This project consists of the following files:

* `analysis_reporting_tool.py` - The Python program that connects to the PostgreSQL
  database, executes the SQL queries and displays the results.
* `newsdata.zip` - SQL News data that you'll be connecting to.
* `Analysis  tool output.txt`- Plain text file that is a copy of what your program printed out.
* `README.md` - Read me file.

## How to Run the Project

Download the project zip file to your computer and unzip the file. Or clone this
repository to your desktop.

### Dowmload the data

You will need to unzip this file after downloading it. The file inside is called newsdata.sql.
Put this file into the vagrant directory, which is shared with your virtual machine.

### Download the data
You will need to unzip newsdata.zip file after downloading it. The file inside is called newsdata.sql.
Put this file into the vagrant directory, which is shared with your virtual machine.

To load the data, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:

* `psql` — the PostgreSQL command line program
* `-d news` — connect to the database named news which has been set up for you
* `-f newsdata.sql` — run the SQL statements in the file newsdata.sql

Running this command will connect to your installed database server and
execute the SQL commands in the downloaded file, creating tables and populating them with data. 

### Bringing the VM up

Open the text-based interface for your operating system (e.g. the terminal
window in Linux, the command prompt in Windows) and navigate to the project
directory.
Bring up the VM with the following command:

```bash
vagrant up
```

The first time you run this command, it will take awhile, as Vagrant needs to
download the VM image.

You can then log into the VM with the following command:

```bash
vagrant ssh
```

More detailed instructions for installing the Vagrant VM can be found
[here](https://www.udacity.com/wiki/ud197/install-vagrant).

### Make sure you're in the right place
Once inside the VM, navigate to the tournament directory with this command:

```bash
cd /vagrant
```

### Running the reporting tool
The logs reporting tool is executed with the following command:

```bash
python analysis_reporting_tool.py
```

The answers to the three questions should now be displayed.

