# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs

def create_new_verbs(verbs, preverb):
    result = []
    for i in range(len(verbs)):
        result.append(preverb + verbs[i])
    print(result)

verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

create_new_verbs(verbs, preverb)