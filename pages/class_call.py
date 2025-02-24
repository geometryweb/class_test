
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from school import student

sooni = student.Student(80, 70, 60, 80, 70)
malgun = student.Student(70, 80, 50, 70, 30)

st.write("class test")
st.write(f"총점: {sooni.student_sum()}/평균: {sooni.student_average():.1f}")
# print(sooni.student_sum(), sooni.student_average())
# print(sooni.__eq__(malgun))
st.write("순이와 순이의 성적은 같다" ,sooni.__eq__(sooni))
st.write("순이와 맑은이의 성적은 같다" ,sooni.__eq__(malgun))
st.write("순이와 맑은이의 성적은 다르다",sooni.__ne__(malgun))


