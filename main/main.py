
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from school import student

수학 = student.Student(80)

st.write("테스트")
st.write(수학.test_sum())
print(수학.test_sum())


