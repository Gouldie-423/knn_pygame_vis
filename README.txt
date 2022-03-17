The purpose of this project is to generate an interactive game where the user slowly uncovers the decision boundaries created by the knn algorithm by using their mouse position on the whitespace of the game display.

The majority of the processing takes place within the following 4 functions. 

-create_points: This function is designed to create unique datapoint combinations each time the script is run. For each iteration within the explict for loop a total of 4 values are created representing the x and y axis of both the blue and red groups. These datapoints are then put in a list with the x value representing the 0th index and the y value representing the 1st index. This list is then added into a larger list that contains all data points that is returned by the function. 

-euclidean_distance: This function calculates the euclidean distance between two points. This function contains 3 arguments. The 'index' argument is necessary because this function is run through part of an explicit for loop and on each iteration we'll need to access a specific index on either the red_points or blue_points list that we created earlier with create_points. The following two arguments are 'point_a' and 'point_b', both of the arguments are intended to be lists. point_a represents a previously generated datapoint and point_b represents the end users current mouse position. Euclidean distance is calculated by squaring the differences on each axis before taking the square root of the sum of those differences. Squaring these values before taking the square root leaves any positive number unchanged while getting the absolute value of every negative number. This is integral to KNN algorithm because otherwise a distance represented by a large negative number would be considered to have a closer distance than a positive number very close to zero when we sort the distances in ascending order to select the nearest k number of neighbors to base our classification off of.

-sort_distances: The purpose of this function is to calculate each of the distances from each of the red/blue point lists and assigning a label indicating 0 if the point is blue and 1 if the point is red. The distances are then put into an ascending order before being returned.

-pick_color: Using the previously created distances variable from sort_distances and 'k' we take a slice of the distances list to get the 'k' number of nearest neighbors before using a series of conditional statements to count the labels I previously applied in sort_distnaces. Depending on what color has the highest tally a pygame variable is returned that has the corresponding rgb values for either a red or blue label.

The remaineder of the workspace is as follows. Lines 63-80 contain all of the global variables required for the pygame workspace. 

Lines 92-96 indicate that if the 'r' key is pressed while the app is running it will clear the screen, clear red/blue points, and create new randomized datapoints to visualize from again.

Lines 97-101 generate the mouse position on the application and pass it in as an argument to sort_distances each and every frame that the game display is running to return a list of distances.

Lines 103-110 contain two explicit for loops that re-draw the randomly created points each frame to ensure they remain on the top layer and don't get drawn over by player input.

Lines 113-116 declare a variable called mouse_point that follows the mouse position before passing that into a pygame.draw.ellipse  function that creates a user controlled cursor. The pick_color function is passed in as an argument and returns the apropriate color that the cursor draws onto the game display. The distances list is then cleared at the end so datapoints from previous frames are not included.  