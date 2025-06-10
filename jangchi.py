class Odam:
    """odam klassi"""
    def __init__(self, qol, oyoq):
        self.arm = qol
        self.leg = oyoq
        
class Jangchi(Odam):
    """odam klassidan vorislik"""
    energiya = 100
    jang_qiyinligi = 30
    
    def jang_qil(self):
        if self.energiya >= self.jang_qiyinligi:
            self.energiya -= self.jang_qiyinligi
            print(f"{self.jang_qiyinligi} energiya sarflandi {self.energiya} energiya qoldi")
        else:
            print('energiya yetarli emas')

jangchi1 = Jangchi(2, 2)
# jangchi1.jang_qil()
# jangchi1.jang_qil()
# jangchi1.jang_qil()
# jangchi1.jang_qil()

class Doctor(Odam):
    """shifokor classi"""
    dorilar = ['trimol', 'asperin', 'suv']
    
    def __init__(self, qol, oyoq):
        super().__init__(qol, oyoq)
    
    def davola(self):
        if len(self.dorilar) > 0:
            dori = self.dorilar.pop()
            print(f"{dori} bilan davolandi")
        else:
            print('dori qolmadi')
            
shifokor1 = Doctor(2, 2)
shifokor1.davola()
shifokor1.davola()
shifokor1.davola()
shifokor1.davola()

class JangchiShifokor(Jangchi, Doctor):
    pass

jsh1 = JangchiShifokor(2, 2)
jsh1.jang_qil()