# Find-number-of-Intersection-
Given a list of chords in a circle, count the number of intersections, if any. For simplicity's sake, assume all starting and ending points are unique.

Below is my Aproach 
1)Initialize an empty list to keep track of active chords.
2)Iterate through the list of chords. For each chord:
-If it's a starting point (s_x), add it to the list of active chords.
-If it's an ending point (e_x), remove the corresponding starting point from the list of active chords.
3)Calculate the number of intersections by checking the number of active chords at each point.
Return the total count of intersections.

