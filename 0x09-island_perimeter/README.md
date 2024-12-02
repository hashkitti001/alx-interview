# 0x09 - Island perimeter

Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

# Solution 
We solve this by checking through the elements of the grid. 
Once we find a one, we increment a `perimeter` variable by 4 and then for each adjacent cell, if any, we decrease perimeter by one, as only n - 1 edge constitute the perimeter for an island with more than one cell.

We then return the perimeter

