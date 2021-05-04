import streamlit as st
import pickle
from sklearn.tree import DecisionTreeClassifier
model=pickle.load(open("model.pkl","rb"))

def main():
	st.title("Data Mining Term Project")
	html_text="<div><h3>Bank Marketing Analysis</h4></div><div><p>Author: Deepak Prakash Lokande</p></div><div><p>The Final Accuracy Of Decision Tree is:</p></div>"
	st.markdown(html_text,unsafe_allow_html=True)
	# option1 = st.selectbox('Age',('Select','56', '57', '37','40','56'))
	# option2= st.selectbox('Duration',('Select','152', '96', '349','368','183'))
	# option3 = st.selectbox('Campaign',('Select','2', '4', '1','3'))
	# option4 = st.selectbox('Previous',('Select','0', '1'))
	if(st.button("Prediction")):
		result=model.mean()
		st.success(result)
	# Working
	# if(st.button("Prediction")):
	# 	#predict=(model.mean(36.0,152.0,2.0,0.0,1.4,94.465,-41.8,4.961,5228.1,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,1.0,0.0,0))
	# 	#predict=(model.mean(0,152,2,0))
	# 	predict=model.mean()
	# 	st.success(predict)
main()