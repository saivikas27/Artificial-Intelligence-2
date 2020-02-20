
class BinaryTree():


    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid
      self.value = None

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.value = value
    def getNodeValue(self):
        return self.value

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())


def minimax_tree(tree,total_depth,current_depth,maxTurn,Index):
        if(current_depth==total_depth):
            return tree.getNodeValue()
        if (maxTurn):
            tree.setNodeValue(max(minimax_tree(tree.getLeftChild(),total_depth,current_depth+1,False,Index*2),
                       minimax_tree(tree.getRightChild(),total_depth,current_depth+1,False,Index*2+1)))
            x=tree.getNodeValue()
            return x

        else:
            tree.setNodeValue(min(minimax_tree(tree.getLeftChild(),total_depth,current_depth+1,True,Index*2),
                       minimax_tree(tree.getRightChild(),total_depth,current_depth+1,True,Index*2+1)))
            x=tree.getNodeValue()
            return x

myTree = BinaryTree("0")
myTree.insertLeft("1_0")
myTree.insertRight("1_1")
l_10= myTree.getLeftChild()
l_10.insertLeft("2_0")
l_10.insertRight("2_1")
l_11= myTree.getRightChild()
l_11.insertLeft("2_2")
l_11.insertRight("2_3")
l_20=l_10.getLeftChild()
l_20.insertLeft("3_0")
l_20.insertRight("3_1")
l_21=l_10.getRightChild()
l_21.insertLeft("3_2")
l_21.insertRight("3_3")
l_22=l_11.getLeftChild()
l_22.insertLeft("3_4")
l_22.insertRight("3_5")
l_23=l_11.getRightChild()
l_23.insertLeft("3_6")
l_23.insertRight("3_7")
l_30=l_20.getLeftChild()
l_30.insertLeft("4_0")
l_30.insertRight("4_1")
l_31=l_20.getRightChild()
l_31.insertLeft("4_2")
l_31.insertRight("4_3")
l_32=l_21.getLeftChild()
l_32.insertLeft("4_4")
l_32.insertRight("4_5")
l_33=l_21.getRightChild()
l_33.insertLeft("4_6")
l_33.insertRight("4_7")
l_34=l_22.getLeftChild()
l_34.insertLeft("4_8")
l_34.insertRight("4_9")
l_35=l_22.getRightChild()
l_35.insertLeft("4_10")
l_35.insertRight("4_11")
l_36=l_23.getLeftChild()
l_36.insertLeft("4_12")
l_36.insertRight("4_13")
l_37=l_23.getRightChild()
l_37.insertLeft("4_14")
l_37.insertRight("4_15")
l_40=l_30.getLeftChild()
l_40.setNodeValue(3)
l_41=l_30.getRightChild()
l_41.setNodeValue(10)
l_42=l_31.getLeftChild()
l_42.setNodeValue(2)
l_43=l_31.getRightChild()
l_43.setNodeValue(9)
l_44=l_32.getLeftChild()
l_44.setNodeValue(10)
l_45=l_32.getRightChild()
l_45.setNodeValue(7)
l_46=l_33.getLeftChild()
l_46.setNodeValue(5)
l_47=l_33.getRightChild()
l_47.setNodeValue(9)
l_48=l_34.getLeftChild()
l_48.setNodeValue(2)
l_49=l_34.getRightChild()
l_49.setNodeValue(5)
l_50=l_35.getLeftChild()
l_50.setNodeValue(6)
l_51=l_35.getRightChild()
l_51.setNodeValue(4)
l_52=l_36.getLeftChild()
l_52.setNodeValue(2)
l_53=l_36.getRightChild()
l_53.setNodeValue(7)
l_54=l_37.getLeftChild()
l_54.setNodeValue(9)
l_55=l_37.getRightChild()
l_55.setNodeValue(1)

minimax_tree(myTree,4,0,True,0)
print("The optimal value of the tree is",myTree.getNodeValue())

