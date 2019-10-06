class Laptops():

    def __init__(self,cpu,encryption,gpu):
        self.cpu = cpu
        self.encryption = encryption
        self.gpu = gpu
        
class PCom(Laptops):

    def __init__(self,cpu,encryption,gpu):
        super().__init__(cpu,encryption,gpu)
        self.wattage = None

    def add_wattage(self,wattage):
        self.wattage = wattage

    def displayspecs(self):
        print("Specs: ", self.cpu, self.encryption, self.gpu)
        if self.wattage != None:
            print("TDP: ", self.wattage)
        

Inspiron35 = PCom("i7-8565U","False","UHD-620")
print(Inspiron35.cpu)
print(Inspiron35.displayspecs())
Inspiron35.add_wattage("65W")
print(Inspiron35.displayspecs())
