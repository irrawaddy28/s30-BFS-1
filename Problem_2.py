'''
207 Course Schedule
https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.


Solution:
1. Graph and topological sorting:

Step 1: Create a graph representation. Course is a node (totally numCourses nodes) and prerequisites[i]  (where i=1,..,E) is a directed edge from bi to ai, i.e. bi --> ai

Step 2: Determine the in-degree for each node based on the graph.
The in-degree of a node is the number of edges coming into it. In other words, determine the number of parents for each child node. In this scenario, it represents the number of prerequisites for a course.
Populate the in-degree values in an in-degree array, where the index of the array is the node id (or child id) and the value at the index is the number of parents of the node id.

Step 3: Create an adjacency list (hash map). For each node (parent), determine the children (outgoing edges). The parents represent the keys and the corresponding children represent the values of the adjacency list.

Step 4: Initiate a queue and add all nodes with an in-degree of 0 to it.
Note: Any node enqueued in the  queue must have an in-degree of 0. Otherwise, it cannot be enqueued. When it has an in-degree of 0, it means we have visited all its parents. In this scenario, it means all prereqs (parents) for that course (child) have been completed.

Step 5: This is the topological sorting step.
While the queue is not empty, process the nodes:
- Dequeue a node (= a course with no prerequisites). This is equivalent to visiting this node (parent)
- Retrieve the children of the parent (dequeued node) from the adjacency list.
- Now decrease the in-degree count by 1 of the retrieved children in the in-degree array because we visited the parent (by dequeing the node)
- If the in-degree count of a child is 0, then that child can be added to queue

Note: The topological sorted order is the sequence of nodes popped from the queue.

Step 6: Once the queue is empty, count the number of 0's in the in-degree array.
If that count is equal to the numCourses (total no. of courses), then return True. Else return False.

https://youtu.be/AIdppB34TEQ?t=2149

Time: O(V+E), Space: O(V+E)
Note: In a fully connected graph, E = V-1. Hence, hash map size=O(V*E)=O(V^2) and time = O(VE)
'''
from collections import defaultdict, deque

def course_scheduling(N, prereqs):
    if not prereqs or N == 0:
            return True
    indegrees = [0]*N # index = child, value = num parents, O(V)
    adj_list = defaultdict(list) # key = parent, values = children, O(V+E)

    # Determine the in-degree and adjacency list of the graph
    for p in prereqs: # O(E)
        child = p[0]
        parent = p[1]
        indegrees[child] += 1
        adj_list[parent].append(child)

    # Populate the queue with all those children who have no parents
    q = deque()
    count = 0
    for child, num_parents in enumerate(indegrees): # O(V)
        if num_parents == 0:
            count += 1
            q.append(child)

    # Now for each parent popped (visited), get the corresponding children from hash map and decrease their number of parents count by 1 (since the visited parent was popped)
    while q: # O(V)
        parent = q.popleft()
        for child in adj_list[parent]: # O(E)
            indegrees[child] -= 1
            if indegrees[child] == 0:
                q.append(child)
                count += 1
    return (count == N)

def run_course_scheduling():
    tests = [ ([[2,0],[3,0],[1,2],[1,3],[4,2],[5,4],[5,3]],6,True),
              ([[1,0],[2,1],[3,2],[1,3]],4,False),
              ([[1,0]],2,True),
              ([[0,1]],2,True),
              ([[1,0],[0,1]],2,False),
              ([[1,4],[2,4],[3,1],[3,2]],5,True), # strange test case: prereqs has 4 courses 1-4 but total courses = 5. Course 0 is not in prereq and yet all courses can be completed
    ]
    for test in tests:
        prereqs, num_courses, ans = test[0], test[1], test[2]
        can_finish = course_scheduling(num_courses, prereqs)
        print(f"\nTotal no. of courses = {num_courses}")
        print(f"Prereqs = {prereqs}")
        print(f"Can finish all courses? {can_finish}")
        print(f"Pass: {ans == can_finish}")


run_course_scheduling()
