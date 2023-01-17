import streamlit as st
import random


#Spin the wheel game
st.set_page_config(page_title="Spin the wheel", layout="wide")
st.markdown("<h1 style='text-align: center; color: red;'>Spin the wheel</h1>", unsafe_allow_html=True)

rules, game = st.columns(2)

with rules:
    st.markdown("<h2 style='text-align: center; color: blue;'>Rules</h2>", unsafe_allow_html=True)
    #rule 1: Choose a number between 1 and 100 (inclusive)
    st.markdown("<h4 style='text-align: center; color: black;'>1. Choose a number between 1 and 100 (inclusive)</h4>", unsafe_allow_html=True)
    #rule 2: Spin the wheel
    st.markdown("<h4 style='text-align: center; color: black;'>2. Spin the wheel</h4>", unsafe_allow_html=True)
    #rule 3: If the number is exactly the same as the number you chose, you double your money
    st.markdown("<h4 style='text-align: center; color: black;'>3. If the number is exactly the same as the number you chose, you double your money</h4>", unsafe_allow_html=True)
    #rule 4: If the number is prime, you keep your money
    st.markdown("<h4 style='text-align: center; color: black;'>4. If the number is prime, you keep your money</h4>", unsafe_allow_html=True)
    #rule 5: For any other number, you lose your money
    st.markdown("<h4 style='text-align: center; color: black;'>5. For any other number, you lose your money</h4>", unsafe_allow_html=True)

with game:
    #generate a random number between 1 and 100 (inclusive)
    #ask the user to choose a number between 1 and 100 (inclusive) with number input store it session state
    bet = st.number_input("Choose a bet value", min_value=1, max_value=1000, value=1, step=1, key='bet')
    
    #now ask for a number, generate a random number between 1 and 100 (inclusive), and compare the two numbers as long as bet > 0
    prime_set = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    if bet > 0:
        number = st.number_input("Choose a number between 1 and 100 (inclusive)", min_value=1, max_value=100, value=1, step=1, key='number')
        if st.button("Spin the wheel"):
            random_number = random.randint(1, 100)
            if number == random_number:
                st.markdown("<h3 style='text-align: center; color: green;'>You won! You doubled your money!</h3>", unsafe_allow_html=True)
                bet = bet * 2
            elif random_number in prime_set == 0:
                st.markdown("<h3 style='text-align: center; color: blue;'>You won! You keep your money!</h3>", unsafe_allow_html=True)
            else:
                st.markdown("<h3 style='text-align: center; color: red;'>You lost! You lost your money!</h3>", unsafe_allow_html=True)
                bet = 0

    #print the balance
    st.markdown("<h3 style='text-align: center; color: black;'>Your balance is: " + str(bet) + "</h3>", unsafe_allow_html=True)