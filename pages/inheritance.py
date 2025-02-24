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
        return print(f"원의 반지름은: {self.__radius}")
    def area(self): 
        return self.__PI * self.__radius**2
class Square(Shape):
    def __init__(self, 가로, 세로):
        self.__width = 가로
        self.__height = 세로
    def sub_display(self):
        print(f"사각형의 가로: {self.__width} 사각형의 세로: {self.__height}")
    def area(self):
        return self.__width * self.__height
        
circle = Circle(10)
circle.main_display()
square = Square(10, 10)
square.main_display()