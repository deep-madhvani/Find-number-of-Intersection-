def count_intersections(radian, identifiers):
    active_chords = []
    intersections = 0
    
    # Iterate through the chords
    for i in range(len(identifiers)):
        # If it's a starting point, add it to active chords
        if identifiers[i].startswith("s_"):
            active_chords.append(identifiers[i])
        # If it's an ending point, remove the corresponding starting point
        else:
            start_identifier = "s" + identifiers[i][1:]
            if start_identifier in active_chords:
                active_chords.remove(start_identifier)
            # Calculate intersections with active chords
            intersections += len(active_chords)
    
    return intersections

# Example 1 for radian - (0.78,1.47,1.77,3.92) identifier -(s1,s2,e1,e2) intersection is 1
# Example 2 for radian - (0.9,1.3,1.70,2.92) identifier -(s1,e1,s2,e2) intersection is 0 
radian = (0.9, 1.3, 1.70, 2.92)
identifiers = ("s_1", "e_1", "s_2", "e_2")
print(count_intersections(radian, identifiers))  # Output: 0