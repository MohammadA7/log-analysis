# Log Analysis
>This project is a reporting tool that prints out reports (in plain text) based on the http server's logs.

## Get started:
* Install Vagrant
* Install VirtualBox
* Download the vagrant configuration for the VM from[udacity](https://github.com/udacity/fullstack-nanodegree-vm)
* cd to vagrant directory
* clone the project `git clone https://github.com/MohammadA7/log-analysis.git`
* Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Extract the newsdata.sql file and put the newsdata.sql file into log-analysis directory

### Run the VM
* cd to vagrant folder on the host machine (your machine)
* Run `vagrant up` to run the VM
* To ssh to the machine run `vargrant ssh`
*once you are logged in cd to `/vagrant/log-analysis`

### Load the database
* run this command to load the data into the database on the virtual machine `psql -d news -f newsdata.sql`

### Lastly run the project 
* run the project by executing this command `python3 LogAnalysis.py`
* output will be printed