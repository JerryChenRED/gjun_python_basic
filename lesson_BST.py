class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_tree = None
        self.right_tree = None

    def insert(self, data):
        if self.data != data:  # Is root node != data?
            if data < self.data:
                # insert to left_tree
                if self.left_tree:
                    self.left_tree.insert(data)
                else:
                    self.left_tree = BinarySearchTree(data)
            else:
                # insert to right_tree
                if self.right_tree:
                    self.right_tree.insert(data)
                else:
                    self.right_tree = BinarySearchTree(data)

    def delete(self, data):
        if data < self.data:
            if self.left_tree:
                self.left_tree = self.left_tree.delete(data)
            else:  # 沒有這個數字
                print(f"Delete {data} fail: data not found")
            return self
        elif data > self.data:
            if self.right_tree:
                self.right_tree = self.right_tree.delete(data)
            else:  # 沒有這個數字
                print(f"Delete {data} fail: data not found")
            return self
        else:
            # data == self.data
            # 找人遞補我當前這個空缺
            if self.left_tree == None and self.right_tree == None:  # 1. 無子樹
                return None
            elif self.left_tree == None and self.right_tree != None:  # 2 只有右子樹
                return self.right_tree
            elif self.left_tree != None and self.right_tree == None:  # 2 只有左子樹
                return self.left_tree
            else:
                # 3. 左右子樹都在, 找右子樹最小值遞補
                substitute = self.right_tree  # 右子樹根節點
                while substitute.left_tree != None:
                    substitute = substitute.left_tree
                self.data = substitute.data
                self.right_tree = self.right_tree.delete(substitute.data)
                return self

    def search(self, data):  # 有無找到: 有的話return True,  沒有的話 return False
        if data < self.data:
            return self.left_tree.search(data) if self.left_tree else False
        elif data > self.data:
            return self.right_tree.search(data) if self.right_tree else False
        else:
            # data == self.data
            return True

    def preOrderTraversal(self):
        pass

    def inOrderTraversal(self):
        pass

    def postOrderTraversal(self):
        pass


if __name__ == "__main__":
    bst = BinarySearchTree(5)
    bst.insert(4)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)

    bst.insert(11)
    bst.insert(10)
    bst.insert(7)
    bst.insert(8)

    bst.delete(5)

    print("From Root: ", bst.data)
    trace_left_tree = bst.left_tree
    while trace_left_tree != None:
        print("Find left tree: ", trace_left_tree.data)
        trace_left_tree = trace_left_tree.left_tree

    print("From right child node")
    trace_right_tree = bst.right_tree
    while trace_right_tree != None:
        print("Find right tree: ", trace_right_tree.data)
        trace_right_tree = trace_right_tree.left_tree

    print("Search 12: ", bst.search(12))
    print("Search 11: ", bst.search(11))
