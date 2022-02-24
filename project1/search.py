# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    stack.push((problem.getStartState(),[]))
    currPath=[]
    visited=[]
    while not stack.isEmpty():
        data = stack.pop()
        currState = data[0]
        currPath = data[1]
        if problem.isGoalState(currState):
            return currPath
        else:
            visited.append(currState)
            for successor in problem.getSuccessors(currState):
                if not successor[0] in visited:
                    newPath=[]
                    for path in currPath:
                        newPath.append(path)
                    newPath.append(successor[1])
                    stack.push((successor[0],newPath))
    return currPath

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"

    queue = util.Queue()
    queue.push((problem.getStartState(),[]))
    currPath=[]
    ans=[]
    visited=[problem.getStartState()]
    while not queue.isEmpty():
        data = queue.pop()
        currState = data[0]
        currPath = data[1]
        if problem.isGoalState(currState):
            return currPath
        else:
            for successor in problem.getSuccessors(currState):
                if not successor[0] in visited:
                    visited.append(successor[0])
                    newPath=[]
                    for path in currPath:
                        newPath.append(path)
                    newPath.append(successor[1])
                    queue.push((successor[0],newPath))
    return currPath

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    pq.push((problem.getStartState(),[]),0)
    currPath=[]
    visited=[]
    while not pq.isEmpty():
        data = pq.pop()
        currState = data[0]
        currPath = data[1]
        if problem.isGoalState(currState):
            return currPath
        else:
            if not currState in visited:
                visited.append(currState)
                for successor in problem.getSuccessors(currState):
                    newPath=[]
                    for path in currPath:
                        newPath.append(path)
                    newPath.append(successor[1])
                    pq.push((successor[0],newPath),problem.getCostOfActions(newPath))
    return currPath

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    pq.push((problem.getStartState(),[]),0)
    currPath=[]
    visited=[]
    while not pq.isEmpty():
        data = pq.pop()
        currState = data[0]
        currPath = data[1]
        if problem.isGoalState(currState):
            return currPath
        else:
            if not currState in visited:
                visited.append(currState)
                for successor in problem.getSuccessors(currState):
                    newPath=[]
                    for path in currPath:
                        newPath.append(path)
                    newPath.append(successor[1])
                    pq.push((successor[0],newPath),problem.getCostOfActions(newPath)+heuristic(successor[0],problem))
    return currPath


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
