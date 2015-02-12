import pickle

with open("test_data.dat", mode = "wb") as testData:
    test = [2,3,5]
    pickle.dump(test,testData)
    
