#binary search tree
import key
nos=[12,15,6,8,3,7,1,9]

def search(root,key):

 if (root is none) or( root .val==key):
        return root
print(root)

 if (root.val < key):
     return search(root.right,key)
print(root.right)

 if(root.val>key):
     return search(root.left,key)
print(root.left)