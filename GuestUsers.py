from email.message import EmailMessage
from xkcdpass import xkcd_password as xp
import smtplib, datetime, shlex, subprocess, sys, os
import pandas as pd
import pendulum

campuses = [('ahs','edannewitz@auhsdschools.org',''),
             ('chs','edannewitz@auhsdschools.org',''),
             ('llhs','edannewitz@auhsdschools.org',''),
             ('mhs','edannewitz@auhsdschools.org','')]
docontacts = 'chenriksen@auhsdschools.org,rkahrer@auhsdschools.org'
pendulum.week_starts_at(pendulum.MONDAY)
pendulum.week_ends_at(pendulum.FRIDAY)
today = pendulum.now().add(days=3)
start = today.start_of('week')
end = today.end_of('week')
theweekof = "for the week of " + start.strftime('%B %d') + " to " + end.strftime('%B %d')
df = pd.DataFrame(campuses, columns = ['campusname','contacts','emailbody'])
wordfile = xp.locate_wordfile()
mywords = xp.generate_wordlist(wordfile=wordfile, min_length=2, max_length=8)
for x in df.index:
    msg = EmailMessage()
    df['emailbody'][x] = "Passwords for Guest accounts this week are:\n\n"
    for i in range(5):
        password = xp.generate_xkcdpassword(mywords, delimiter="", acrostic=df['campusname'][x])
        df['emailbody'][x] = df['emailbody'][x] + "Guest user -> " + df['campusname'][x] + "-guest" + str(i+1) + "@auhsdschools.org"  + "     Password -> " + password + "\n\n"
        gamstring = "E:\\GAMADV-XTD3\\gam.exe update user " + df['campusname'][x] + "-guest" + str(i+1) + "@auhsdschools.org password " + password
        p = subprocess.Popen(["powershell.exe",gamstring],stdout=sys.stdout)
        p.communicate()
    s = smtplib.SMTP('10.99.0.202')
    msg['Subject'] = "Guest Account Passwords for " + df['campusname'][x].upper() + " " + theweekof
    msg['From'] = 'donotreply@auhsdschools.org'
    msg['To'] = str(df['contacts'][x] + "," + docontacts)
    msg.set_content(df['emailbody'][x])
    s.send_message(msg)
