from fireusairene import fireusairene

import pytest
import pandas as pd


def test_get_all_fire_data():
    
    rst = fireusairene.get_all_fire_data()
    ex = pd.read_pickle('fire_data.csv')
    assert ex.equals(rst), "get all fire data fails"

def test_get_fire_by_po_ra():
   
    rst = fireusairene.get_fire_by_po_ra(-118,35, 10000000)
    ex = pd.read_pickle('llr.csv')
    
    assert rst.equals(ex), "get fire info by position and radium is unsucessful"



def test_get_fire_by_state():
    
    rst = fireusairene.get_fire_by_state('WA')
    ex= pd.read_pickle('st.csv')
    
    assert rst.equals(ex), "get fire info by state is unsucessful"
    

def test_get_freq_by_state():
    
    rst = fireusairene.get_freq_by_state()
    ex = pd.read_pickle('fire_num_state.csv')
    assert ex.equals(rst), "frequecy of fire is not correct, test_get_freq_by_state failed"

