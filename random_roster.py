import random

# open roster
def get_names():
    with open("roster.txt", "r") as roster:
        list_names = []
        for line in roster:
            list_of_line = line.split()
            # grab just the name
            list_of_line.pop()
            # put the names in list
            list_names.append(" ".join(list_of_line))
    list_names.sort()
    return list_names


def remove_absent(list_names):
    is_absent = input("Is anyone absent today :(  ? \n yes or no: ")
    if is_absent == 'yes':
        # find who is absent
        bonus_prompt = ""
        removed_notice = ""
        while True:
            print("Roster:")
            for idx, name in enumerate(list_names):
                print("{}: {}".format(idx, name))
            print(removed_notice)
            print(bonus_prompt)
            absent_idx = input("Enter index of absent or 'done' if done: ")
            if absent_idx == 'done':
                break
            try:
                absent_idx = int(absent_idx)
            except:
                bonus_prompt = "Warning: Integer Value Expected"
                continue
            if absent_idx >= len(list_names) or absent_idx < 0:
                bonus_prompt = "Provide index between 0 and {}".format(
                                len(list_names)-1)
                continue
            else:
                bonus_prompt = ""
                # adjust list for absent
                removed = list_names.pop(absent_idx)
                removed_notice += "\nYou removed {} from lists.".format(
                    removed)
    return


def get_random(list_names):
    # get random number
    n = random.randint(0, len(list_names)-1)
    # get name at index
    name = list_names[n]
    # remove if used
    list_names.remove(name)
    return name


def random_names(list_names):
    while True:
        stop = input("Enter 'stop' to stop or anything to cont.: ")
        if stop == 'stop':
            break
        elif len(list_names) > 0:
            print(get_random(list_names))
        else:
            break


def main():
	list_names = get_names()
	remove_absent(list_names)
	random_names(list_names)


if __name__ == '__main__':
	main()