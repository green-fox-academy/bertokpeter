class Tree(object):
    def __init__(self, tree_type, leaf_color, age, sex):
        self.type = tree_type
        self.leaf_color = leaf_color
        self.age = age
        self.sex = sex


tree1 = Tree("oak","green", 150, "female")
tree2 = Tree("maple","brown", 200, "male")
tree3 = Tree("oak","red", 50, "female")
tree4 = Tree("apple","green", 100, "male")
tree5 = Tree("plum","yellow", 250, "female")

print(tree2.type)