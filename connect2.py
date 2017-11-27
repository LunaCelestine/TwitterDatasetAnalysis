import time

def findX(x):
    return dSets[x]

def mergeSet(p,q):
    lis=hashSet[q]
    for i in lis:
        dSets[i]=p
        hashSet[p].append(i)
    del hashSet[q]

startTime=time.clock()
n=1000000
dSets =[]
for i in range(0,n):
    dSets.append(i)
hashSet={}
for i in range(0,n):
    hashSet[i]=[i]
edgeSet=[]
fh= open("Graph.txt","r")
for k in fh:
    a,b=k.split(',')
    a=int(a)
    b=int(b)
    #print(a,b)
    c,d=findX(a),findX(b)
    if c!=d:
        #switched q and p assignments
        q=min(c,d)
        p=max(c,d)
        mergeSet(p,q)
endTime=time.clock()


#==============================================================================
# Cluster Analysis
#==============================================================================

clusterSet = {}
for k in hashSet:
    valueList = hashSet[k]
    if(len(valueList) > 1):
        clusterSet[k] = k
        clusterSet[k]= hashSet[k]

clustersSorted = (sorted(clusterSet, key=lambda k: len(clusterSet[k]), reverse=True))
numberOfClusters = len(clustersSorted)
singletons = len(hashSet) - len(clustersSorted)
largestClusters = clustersSorted[:5]

#==============================================================================
# Results
#==============================================================================

print("Number of clusters: ", numberOfClusters)
print("Number of singletons: ", singletons)
print("----------Five Largest Clusters----------")
for setLabel in largestClusters:
    print("Cluster Label: ", setLabel , " Cluster Size:", len(clusterSet[setLabel]))
print('Took %s seconds to calculate.' % (endTime - startTime))
print(findX(825289)==findX(891950))
print(findX(1)==findX(267721))
print(findX(785775)==findX(891950))
print(findX(733252)==findX(891950))
print(findX(250429)==findX(2)) 
#for i in dSets:
    #print(i)
#for k,v in hashSet.items():
    #print(k,v)
fh.close()



    
    
    
    
