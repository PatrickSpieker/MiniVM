class Machine:
    def __init__(self):
        self.pos = 0
        self.memory = [0 for i in range(512)]

    def printMem(self):
        print self.memory

    def load(self, arr):
        for i in range(len(arr)):
            self.memory[i] = arr[i] 

    def step(self):
        op = self.memory[self.pos:self.pos+3]
        self.pos += 3
        opcode = op[0]
        arg1 = op[1]
        arg2 = op[2]
        if opcode == 1: # print
            print self.memory[arg1]
        elif opcode == 2: # add
            self.memory[arg1] += self.memory[arg2]
        elif opcode == 3: # set
            self.memory[arg1] = arg2
        elif opcode == 4: # jump
            self.pos = arg1
        elif opcode == 5: # if 
            if self.memory[arg1] != arg2:
                self.pos += 3
        else: # panic
            self.printMem() 
            raise Exception


mach = Machine()
mach.printMem()
mach.load([5,25,5, 0,255,255, 1,25,255, 2,25,6, 4,0,255])
while True:
    mach.step()



 

