#!/bin/sh

exec "$COMMANDER_HOME/bin/ec-perl" -x "$0" "${@}"

#!perl

use LWP::UserAgent;
use XML::XPath;
use ElectricCommander;
use CGI;

my $query = new CGI;

# Get the GET parameters
my $change = $query->param("change") || "";
my $status = $query->param("status") || "";
my $review = $query->param("review") || "";
my $project = $query->param("project") || "";
my $branch = $query->param("branch") || "";
my $pass = $query->param("pass") || "";
my $fail = $query->param("fail") || "";

# The ElectricCommander project that houses the procedure to run
my $projectName = $query->param("projectName") || "";

# The ElectricCommander procedure to run
my $procedureName = $query->param("procedureName") || "";

# User name and password to login to ElectricCommander Server
my $user = $query->param("user") || "";
my $password = $query->param("password") || "";

# Create ElectricCommander object
my $ec = new ElectricCommander();

# Login to the ElectricCommander server
$ec->login($user,$password);
						 
$ec->runProcedure($projectName, {procedureName => $procedureName, 
     actualParameter => [  
      {actualParameterName => "change", value => $change},
      {actualParameterName => "status", value => $status},
      {actualParameterName => "review", value => $review},
      {actualParameterName => "project", 
                     value => $project},
	 {actualParameterName => "pass", 
                     value => $pass},
	{actualParameterName => "branch", 
                     value => $branch},
	{actualParameterName => "fail", 
                     value => $fail}
]});

$ec->logout();

print "Status: 200 OK", "\n";
print "Content-type: text/plain", "\n\n";
