import sys
sys.setrecursionlimit(10**5)
class Yaal:
    def __init__(self,_id,fe,se):
        self.id = _id
        self.small_edge = fe
        self.big_edge = se
        self.contracts = []
        self.status = ""
    def add_contract(self,yaal):
        self.contracts.append(yaal)
        
class Graph:
    def __init__(self,num_of_vs,num_of_edges):
        self.insides = []
        self.outsides = []
        self.num_of_edges = num_of_edges
        self.num_of_yaals = num_of_vs
        self.counter = 0
        self.yaals = []
        self.impossible = False
        self.initializing()
        self.finding_contract()
        self.check_all_status()
        
    def initializing(self):
        for i in range(self.num_of_yaals):
            a_b = [int(x) for x in input().split()]
            first_edge = a_b[0]
            second_edge = a_b[1]
            if first_edge < second_edge:
                new_yaal = Yaal(len(self.yaals)+1,first_edge,second_edge)
            else:
                new_yaal = Yaal(len(self.yaals)+1,second_edge,first_edge)
            self.yaals.append(new_yaal)
    
    def find_contract_for_one_yaal(self,current_yaal):
        left_sides = []
        right_sides = []
        for i in range(current_yaal.small_edge + 1,current_yaal.big_edge):
            left_sides.append(i)
        for i in range(current_yaal.big_edge + 1, current_yaal.big_edge + self.num_of_edges - \
            (current_yaal.big_edge - current_yaal.small_edge)):
            if i <= self.num_of_edges:
                right_sides.append(i)
            else:
                right_sides.append(i - self.num_of_edges)

        for yaal in self.yaals:
            if (yaal.small_edge in left_sides) and (yaal.big_edge in right_sides) or\
                (yaal.big_edge in left_sides) and (yaal.small_edge in right_sides):
                    current_yaal.add_contract(yaal)
        
    def finding_contract(self):
        for yaal in self.yaals:
            if yaal.small_edge == yaal.big_edge - 1:
                continue
            elif (yaal.small_edge == 1) and (yaal.big_edge == self.num_of_edges):
                continue
            self.find_contract_for_one_yaal(yaal)
            
    def check_yaal(self,yaal,I_or_o):
        if self.impossible == True:
            return
        if yaal.status != "":
            if yaal.status == I_or_o:
                return
            self.impossible = True
            return
        
        yaal.status = I_or_o
        for contract_yaal in yaal.contracts:
            if self.impossible == True:
                return    
            if I_or_o == "I":
                    self.check_yaal(contract_yaal,"O")
            else:
                self.check_yaal(contract_yaal,"I")
            
    def check_all_status(self):
        for yaal in self.yaals:
            if self.impossible == True:
                return
            if len(yaal.contracts) == 0:
                yaal.status = "I"
                continue
            if yaal.small_edge == yaal.big_edge - 1:
                yaal.status = "I"
            elif (yaal.small_edge == 1) and (yaal.big_edge == self.num_of_edges):
                yaal.status = "I"
            elif yaal.status == "":
                self.check_yaal(yaal,"I")     
            
    def show_answer(self):
        if self.impossible == True:
            print("Impossible")
            return
        ans = ""
        for yaal in self.yaals:
            ans += yaal.status
        print(ans)
            
n_l = donbale = [int(x) for x in input().split()]
num_of_dots = n_l[0]
num_of_vs = n_l[1]
graph = Graph(num_of_vs,num_of_dots)
graph.show_answer()
