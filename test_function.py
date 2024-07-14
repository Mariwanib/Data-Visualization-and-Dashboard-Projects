import pandas as pd
from project_function import data_trans

def test_func():
    
    data = pd.DataFrame({'movie_id':[101,102,103,104,105,106,107,108,109,110],
                    'release_date':['1980-8-20','1990-3-27','1987-1-14','1992-11-13','1971-2-21',
                                   '1999-9-19','1985-9-16','2001-6-23','1993-7-19','1960-12-22'],
                    'total_gross':['$44,873','$35,890','$21,839','$40,295','$32,751','$27,184',
                                  '$39,763','$32,091','$26,004','$29,870'],
                    'inflation_adjusted_gross':['$224,487,3','$123,589,0','$632,183,9','$104,029,5','$313,275,1',
                                                '$632,718,4','$473,976,3','$483,209,1','$252,600,4','$422,987,0']})    

    
    assert data_trans(data, 'release_date','total_gross', 'inflation_adjusted_gross').columns.tolist() == ['movie_id', 'release_date','total_gross',
                                                                                                          'inflation_adjusted_gross'], 'Incorrect column names'
    assert data_trans(data, 'release_date','total_gross', 'inflation_adjusted_gross').shape == (10, 4), 'Incorrect shape of dataframe'
    assert data_trans(data, 'release_date','total_gross', 'inflation_adjusted_gross').size == 40 , 'Incorrect size of dataframe'
    assert type(data_trans(data, 'release_date','total_gross', 'inflation_adjusted_gross')) == pd.DataFrame, 'Incorrect dataframe type'

    
    

