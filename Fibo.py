#! Python 3.11
# Using a txt file to store the calculated values of the fibonacci sequence
# Recursive version 

import sys


class Fibo():
    def __init__ (self, n:int) -> None:
        """ 
        Where we store the calculated values of the fibonacci sequence
        """
        self.dico = {0:1,1:1}
        self.n = n
        
    def read_data(self, file:str) -> None:
        """
        Read the data from the file

        Args:
            file (str): Relative path to the file
        """
        with open("results.txt", "r") as f:
            for line in f:
                key, value = line.split(";")
                self.dico[int(key)] = int(value)
    
    def calculate_iter(self, file:str) -> int:
        """
        Fibo recursive function

        Args:
            file (str): Relative path to the file
            n (int): Number we want to calculate the fibonacci sequence

        Returns:
            int: Result of the fibonacci sequence
        """
        self.read_data(file)
        
        try:
            return self.dico[self.n]
        
        except:
            max_key = max(self.dico.keys())
            while max_key <= self.n:
                max_key += 1
                self.dico[max_key] = self.dico[max_key - 1] + self.dico[max_key-2]
            self.write_data(file)
            return self.dico[self.n]
            
        
        
    def calculate_recu(self, file: str) -> int:
        """
        Fibo iterative function

        Args:
            file (str): Relative path to the file
            n (int): Number we want to calculate the fibonacci sequence

        Returns:
            int: _description_
        """
        self.read_data(file)
        result = self.__wrapper()
        self.write_data(file)
    
    def __wrapper(self) -> int:
        """
        Wrapper for the recursive function

        Args:
            n (int): Number we want to calculate the fibonacci sequence

        Returns:
            int: _description_
        """
        if self.n in self.dico: 
            return self.dico[self.n]
        else:
            self.dico[self.n] = self.__wrapper(self.n-1) + self.__wrapper(self.n-2)
            return self.dico[self.n]
        
                
    def write_data(self, file) -> None:
        """
        Write the data to the file

        Args:
            file (_type_): _description_
        """
        
        with open(file, "w") as f:
            for key, value in self.dico.items():
                f.write(str(key) + ";" + str(value) + "\n")
    
