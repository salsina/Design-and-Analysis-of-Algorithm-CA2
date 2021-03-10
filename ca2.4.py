class Pixel:
    def __init__(self,dark,num):
        self.darkness = dark
        self.num_of_pixels = num
class Picture:
    def __init__(self,basisnum,darknessvariety):
        self.num_of_basis = basisnum
        self.pixels = []
        self.grouping_costs = []
        self.darkness_variety = darknessvariety
        self.D = []
    def add_pixel(self,darkness,num_of_pixels):
        new_pixel = Pixel(darkness,num_of_pixels)
        self.pixels.append(new_pixel)
    
    def print_answer(self,darkness_variety):
        if num_of_basis == darkness_variety:
            print(0)
            return
        if self.num_of_basis == 1:
            up = 0
            down = 0
            for pixel in self.pixels:
                up += pixel.darkness * pixel.num_of_pixels
                down += pixel.num_of_pixels
            basis = int(up/down)
            ans = 0
            for pixel in self.pixels:
                ans += pixel.num_of_pixels * ((basis - pixel.darkness)**2)
            print(ans)
            return
        picture.make_cc()
        picture.make_D()
        print(picture.D[-1][-1])
        
    def calc_cc(self,i,j):
        sum_of_darknesses = 0
        
        for pixel in self.pixels[i:j+1]:
            sum_of_darknesses += pixel.darkness
            
        miangin = sum_of_darknesses/(j-i+1)
        grouping_cost = 0
        
        for pixel in self.pixels[i:j+1]:
            grouping_cost += (pixel.num_of_pixels) * (pixel.darkness -miangin)**2
            
        return grouping_cost
    
    def make_cc(self):
        self.cc = [[0 for i in range(self.darkness_variety)] for j in range(self.darkness_variety)]
        for i in range(len(self.cc)):
            for j in range(i+1,len(self.cc[i])):
                self.cc[i][j] = self.calc_cc(i,j)
        
    def make_D(self):
        self.D = [[0 for i in range(self.darkness_variety)] for j in range(self.num_of_basis)]
        for i in range(self.darkness_variety):
            self.D[0][i] = self.cc[0][i]
            
        for i in range(1,self.num_of_basis):
            for m in range(self.darkness_variety):
                answer = 10 ** 100
                for j in range(m):
                    temp_ans = self.D[i-1][j] + self.cc[j+1][m]
                    if temp_ans < answer:
                        answer = temp_ans
                self.D[i][m] = int(answer)
            
                    
d_k = [int(x) for x in input().split()]
darkness_variety = d_k[0]
num_of_basis = d_k[1]
picture = Picture(num_of_basis,darkness_variety)

for i in range(darkness_variety):
    c_e = [int(x) for x in input().split()]
    darkness = c_e[0]
    num_of_pixels = c_e[1]
    picture.add_pixel(darkness,num_of_pixels)

picture.print_answer(darkness_variety)
