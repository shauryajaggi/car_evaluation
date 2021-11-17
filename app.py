import pickle
import streamlit as st
 
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
def prediction(Buying, Maintainance, Doors, Persons, Lug_boot, Safety):   
 
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Buying, Maintainance, Doors, Persons, Lug_boot, Safety]])
     
    if prediction == 0:
        pred = 'Very Bad'
    elif prediction == 1:
        pred = 'Bad'
    elif prediction == 2:
        pred = 'Good'
    else:
        pred = "Very Good"
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Car Evaulation ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Buying = st.selectbox('Buying',("0","1","2","3"))
    Maintainance = st.selectbox('Maintainance',("0","1","2","3")) 
    Doors = st.selectbox('Doors',("0","1","2","3"))
    Persons = st.selectbox('Persons',("0","1","2","3"))
    Lug_boot = st.selectbox('Lug_Boot',("0","1","2"))
    Safety = st.selectbox('Safety',("0","1","2"))

    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Buying, Maintainance, Doors, Persons, Lug_boot, Safety) 
        st.success('Your Car Condition is {}'.format(result))
     
if __name__=='__main__': 
    main()