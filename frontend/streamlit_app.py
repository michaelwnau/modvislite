import streamlit as st

total_points = st.slider("Total points", 0, 100, 50)
num_turns = st.slider("Number of turns", 1, 10, 5)

Point = namedtuple("Point", 'x y')
data = []

points_per_turn = total_points / num_turns

# Create a list of points
# for i in range(num_turns):
#     x = i
#     y = points_per_turn * i
#     data.append(Point(x, y))
