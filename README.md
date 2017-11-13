# Udacity FullStack Developer Nanodegree Program
#### SQL database project

###### Requirements
You need to install python and the virtual machine that to run the sql databse server. The VM is a Linux server that runs on top of you computer.
* Download the latest version of [Python 3](https://www.python.org/downloads/)
* Download [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org) to install and manage the Virtual Machine.
* Download the information into your vagrant folder [VM configuration](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


###### Install the virtual Machine
* Install [VirtualBox](https://www.virtualbox.org) make sure you are downloading the latest version, there could be some incompatibility issues.
* Install [Vagrant](https://www.vagrantup.com/downloads.html) verify by running that it has installed by using:
```
$ vagrant --version
```
* Navigate where you vagrant folder is and the run the following command to intsall Linux in you VM:
```
$ vagrant up
```
* Log into you Linux VM by using:
```
$ vagrant ssh
```

###### Running the project
* Verify access to database using the following command: 
```
$ psql -d news -f newsdata.sql
```
* Access the Virtual machine navigate to the vagrant folder inside it and then run the following command to output the database queries for the project.
```
$ python3 news.py
```

