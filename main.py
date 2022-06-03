import requests
from requests import get
from bs4 import BeautifulSoup
import pandas
import itertools
import streamlit as st
import random





st.title('Real Estate Analyzer')

def getFloatInput(sPrompt):
  fValue = -1
  
  while fValue < 0:
    try:
      fValue = float(input(sPrompt))
# Check to see if the input is greater than 0               
      if fValue < 0:
        st.write("Input must be greater than 0: ")
        continue
# Check to see if the input is a numeric value        
    except ValueError:
            st.write ("Input must be a numeric value: ")
            continue
  return fValue
  
# Asks user for another property price after entering property price
def main():
    propertyPrices =[]
    fValue= st.number_input("Enter property price: ")
    propertyPrices.append(fValue)

    downPayment= st.number_input("Enter down payment (as decimal):")  
    rentPayment= st.number_input("Enter rent:") 
               
    iElement = 0
    st.write("Property", iElement+1,':', "$", "{:,.2f}".format(propertyPrices[iElement]))
    iElement += 1
#Downpayment/price to rent ratio/Commisson/Annual gross rental income calculations
    AGRI= rentPayment * 12
    rp= fValue / float((rentPayment * 12))
    dp= fValue * downPayment 
    commission = (fValue) * .05
# Print each entry element on its own line    
    st.write(f"Rent:", "$", "{:,.2f}".format(rentPayment))
    st.write(f"Down Payment:", "$", "{:,.2f}".format(dp))
    st.write(f"Price to rent ratio:", round((rp)))
    st.write(f"Annual Gross Rental Income:", "$", "{:,.2f}".format((AGRI)))
    st.write(f"Commission (5%):", "$", "{:,.2f}".format(round(commission , 2)))   
main()

