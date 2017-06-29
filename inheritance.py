class Fish:
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    def Swim(self):
        print("Fish is swiming")
    def swim_back(self):
        print("fish swim back")
        
'''Creating a child class:'''
class Trout(Fish):
    pass
terry = Trout("sam")
print(terry.first_name + "" + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.Swim()
terry.swim_back()
