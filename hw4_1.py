class Pet:
    def init(self, name): #the "init" should be "__init__"
        self.name = name
        
    def introduce(): #"self" should be inside the parenthesis
        print (“hello, I am ”, self.name)