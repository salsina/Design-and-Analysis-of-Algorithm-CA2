import sys
sys.setrecursionlimit(10**5)
class Node:
    def __init__(self,dad_id,num,_id):
        self.father_id = dad_id
        self.number = num
        self.node_id = _id
        self.children = []
        self.as_odd = 0
        self.as_even = 0
    def add_child(self,child_node):
        self.children.append(child_node)
        
class Tree:
    def __init__(self):
        self.nodes = []
    
    def add_node(self,father_id,num):
        new_node = Node(father_id,num,len(self.nodes)+1)
        self.nodes.append(new_node)
        if father_id != -1:
            self.nodes[father_id-1].add_child(new_node)
    
    def show_ans_root(self):
        root_node = self.nodes[0]
        even_answer = root_node.as_even
        odd_answer = root_node.as_odd
        if even_answer > odd_answer:
            print(even_answer)
            return
        print(odd_answer)
        
    def node_answer(self,node_id):
        current_node = self.nodes[node_id-1]
        
        if len(current_node.children) == 0 :
            current_node.as_odd = current_node.number
            return 
        
        for child in current_node.children:
            self.node_answer(child.node_id)

        odd_answers = 0
        max_answer = 0
        min_difference_even_odd = 10 ** 5
        
        for child in current_node.children:
            if child.as_odd > child.as_even:
                odd_answers += 1
                max_answer += child.as_odd
            else:
                max_answer += child.as_even
            if abs(child.as_even - child.as_odd) < min_difference_even_odd :
                min_difference_even_odd = abs(child.as_even - child.as_odd)
        
        if odd_answers % 2 == 0:
            current_node.as_even = max_answer
            current_node.as_odd = max_answer + current_node.number
            return
        
        current_node.as_even = max_answer - min_difference_even_odd
        ans = max_answer - min_difference_even_odd + current_node.number
        if max_answer > ans:
            current_node.as_odd = max_answer
            return
        current_node.as_odd = ans
        
tree = Tree()                
num_of_nodes = int(input())
for i in range(num_of_nodes):
    data = [int(x) for x in input().split()]
    father_id = data[0]
    num = data[1]
    tree.add_node(father_id,num)

root_id = 1
tree.node_answer(root_id)
tree.show_ans_root()
