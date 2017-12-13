def check_anagram(sorted_one, sorted_two):
    sorted_one = sorted_one.lower()
    sorted_two = sorted_two.lower()
    sorted_one = "".join(sorted(sorted_one))
    sorted_two = "".join(sorted(sorted_two))
    if sorted_one == sorted_two:
        return True
    return False

check_anagram("Dog", "God")