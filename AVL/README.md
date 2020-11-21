# AVL   

**ABSTRACT**   
This is kind of Height-Balancing Binary Search Tree. 
It was devised by Adelson-Velskii and Landis to reduce time complexity of Binary Search Tree of which it is `O(n)`. 
And in AVL tree, it gets `O(log n)` time complexity. 
Being balanced means that height of the left sub-tree and height of the right sub-tree differ by at most one.    
<br/>   

## Table of Contents   
+ [1. Algorithm](#1-algorithm)
   + [1.1 AVL Rotations](#11-avl-rotations)
+ [2. Time Complexity](#2-time-complexity)

## 1. Algorithm      
All the nodes are unique, and left child node is always smaller than its parent node and right child node is always greater than its parent node(just like the Binary Search Tree). 
But the difference with the Binary Search Tree is that AVL has **Balance Factor(BF)**. Balance Factor is as follows:    
`height(left_subtree) − height(right_subtree)`    
And we call it balanced only when BF is not more than **1**(so it can have following values: **-1**, **0**, **1**).   
<br/>    

### 1.1 AVL Rotations      

#### Single Rotation - _Left Rotation_   
When a new node is instered 

#### Single Rotation - _Right Rotation_   


#### Double Rotation - _Left-Right Rotation_   


#### Double Rotation - _Right-Left Rotation_   


<br/>   

## 2. Time Complexity   

### Average   

   
### Best Case   


### Worst Case   

