def calculate_optimal_fare(travelKm, travelMins, driveSpeed, ratePerKm, walkSpeed):

    driveTime = (travelKm / driveSpeed) * 60  # Total time it takes to drive entire distance.
    walkTime = (travelKm / walkSpeed) * 60    # Total time it takes to walk entire distance.

    if walkTime > travelMins and driveTime > travelMins:  # If student won't be on time at all.
        return print("Won't make it!")
    else:
        if walkTime <= travelMins:  # If student will be on time by walking entire distance.
            return print("00.00")
        else:
            for meter in range(int(travelKm * 1000), -1, -1):
                driveDist = (travelKm * 1000) - meter                 # Meters to be driven.
                driveTime = ((driveDist / (driveSpeed * 1000)) * 60)  # Drive time based on current distance.
                walkTime = ((meter / (walkSpeed * 1000)) * 60)        # Walk time based on current distance.
                drivePrice = driveDist * (ratePerKm / 1000)           # Fare based on current drive distance.
                if (walkTime + driveTime) <= travelMins:  # If student will be on time by part driving, part walking.
                    return print(str("%.2f" % drivePrice))
                    break
                elif meter == 0:  # If student will only be on time by driving entire distance.
                    return print(drivePrice)

# calculate_optimal_fare(8, 10, 90, 2, 6)
calculate_optimal_fare(68, 86, 85, 13, 6)