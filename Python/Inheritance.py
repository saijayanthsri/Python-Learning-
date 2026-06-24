#inheritance
#single inheritance
#multilevel inheritance
#multiple inheritance
#hierarchical inheritance
#hybrid inheritance

#single

class parent:
    def par(self):
        parent_property= 5000
        print(f"Parent property={parent_property}")
        self.a=parent_property
class child(parent):
    def ch(self):
        self.par()
        child_property= 2500
        print(f"Child property={child_property}")
        d= self.a + child_property
        print(f"All property={d}")

e=child()
e.ch()

#multilevel

class grandparent:
    def gpar(self):
        gran_prop= 90000
        print(f"Grand parent property={gran_prop}")
        self.g = gran_prop
        
class parent(grandparent):
    def par(self):
        self.gpar()
        parent_prop = 45000
        print(f"Parent property={parent_prop}")
        self.p =parent_prop

class child(parent):
    def ch(self):
        self.par()
        child_prop= 15000
        print(f"Child property= {child_prop}")
        d= self.g + self.p + child_prop
        print(f"All property={d}")
e = child()
e.ch()


#multiple

class father:
    def fahh(self):
        father_prop=40000
        print(f"Father property={father_prop}")
        self.f=father_prop

class mother:
    def maa(self):
        mother_prop = 50000
        print(f"Mother property={mother_prop}")
        self.m =mother_prop

class child(father,mother):
    def ch(self):
        self.maa()#imp
        self.fahh()#imp
        child_prop = 25000
        print(f"Child property={child_prop}")
        b=self.f + self.m + child_prop
        print(f"All property={b}")

c=child()
c.ch()


#hierarchical

class parent:
    def par(self):
        parent_prop= 35000
        print(f"Parent property={parent_prop}")
        self.p = parent_prop

class child1(parent):
    def ch1(self):
        self.par()
        child1_prop=10000
        print(f"Child 1 property={child1_prop}")
        d=self.p//2
        print(f"Child 1 share{d}")

class child2(parent):
    def ch2(self):
        self.par()
        child2_prop=10000
        print(f"Child 2 property={child2_prop}")
        self.j = child2_prop
        e=self.p//2
        print(f"Child 2 share{e}")
c=child1()
c.ch1()

d=child2()
d.ch2()

#hybrid

class parent:
    def par(self):
        parent_prop = 100
        print(f"Parent property={parent_prop}")
        self.a=parent_prop

class child1(parent):
    def ch1(self):
        self.par()
        child1_prop= 50
        print(f"Child 1 property={child1_prop}")
        self.b=child1_prop

class child2(parent):
    def ch2(self):
        #self.par()
        child2_prop= 50
        print(f"Child 2 property={child2_prop}")
        self.c=child2_prop

class child3(child1,child2):
    def ch3(self):
        self.ch1()
        self.ch2()
        child3_prop= 50
        print(f"Child 3 property={child3_prop}")
        self.d=child3_prop


g=child3()
g.ch3()
