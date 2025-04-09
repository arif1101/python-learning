# Enqueue: Adds a new element to the queue.

# Dequeue: Removes and returns the first (front) element from the queue.

# Peek: Returns the first element in the queue.

# isEmpty: Checks if the queue is empty.

# Size: Finds the number of elements in the queue.

myQueue = []
# Enqueue
myQueue.append('A')
myQueue.append('R')
myQueue.append('I')
myQueue.append('F')
print("Queue: ", myQueue)
# Dequeue
element = myQueue.pop(0)
print("Dequeue: ", element)
print(myQueue)
#Peek
peekElement = myQueue[0]
print('Peek: ', peekElement)
isEmpty = False
if(len(myQueue)<=0):
    isEmpty = True;
print("isEmpty: ", isEmpty)
# size
print(len(myQueue))