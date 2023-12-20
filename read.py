import random


class Read():
    def __init__(self,seq:str):
        self.__seq=seq
        self.__mapped=False
        self.__position=-1
        
    def __len__(self):
        return len(self.__seq)
    
    def get_seq(self):
        return self.__seq
    
    def get_pos(self):
         return self.__position
    
    def add_pos(self,pos):
            if not self.__mapped:
                self.__position=pos

    def was_mapped(self):
        self.__mapped=True

    def get_mapping_status(self):
         return self.__mapped

    def reverse_complentation(self):
        dic={"A":"T","T":"A","C":"G","G":"C"}
        new_seq=""
        old_seq=self.get_seq()
        for i in range(len(self.get_seq())-1,-1,-1):
              new_seq+=dic[old_seq[i]]
        self.__seq=new_seq

    def error_rate(self,rate):
        alphabet=["A","G","C","T"]
        a=list(self.get_seq())
        nb=int(len(self.get_seq())*rate)
        for i in range(nb):
            a[random.randint(0,len(self)-1)]=alphabet[random.randint(0,3)]
        self.__seq="".join(a)