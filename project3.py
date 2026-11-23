# Elian Martinez
# COMP 250-002
# Project 3

from collections import deque #we need deque for the BFS, it works as our queue.

# step 1: Node class
class treeNode: #this is one student in the tree. every student is a node.
    def __init__(self, student_id, name, major):
        self.student_id = student_id #the ID is a number, and it is the key we use to order the tree.
        self.name = name 
        self.major = major
        self.left = None #the left child starts empty, smaller IDs will go here.
        self.right = None #the right child starts empty too, bigger IDs will go here.

# step 2: BinarySearchTree class
class BinarySearchTree: #this class keeps the root and all the tree methods.
    def __init__(self):
        self.root = None #the tree starts empty, so there is no root yet.

    def insert_function(self, student_id, name, major):
        new_node = treeNode(student_id, name, major) #first we make the new node with the student info.
        if self.root is None: #if the tree is empty, the new student becomes the root.
            self.root = new_node
            return True #this means the student was added.
        current = self.root #if not empty, we start at the root and walk down the tree.

        while True:
            if student_id == current.student_id:
                return False #the ID is already there, so we don't add it. False means it was already there
            elif student_id < current.student_id: #smaller IDs go to the left.
                if current.left is None: #if the left place is empty, this is where the new node goes to
                    current.left = new_node
                    return True
                current = current.left #for this if the place is taken, we move to that node and keep going down
            else:
                if current.right is None: #if the right place is empty, the new node goes here.
                    current.right = new_node
                    return True
                current = current.right #if the place is taken, we move to that node and keep going down.

    def search_function(self, student_id):
        visited = [] #this list keeps the IDs we have check
        current = self.root #we start with the root note
        while current is not None:
            visited.append(current.student_id) #for this every node we look at gets saved in the list visited
            if student_id == current.student_id:
                return current, visited
            elif student_id < current.student_id:
                current = current.left 
            else:
                current = current.right # here if the ID we want is bigger, we go right.
        return None, visited

    # step 3: DFS, these use recursion.
    def pre_order(self, node): #pre-order is center, left,right.
        if node is None: #this is our base case
            return
        print_student(node) #first we print the current node.
        self.pre_order(node.left) #and with this the function calls itself with the left child.
        self.pre_order(node.right) #after that we go the right child.

    def in_order(self, node): #in-order is left, center, right.
        if node is None: # this is our base case
            return
        self.in_order(node.left) 
        print_student(node) 
        self.in_order(node.right) 

    def post_order(self, node):
        if node is None:
            return
        self.pre_order(node.left) 
        self.pre_order(node.right)
        print_student(node)

    # step 4: BFS, this one uses a queue (deque).
    def bfs(self):
        queue = deque([self.root]) #we start the queue with the root node.
        level = 1 #we make it level 1
        while queue: #this will run unitl the queue doesn't have a note
            size = len(queue) 
            ids_level = [] #this list will keep the IDs

            for i in range(size):
                current = queue.popleft() #takes the node from the front of the queue.
                ids_level.append(str(current.student_id)) #this will turn the ID into a string 
                if current.left:
                    queue.append(current.left) #the children go to the back of the queue
                if current.right:
                    queue.append(current.right)
            print(f"Level {level}: " + " ".join(ids_level)) #this join will puts all the IDs of the level in one line with spaces
            level += 1 #now we go to the next level.

    # step 5: tree stats, these use recursion
    def count_nodes(self, node):
        if node is None: #base case, an empty place counts as 0.
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right) #1 for this node plus the left and right sides.

    def height(self, node):
        if node is None: #base case, an empty place has a height of 0.
            return 0
        left_height = self.height(node.left) + 1 #the height of the left side.
        right_height = self.height(node.right) + 1#the height of the right side.
        return max(left_height, right_height) #we take the taller side and add 1 for this node. a tree with only a root gives 1.

    def find_smallest(self):
        current = self.root #we start at the root.
        while current.left is not None: #the smallest ID is always going left, until there is nothing more on the left.
            current = current.left
        return current

    def find_largest(self):
        current = self.root #we start at the root.
        while current.right is not None: #the largest ID is always going right, until there is nothing more on the right.
            current = current.right
        return current

# helper functions
def print_student(node): #this is the format of how we show a student.
    print(f"ID: {node.student_id} | Name: {node.name} | Major: {node.major}")

def get_int(message): #this works as an error catcher, it keeps asking until the we type a whole number.
    while True: #the loop only stops when we return a number.
        try:
            return int(input(message)) #if the input can become an int, we give it back and the function ends.
        except ValueError: #if the we type letters or something else, int() gives an error
            print("Invalid input. Please enter a whole number.")

