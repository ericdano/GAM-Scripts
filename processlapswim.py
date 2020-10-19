import pandas as pd
import os, sys, shlex, subprocess

#This is part of a crontab job that
#takes a sheet from Google Sheets, using GAM, and dumps it to a target folder
#then we call this script to process the csv file
#then the crontab job uses gam sync to sync the group (to add or delete members)
#probably could just put this ALL in python but..........oh well..

lapswim = pd.read_csv('/home/gamuser/LapSwim/LapSwimResponses.csv')
header = ["E-mail Address"]
lapswim.to_csv('/home/gamuser/LapSwim/LapSwimResponses.csv', index = False, header = False, columns = header)

#bash script that is called by crontab
#!/bin/sh
#rm /home/gamuser/LapSwim/*
#/usr/local/gamadv-xtd3/gam user user@school.org get drivefile id PUTGOOGLESHEETIDHERE format csv targetfolder /home/gamuser/LapSwim/
#/usr/bin/python /root/gamscripts/processlapswim.py
#/usr/local/gamadv-xtd3/gam update group lapswimemaillist sync members file /home/gamuser/LapSwim/LapSwimResponses.csv
#rm /home/gamuser/LapSwim/LapSwimResponses.csv
