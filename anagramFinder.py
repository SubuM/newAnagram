import streamlit as st
# import streamlit_authenticator as stauth
from itertools import permutations, combinations
import enchant


def checkAngrm():
    d = enchant.Dict('en_US')
    word = st.text_input('Enter your word:', placeholder='Enter your jumbled word')
    letters = [chr for chr in word]
    repeat_check = []
    resList = []
    word_len = len(word)

    if word_len > 0:
        for number in range(3, len(letters) + 1):  # For Loop
            for current_set in combinations(letters, number):  # Combinations Function
                # Code for the Basic Anagram Finder
                for current in permutations(current_set):
                    current_word = ''.join(current)
                    if d.check(current_word) and current_word not in repeat_check:
                        resList.append(current_word)
                        repeat_check.append(current_word)

    if resList:
        resList.sort()
        for i in range(len(resList)):
            st.write(resList[i])


def pageSettings():
    st.set_page_config(page_title='Anagram Solver', page_icon='random', initial_sidebar_state='auto')
    st.sidebar.image('./images/anagram.png')

    # hide hamburger menu and footer
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden}
                    footer {visibility: hidden}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    checkAngrm()


if __name__ == '__main__':
    pageSettings()
