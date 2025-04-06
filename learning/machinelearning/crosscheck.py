prediction=['setosa', 'versicolor', 'versicolor' ,'setosa' ,'virginica' ,'versicolor',
 'virginica', 'setosa' ,'setosa' ,'virginica' ,'versicolor' ,'setosa',
 'virginica', 'versicolor', 'versicolor', 'setosa' ,'versicolor' ,'versicolor',
 'setosa', 'setosa' ,'versicolor', 'versicolor', 'virginica' ,'setosa',
 'virginica' ,'versicolor' ,'setosa' ,'setosa' ,'versicolor' ,'virginica']

y_test=['setosa', 'versicolor' ,'versicolor' ,'setosa' ,'virginica', 'versicolor',
 'virginica', 'setosa', 'setosa' ,'virginica' ,'versicolor' ,'setosa',
 'virginica' ,'versicolor' ,'versicolor' ,'setosa' ,'versicolor' ,'versicolor',
 'setosa', 'setosa', 'versicolor' ,'versicolor', 'versicolor', 'setosa',
 'virginica' ,'versicolor' ,'setosa', 'setosa' ,'versicolor', 'virginica']
l1=[]
for i in range(0,len(prediction)):
   

    if prediction[i]==y_test[i]:
        l1.append(1)
    else:
        l1.append(0)
print(sum(l1),"out of",len(prediction))
print("Accuracy: ",sum(l1)/len(prediction)*100)


