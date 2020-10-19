# GAM-Scripts
<h2>Introduction</h2>
Various GAM Scripts done with Python, Bash, or Powershell for doing various things with a G-Suite for Education domain (or any domain really).
<h2>Requirements</h2>
<a href="https://github.com/taers232c/GAMADV-XTD3">GAMADV-XTD3</a> is required for all these scripts. 
<h2>Installation</h2>
You need Python 3.8.5 or later installed.
You need GAMADV-XTD3 installed
<h2>Scripts</h2>
<ul><li><b>GetUsers.py</b> - Python script I wrote to rotate guest passwords to 5 guest accounts being used in our district for logins to join Zoom meetings and what not. The passwords are then emailed to people at the site and select district contacts. In use, this script is scheduled to run on Friday afternoons to notify the sites of the next weeks passwords for the accounts.
<li><b>processlapswim.py</b> - Part of a crontab bash shell script that calls GAM that csv dumps a google sheet (which is from a form where people sign up for a campus's lapswim program), and then syncs members of the group.
</ul>
