
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from school import student

sooni = student.Student(80,70,60,80,70)


st.write("class test")
st.write(f"총점: {sooni.student_sum()}/평균: {sooni.student_average():.1f}")
# print(sooni.student_sum(), sooni.student_average())



