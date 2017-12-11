from fleet import Fleet
from thing import Thing

fleet = Fleet()
thing1 = Thing("Get milk")
thing2 = Thing("Remove the obstacles")
thing3 = Thing("Stand up")
thing4 = Thing("Eat lunch")
thing3.complete()
thing4.complete()
fleet.things = [thing1, thing2, thing3, thing4]

# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch


print(fleet)

