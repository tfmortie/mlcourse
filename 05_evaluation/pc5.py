# helper functions for PC lab 6
# Jim Clauwaert

import numpy as np
import pandas as pd

def ChopStringVector(strings):
    
    """Chops a vector of strings (equal length) into a matrix of characters, with each row containing a separate 
    string
    
    Parameters
    -----------
    strings : 1-dimensional numpy array
        numpy array containing array of strings 
   
    Returns
    --------
    charMatrix : 2-dimensional numpy array 
        Matrix containing chopped up strings
    """
    
    charMatrix = np.empty([len(strings),len(strings[0])],dtype=np.dtype(str,1))
    strings=np.array(strings)
    for i in range(0,len(strings)):
        charMatrix[i] = [strings[i][u] for u in range(0,len(strings[i]))]

    return charMatrix

def CreateDummyNucleotideFeatures(sequences, length):
    
    """Create dummy dataframe of nucleotides for two regions surrounding 35- and 10-box
    
    Parameters
    -----------
    sequences : 1-dimensional numpy array
        numpy array containing an array of sequences (str)
        
    length : integer
        Length of the DNA sequences
          
    Returns
    --------
    dfDummyDataFrame : Dataframe 
        Dataframe containing dummy features
    """
    
    # Create Position Matrix
    nucleotideMatrix = ChopStringVector(sequences)
    # Convert to Dataframe
    posRangeCol = [str(x) for x in range(length)]
    dfNucleotideMatrix = pd.DataFrame(nucleotideMatrix, columns = posRangeCol)

    # Create dummy Matrix
    dfDummyNucleotideFeatures =  pd.get_dummies(dfNucleotideMatrix)


    return dfDummyNucleotideFeatures
