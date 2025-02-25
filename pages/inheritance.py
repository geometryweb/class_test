import streamlit as st

class Shape:
    def __init__(self):
        pass

    def main_display(self):
        st.write("_"*10)
        st.write(self.sub_display())
        st.write(f"{self.__class__.__name__} 넓이: {self.area()}")

class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self._radius = radius

    def sub_display(self):
        return f"원의 반지름은: {self._radius}"

    def area(self):
        return self.PI * self._radius**2

class Square(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def sub_display(self):
        return f"사각형 가로 길이: {self._width} / 사각형 세로 길이: {self._height}"

    def area(self):
        return self._width * self._height

st.subheader("클래스")        
circle = Circle(10)
circle.main_display()
square = Square(10, 10)
square.main_display()