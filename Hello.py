import streamlit as st
import streamlit-survey as ss
import pandas as pd
import numpy as np
import plotly.express as px

def generate_survey():
    survey = ss.StreamlitSurvey()
    for i in range(1, 11):
        question = f"Question {i}"
        options = list(range(1, 11))
        survey.radio(question, options)
    return survey

def generate_responses():
    responses = []
    for i in range(30):
        response = np.random.randint(1, 11, size=10)
        responses.append(response)
    return pd.DataFrame(responses)

def visualize_results(responses):
    fig1 = px.pie(responses.mean(), values=responses.mean(), names=responses.columns,
                  title="Average Response per Question")
    fig2 = px.scatter_geo(responses.reset_index(), locations="state", color="state",
                           hover_name="index", size="index",
                           projection="albers usa", title="Responses by State")
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)

def main():
    st.set_page_config(page_title="Survey", page_icon=":pencil2:")
    st.title("Survey")
    st.write("Please answer the following questions:")
    survey = generate_survey()
    if survey.submit_button():
        responses = generate_responses()
        visualize_results(responses)
        st.write("Thank you for your response!")
        st.write("Here are the results:")
        st.dataframe(responses)

if __name__ == "__main__":
    main()
