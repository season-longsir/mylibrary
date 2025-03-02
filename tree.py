'''
This document mainly deals with tree structure types.
---Author: Season
---Language: Python
---Signature: S and A
              PHJsi
#############
#####---#####
###--   --###
#--S and A--#
###--   --###
#####---#####
#############
~~~~~~~~~~~~~
#############
#####---#####
###--   --###
#---PHJsi---#
###--   --###
#####---#####
#############
'''





class Tree:
    def __init__(self,treeNodeData:str = "") -> None:
        self.data = treeNodeData
        self.deep = 0
        self.__children = []
        self.parent = None
        self.end = []
    
    def parents(self) -> list:
        if self.parent is None:
            return []
        return Tree.parents(self.parent) + [self.parent]
    
    @property
    def children(self) -> list:
        return self.__children
    
    def add(self,subTreeNode:type) -> type:
        assert isinstance(subTreeNode,Tree)
        subTreeNode.deep = self.deep + 1 
        subTreeNode.parent = self
        if subTreeNode not in  self.__children:
            self.__children.append(subTreeNode)
        for node in subTreeNode.children:
            Tree.add(subTreeNode,node)
        return subTreeNode
    
    def get_thisParents(self) -> dict:
        parents = []
        for this in self.parents():
            parents.append(this.data)
        self.Tree_up = {self.data:parents}
        return self.Tree_up

class TreePrint(Tree):
    def print(self) -> None:
        print('  '* self.deep + self.data)
        for subTreeNode in self.children:
                TreePrint.print(subTreeNode)
    
    def tree_print(self) -> None:
        if self.parent:        
            lines = ""
            for node in self.parents():
                if node.parent is not None:
                    if node != node.parent.children[-1]:
                        lines += "│ "
                    else:
                        lines += "  "
            if self.parent.children[-1] == self: 
                lines += "└─" 
            else:
                lines += "├─"
            print(lines ,end = "")
        print(self.data)
        for subTreeNode in self.children:
            TreePrint.tree_print(subTreeNode)





if __name__ == "__main__":
    print("Welcome to my library: tree.py!")
