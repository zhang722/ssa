class Reader:
    def __init__(self) -> None:
        self.timestamp = list()
        self.t = list()
        self.q = list()
      
    def read(self, filename):
        with open(filename, "r") as f:
            lines = f.read().splitlines()
            lines = list(map(lambda x : x.split(' '), lines))
            for line in lines:
                self.timestamp.append(float(line[0]))
                self.t.append([float(x) for x in line[1:4]])
                self.q.append([float(x) for x in line[4:7]])

if __name__=="__main__":
    r = Reader()
    r.read("./motion_path.txt")
    t = r.t
    for time in t:
        print(time)