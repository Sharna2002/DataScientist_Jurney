* The spped trap -<br>
    number_list =  list(range(1,1000001)) <b> # This line indicate a list.</b> <br>
    number_set = set(range(1,1000001))  <b> #  This line indicates a set.</b> <br>

    print(-1 in number_list) <br>
    print(-1 in number_set)<br>
    For searching -1 in a list use the time complexity of O(N), beacuse internally it follows the loop function to search.In the otherhand set/ dict is searching the value of the the -1, which time complexity is O(1).
