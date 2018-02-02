theaters = [
	{
		"name": "The Seeing Place Theater",
		"seats": 100,
		"actors": ["Meredith Hermann", "Ayden Mosciski", "Robyn Baumbach Sr.", "Joyce Bruen DDS", "Annabell Marks MD", "Madisyn Schinner", "Macy Hamill Jr.", "Johnpaul Aufderhar", "Howard Schaden IV", "Novella Sporer"],
		"plays": []
	
	},
	{
		"name": "The Emerald Theater",
		"seats": 250,
		"actors": ["Clifford O'Conner", "Prof. Velva Collier III", "Josianne Schinner", "Novella Klocko", "Mr. Cale Walsh", "Roma Kris", "Luna Smith IV", "Prof. Eino Koepp", "Annabel Keebler", "Cedrick Ullrich", "Kaela Hoeger", "Miss Laila Zemlak", "Arielle Nikolaus", "Miss Blanche Cassin", "Mr. Hazle Stehr"],
		"plays": []
	
	}
]
theaters[0]["plays"].append(
	{
		"date": "21.02.2018",
		"name": "Addams Family",
		"actors": [theaters[0]["actors"][0], theaters[0]["actors"][3], theaters[0]["actors"][5], theaters[0]["actors"][6], theaters[0]["actors"][8]],
		"ticket price": 200,
		"sold tickets": 30,
		"topicality": True
	}
)
theaters[0]["plays"].append(
	{
		"date": "21.01.2018",
		"name": "The Book of Mormon",
		"actors": [theaters[0]["actors"][1], theaters[0]["actors"][3], theaters[0]["actors"][5], theaters[0]["actors"][7], theaters[0]["actors"][9]],
		"ticket price": 250,
		"sold tickets": 90,
		"topicality": False
	}
)
theaters[1]["plays"].append(
	{
		"date": "27.03.2018",
		"name": "Bonnie and Clyde",
		"actors": [theaters[1]["actors"][0], theaters[1]["actors"][3], theaters[1]["actors"][5], theaters[1]["actors"][6], theaters[1]["actors"][8], theaters[1]["actors"][10], theaters[1]["actors"][11]], 
		"ticket price": 170,
		"sold tickets": 200,
		"topicality": True
	}
)
theaters[1]["plays"].append(
	{
		"date": "27.04.2018",
		"name": "Chicago",
		"actors": [theaters[1]["actors"][0], theaters[1]["actors"][4], theaters[1]["actors"][5], theaters[1]["actors"][7], theaters[1]["actors"][9], theaters[1]["actors"][11]], 
		"ticket price": 150,
		"sold tickets": 98,
		"topicality": True
	}
)
#show all data
i=-1
for list in theaters:
	i=i+1
	print(" ")
	print("------THEATER------")
	for x in list:
		if x != "plays":
			print (x," - ", theaters[i][x])
		else:
			print(" ")
			print ("----PLAY----")
			print (theaters[i][x][0]['date'])
			b=-1
			for list in theaters[i][x]:
				b=b+1
				for n in list:
					print (n, " - ", theaters[i][x][b][n])
				print ('------------')
			print("-------------------")
			print("")
#-------
print("")
print("")


print('----ALL PLAYS----')
print(theaters[0]["plays"][0]['name'])
print(theaters[0]["plays"][1]['name'])
print(theaters[1]["plays"][0]['name'])
print(theaters[1]["plays"][1]['name'])
print('-----------------')

print("Number of actors in ”{theater}” = ”{num}”".format(theater = theaters[0]["name"], num = len(theaters[0]["actors"])))
print("Play “{name}”, availiable tickets num = ”{num}”".format(name = theaters[0]["plays"][0]["name"],num = theaters[0]["seats"] - theaters[0]["plays"][0]["sold tickets"]))

print("Play “{name}”, profit = ”{money}”".format(name = theaters[1]["plays"][0]["name"],money = theaters[1]["plays"][0]["sold tickets"]*theaters[1]["plays"][0]["ticket price"] ))

theaters[1]["plays"][1]["sold tickets"] = theaters[1]["plays"][1]["sold tickets"]+1
print("Sold tickets =",theaters[1]["plays"][1]["sold tickets"])
	
	
	
