import math

class Writer:
    def __init__(self, iterNum, dT) -> None:
        self.N = iterNum
        self.deltaTime = dT
        self.timestamp = list()
        self.t = list()
        self.q = list()
    
    def generate(self):
        for i in range(self.N):
            t_i = [10*math.cos(6.28 / self.N * i), 10*math.sin(6.28 / self.N * i), 0]
            q_i = [0, 0, 6.28 / self.N * i]
            self.timestamp.append(i * self.deltaTime)
            self.t.append(t_i)
            self.q.append(q_i)
    
    def write(self):
        with open("./motion_path.txt", "w") as f:
            for time, t_i, q_i in zip(self.timestamp, self.t, self.q):
                f.write("{} {} {} {} {} {} {}\n".format(time, t_i[0], t_i[1], t_i[2], q_i[0], q_i[1], q_i[2]))
                
if __name__=="__main__":
    w = Writer(200, 0.1)
    w.generate()
    w.write()