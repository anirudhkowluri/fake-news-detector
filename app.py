# import the libraries
import streamlit as st
import joblib

#Load pre-trained objects (vectorizer and model) from saved .jb files.
vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("model.jb")

# Displays a title at the top of the Streamlit web app interface,write the information.
st.title("Fake News Detector")
st.write("Enter a News Article below to check whether it is Fake or Real. ")

#Creates a multi-line text box labeled "News Article:" where the user can paste or type the news text.
inputn = st.text_area("News Article:","")


if st.button("Check News"):#Adds a button labeled "Check News".
    if inputn.strip():#Checks if the user actually entered some text and removes extra spaces or newlines; if the result is empty, it means the user didn’t type anything meaningful.
        transform_input = vectorizer.transform([inputn])#Converts the user’s entered news text into a numerical vector using the preloaded vectorizer.
        prediction = model.predict(transform_input)#Feeds the transformed vector into the trained ML model to make a prediction.

        # function to Check the model’s output:
        #if the prediction is 1, Streamlit shows a green success message saying “The News is Real!,Otherwise, it shows a red error message saying “The News is Fake!”.
        if prediction[0] == 1:
            st.success("The News is Real! ")
        else:
            st.error("The News is Fake! ")
    else:
        st.warning("Please enter some text to Analyze. ") 