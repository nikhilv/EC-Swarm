EC-Swarm
========

ElectricCommander/Perforce Swarm integration

1. Install the EC-Swarm.jar plugin on your ElectricCommander Server.
2. Setup a Project in Swarm.
3. Use the following URL format in the Automated Tests Field

> https://[Commander Server IP]/commander/plugins/EC-Swarm-1.0/cgi-bin/swarm.cgi?change={change}&status={status}&review={review}&project={project}&branch={branch}&pass={pass}&fail={fail}&projectName=Default&procedureName=Swarm&user=[User name to electriccommander]&password=[password]

Fill in the fields marked with < >
projectName - Project name that contains the procedure to run upon shelving of code.
procedureName - Procedure name to execute upon shelving of code.
user - User name to login to ElectricCommander
password - password for user name
The fields marked within { } are populated at run time by Swarm. Leave them as they appear.
4. Shelve a file in p4v or on the command line with '[review]'
5. Login to Commander and see job that was launched
6. Unshelve files and checkout from p4, build, test, deploy, profit!

More information about the Swarm and Commander:

Perforce Swarm
http://www.perforce.com/product/components/swarm

ElectricCommander
http://www.electric-cloud.com/products/electriccommander.php