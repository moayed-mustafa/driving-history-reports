# Pseudocode and thought process: -

### After reading the requirements here's my initial way of thinking about how to solve it technically:-
- Declare an empty list that will hold driveres names.
- Declare an empty object that will later on hold key value pairs of the driver and his milage
- The object will be updated with every new caluclation
- Read the file
- push driveres into the list
- once it has finished looping and registering all the drivers
- Rewind the  file
- Check for trips this time
- Figure out the speed of the trip based on the time and the miles covered
- Discard trips that average speed less than 5mph or exeeds 100 mph
- Update the object that holds all of the driveres with their mph for all trips
- Return the object