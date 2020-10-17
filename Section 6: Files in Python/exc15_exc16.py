"""
CSV file - csv_file.txt

Manchester United,Manchester,UK
Real Madrid,Madrid,Spain
Juventus,Turin,Italy
"""

#solution
import json

json_list = []

csv_file = open('csv_file.txt', 'r')

for line in csv_file.readlines():
    club, city, country = line.strip().split(',')
    data = {
        "club": club,
        "country": country,
        "city": city
    }
    json_list.append(data)

csv_file.close()

json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)
json_file.close()

# mine
# import csv
# import json
#
# with open("csv_file.txt", "r") as csv_file:
#   reader = csv.DictReader(csv_file)
#
# to_json = []
#
# for row in reader:
#     to_json.append(row)
##
# with open("json_file.txt", "w") as json_file:
#   json_string = json.dumps(to_json)
#   json_file.write(json_string)

"""
Cary's

def csv_to_json(csv_filename, json_filename):
    import csv
    import json
    
    # Reading a file using csv.DictReader
    f_csv = open(csv_filename, "r")
    reader = csv.DictReader(f_csv, fieldnames = ["club", "city", "country"])
    csv_to_dict = list(reader)
    f_csv.close()
 
    # Converting output to a json file
    f_json = open(json_filename, "w")
    json.dump(csv_to_dict, f_json)  # turns a dict into a json file
    f_json.close()
 
csv_to_json("csv_file.txt", "json_file.txt")
"""