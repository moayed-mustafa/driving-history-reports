


# Attempting to read the file
drivers_list = []
drivers_object = {}
with open('input.txt', 'r') as File:
    # you want to read the data
    # push driveres into the list
    # once it has finished looping over your and assiging all your drivers
    # you want to use File.seek(0) to have it rewind
    # then you want to check for trips this time
    # figure out the speed of the trip based on the time and the miles covered
    # discard trips that average speed less than 5mph or exeeds 100 mph
    # update a sort of a data structure that holds all of the driveres with their mph for all trips

    # print(File.read())
    for line in File:
        print(line)
        if line.startswith('Driver'):
            line = line.strip()
            drivers_list.append(line)
            drivers_object[line] = 0
print(drivers_list)
print(drivers_object)

