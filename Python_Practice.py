print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')



# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


    brands = ["Samsung", "LG", "Sony"]

    if "LG" in brands:
        print("Yes")

    if "Panasonic" not in brands:
        print ("Yes")


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


x = 0
while x <= 5:
    print(x)
    x = x + 1


for county in counties:
    print(county)


numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)


for num in range(5):
    print(num)


for i in range(len(counties)):
    print(counties[i])

municipios = ("Ecatepec", "Cuautitlan", "Coacalco")
municipios

for i in range(len(municipios)):
        print(municipios[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
counties_dict

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for values in counties_dict.values():
    print(values)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(str(county) + " county has", str(voters) + " registered voters")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

voting_data

for county_dict in voting_data:
    print(county_dict)

for county_dict in range(len(voting_data)):
    print(voting_data[county_dict])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict["county"])

for county_dict in voting_data:
    print(county_dict["registered_voters"])


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes.")

print(message_to_candidate)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

counties_dict

for county, voters in counties_dict.items():
    print(f"{county} county has {voters: ,} registered voters")

for county, voters in counties_dict.items():
    print(str(county) + " county has", str(voters) + " registered voters")


import datetime as dt
now = datetime.datetime.now()
print("The time right now is ", now)