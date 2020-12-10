import requests
import time
import datetime
from datetime import date




# setting/getting date for request
d = date.today() - datetime.timedelta(days=1)
d = f"{d.day}/{d.month}/{d.year}"
d = time.mktime(datetime.datetime.strptime(d, "%d/%m/%Y").timetuple())
d = int(d)

# requesting the page or data
main_url = "https://api.stackexchange.com/2.2/questions?"
response = requests.get(main_url, {
                        "order": "desc", "tagged": "python", "site": "stackoverflow", "fromdate": d, "pagesize": 100})

# sorting the data
x = response.json()
list = []
for i in x["items"]:
    if not i["is_answered"]:
        list.append([i["title"], i["link"], i["tags"]])

# creating an file
with open("stack_over_flow_questions.txt", "w") as f:
    for i in list:
        f.write("Name: ")
        f.write(i[0])
        f.write("\n")

        f.write("Tags: ")
        f.write(str(i[2]))
        f.write("\n")

        f.write("Link: ")
        f.write(i[1])
        f.write("\n")

        f.write("\n")

