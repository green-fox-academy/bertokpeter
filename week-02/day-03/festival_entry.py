watchlist = []

security_alcohol_loot = 0

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival

# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot)
#  and let them enter the festival
def security_check(list_of_poeple):
    enter_list = []
    global security_alcohol_loot
    for i in list_of_poeple:
        if i["guns"] > 0:
            watchlist.append(i["name"])
        elif i["alcohol"] > 0:
            security_alcohol_loot = security_alcohol_loot + i["alcohol"]
            i["alcohol"] = 0
            enter_list.append(i["name"])
        else:
            enter_list.append(i["name"])
    print(watchlist)
    print(security_alcohol_loot)
    print(enter_list)
security_check(queue)