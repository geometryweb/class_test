import streamlit as st

class Shape:
    def __init__(self):
        pass
    def main_display(self):
        st.write("_"*10)
        self.sub_display()
        st.write(f"{self.__class__} 넓이: {self.area()}")
        
class Circle(Shape):
    def __init__(self, 반지름):
        self.__PI = 3.14
        self.__radius = 반지름
    def sub_display(self):
        print(f"원의 반지름은: {self.__radius}")
    def area(self): 
        return self.__PI * self.__radius**2
    
circle = Circle(10)
circle.main_display()