import bpy

class Blender:
    def __init__(self):
        self.time = 0.0

    # type data is dict 
    def assignToBlender(self, data, name):
        bpy.data.Objects[name].location[0] = data["t"][0]
        bpy.data.Objects[name].location[1] = data["t"][1]
        bpy.data.Objects[name].location[2] = data["t"][2]

        bpy.data.Objects[name].rotation_quaternion[0] = data["q"][0]
        bpy.data.Objects[name].rotation_quaternion[1] = data["q"][1]
        bpy.data.Objects[name].rotation_quaternion[2] = data["q"][2]
        bpy.data.Objects[name].rotation_quaternion[3] = data["q"][3]
        self.delta_time = data["delta_time"]


