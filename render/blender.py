import bpy
import math
import functools

class Blender:
    def __init__(self):
        self.time = 0.0
        self.data = {"t": [0, 0, 0], "q": [0, 0, 0], "delta_time": [0]}
        self.iterNum = 0
        self.N = 100
        self.delta_time = 0.1

    # type data is dict 
    def assignToBlender(self, name):
        bpy.data.objects[name].location[0] = self.data["t"][0]
        bpy.data.objects[name].location[1] = self.data["t"][1]
        bpy.data.objects[name].location[2] = self.data["t"][2]

        bpy.data.objects[name].rotation_euler[0] = self.data["q"][0]
        bpy.data.objects[name].rotation_euler[1] = self.data["q"][1]
        bpy.data.objects[name].rotation_euler[2] = self.data["q"][2]

    def update(self):
        self.data["t"] = [10*math.cos(6.28 / self.N * self.iterNum), 10*math.sin(6.28 / self.N * self.iterNum), 0]
        self.data["q"] = [0, 0, 6.28 / self.N * self.iterNum]
        self.iterNum += 1


def renderUpdate(blender):
    blender.assignToBlender("Cube")
    blender.update()
    if blender.iterNum > 99:
        raise Exception("stop iter")
    return blender.delta_time


def main():
    blender = Blender()
    bpy.app.timers.register(functools.partial(renderUpdate, blender))


if __name__=="__main__":
    try:
        main()  
    except Exception:
        print("done")
