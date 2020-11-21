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
      + [1.1.1 Single Rotation - Left Rotation]
+ [2. Time Complexity](#2-time-complexity)
<br/>   

## 1. Algorithm      
All the nodes are unique, and left child node is always smaller than its parent node and right child node is always greater than its parent node(just like the Binary Search Tree). 
But the difference with the Binary Search Tree is that AVL has **Balance Factor(BF)**. Balance Factor is as follows:    
`height(left_subtree) − height(right_subtree)`    
And we call it balanced only when BF is not more than **1**(so it can have following values: **-1**, **0**, **1**).   
<br/>    

### 1.1 AVL Rotations      

_**NOTE**: In this AVL algorithm, you need to make sure what each term means. Please refer to [this page](https://en.wikipedia.org/wiki/Tree_rotation)._    

#### 1.1.1 Single Rotation - _Left Rotation_ `a.k.a. RR(Right Right Case)`    
When a new node is instered in 

<br/>   

#### 1.1.2 Single Rotation - _Right Rotation_ `a.k.a. LL(Left Left Case)`   

<br/>   

#### 1.1.3 Double Rotation - _Left-Right Rotation_ `a.k.a. LR(Left Right Case)`   

<br/>   

#### 1.1.4 Double Rotation - _Right-Left Rotation_ `a.k.a. RL(Right Left Case)`   


<br/>   

## 2. Time Complexity   

### Average   

   
### Best Case   


### Worst Case   

