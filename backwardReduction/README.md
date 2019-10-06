run.py is a script in which the generator generates the desired number of scenarios and a distances matrix, and then applies 
backward reduction to reduce the number of scenarios by the desired number.

To run it, pass in the number of initial scenarios and scenarios to be eliminated as arguments 
For eg. python run.py 10 5 

run.py runs the implementation of Backward Reduction using the data structure SortedList (http://www.grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedcontainers.SortedList) with O(n^2) complexity.


*****

runOld.py is a script that does essentially the same thing, except it runs with O(n^2 * log(n)). It has been kept in order to test correctness of the other implementation. To run it correctly, a change has to be made to generator.py on line 29, where the 0 has to be replaced with a 100. 


*****

Run the scripts kScript.sh and nScript.sh using:


bash kScript.sh > outK.txt


bash nScript.sh > outN.txt


*****

To run scatter.plot, you need to "pip install scipy"