def get_text(input_text): #this works until it is not empty
    while True:
        return input(input_text).strip()

def show_menu(): #this is the menu that we get when we run the code.
    print()
    print("----- STUDENT TAP -----\n")
    print("1. Add a new student\n")
    print("2. Search for a student by ID\n")
    print("3. Display all students (DFS)\n")
    print("4. Display all students (BFS)\n")
    print("5. Display tree stats\n")
    print("6. Display smallest and largest IDs\n")
    print("7. Exit\n")

# step 6: each menu option has its own function.
def add_student(tree): #option 1.
    student_id = get_int("Enter student ID: ") #get_int makes sure the ID is a whole number.
    name = get_text("Enter student name: ")
    major = get_text("Enter student major: ")
    if tree.insert_function(student_id, name, major): #insert gives True if it was added and False if the ID was a duplicate.
        print("Student added.")
    else:
        print(f"A student with ID {student_id} already exists. Student not added.")

def search_student(tree): #option 2.
    student_id = get_int("Enter the student ID to search for: ")
    found, visited = tree.search_function(student_id) #search gives back two things, the node (or None) and the list of IDs we visited.
    if found is None:
        print("Student not found.")
    else:
        print_student(found) #we show the record of the student.
    path = " -> ".join(str(x) for x in visited) #this turns the list into 50 -> 30 -> 40.
    print(f"Nodes visited: {path}")
    print(f"Total nodes checked: {len(visited)}") #the length of the list is the number of nodes we checked.

def display_dfs(tree): #option 3.
    print("1. Pre-order")
    print("2. In-order")
    print("3. Post-order")
    choice = get_int("Choose a traversal (1-3): ")
    while choice < 1 or choice > 3: #this will let you pick 1 or 3
        print("Invalid choice.")
        choice = get_int("Choose a traversal (1-3): ")
    if choice == 1:
        tree.pre_order(tree.root) #we send the root to start the recursion.
    elif choice == 2:
        tree.in_order(tree.root)
    else:
        tree.post_order(tree.root)


def display_bfs(tree): #option 4.
    tree.bfs()

def display_stats(tree): #option 5.
    print(f"Total students: {tree.count_nodes(tree.root)}") #we start counting from the root.
    print(f"Height of the tree: {tree.height(tree.root)}") #and we start the height from the root too.

def display_m_l(tree): #option 6.
    print("Smallest ID:")
    print_student(tree.find_smallest())
    print("Largest ID:")
    print_student(tree.find_largest())

def main():
    tree = BinarySearchTree() #we make the tree here.
    while True: #the menu keeps showing until we use oction picks 7.
        show_menu()
        choice = get_int("Choose an option: ") #this only accepts whole numbers, so letters won't crash the program.
        if choice == 1:
            add_student(tree)
        elif choice == 2:
            search_student(tree)
        elif choice == 3:
            display_dfs(tree)
        elif choice == 4:
            display_bfs(tree)
        elif choice == 5:
            display_stats(tree)
        elif choice == 6:
            display_m_l(tree)
        elif choice == 7:
            print("Goodbye!")
            break
        else: #if it is a number but not from 1 to 7, we end up here.
            print("Invalid option. Choose a number from 1 to 7.")

main()

'''
Time Complexity Questions
1. O(log n): why searching a BST is O(log n) only when the tree is balance.

First tree: I added 50, 30, 70, 20, 40, 60, 80.
Search for 80: 50 - 70 - 80, so it checked 3 nodes.

Second tree: I added 10, 20, 30, 40, 50, 60, 70.
Search for 70: 10 - 20 - 30 - 40 - 50 - 60 - 70, so it checked 7 nodes.

In the balanced tree, every step down throws away half of the
students that are left, so the number of steps is log n. With 7 students,
log n is 3, and that is why we only checked 3 nodes.
In the second tree, every new ID was bigger than the one before it, so every student
went to the right. This makes the tree a straight line, like a linked list, and each step
only gets rid of one student. We had to check all 7 nodes, which is O(n).

2. Explain why building a balanced tree of n students is O(n log n), and estimate the
total number of steps to build a balanced tree of 1,000 students.

O(n log n), we adding one student and it takes log n steps, and to build the tree we
insert n students, one after the other. So it is n students times log n steps each,
which is n log n.
For 1,000 students, log n is about 10 (because 2 to the power of 10 is 1,024).
So 1,000 x 10 = 10,000 steps.
'''