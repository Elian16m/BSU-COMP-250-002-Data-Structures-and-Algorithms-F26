# Elian Martinez
# COMP 250-002
# Project 3
from collections import deque

# this is creating the treenote class
class TreeNode:
    def __init__(self, student_id, name, major):
        self.id = student_id
        self.name = name
        self.major = major
        self.left = None
        self.right = None

class BinarySearchTree:
    