import random
import smtplib
import datetime as dt
import pandas as pd
# from pprint import pprint
import random
my_email = "araajjheshk.cs20@rvce.edu.in"  # plain text can lead to error ->typos
password = "!q)o@w(i"
##################### Extra Hard Starting Project ######################

now = dt.datetime.now()
day =  now.day
month = now.month
year = now.year

file = pd.read_csv('birthdays.csv')
pan_dict = file.to_dict()
print(pan_dict)
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
# print(int(file['year']))
#check if all coresspoding time stuff matches
# print(year,month,day)
# print(int(file['year']),int(file['month']),int(file['day']))
# print(year == int(file['year'])  and month ==int(file['month'])  and day ==int(file['day']))
if year == int(file['year'])  and month ==int(file['month'])  and day ==int(file['day'])  :

    #choosing random letter template
    ran_file = random.randint(1,3)
    with open(f'letter_{ran_file}.txt') as temp :
        content = temp.read()
        #print(pan_dict['name'][0])
        content = content.replace('[NAME]',pan_dict['name'][0])
       # print((content))
    with smtplib.SMTP('smtp.gmail.com') as connection :
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="aryan.kulkarni22@gmail.com",
                            msg=f"Subject:Motivational Quote \n\n {content}")





# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



#
