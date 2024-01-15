class Telephone:
    def __init__(self,connection):
        self.connection=connection
        
class Computer:
    def __init__(self,processor):
        self.processor=processor

class Smartphone(Telephone,Computer):
    def __init__(self,connection,processor,camera) -> None:
      
        Computer.__init__(self,processor=processor)
        Telephone.__init__(self,connection=connection)
        self.camera=camera

       

sp=Smartphone(processor='MediaTeck',connection='5G',camera='64mp')