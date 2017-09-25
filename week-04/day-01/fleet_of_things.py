from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

fleet.add(Thing("Get milk"))
fleet.add(Thing("Remove the obstacles"))
fleet.add(Thing("Stand up"))
fleet.add(Thing("Eat lunch"))

fleet.things[2].complete()
fleet.things[3].complete()

print(fleet)