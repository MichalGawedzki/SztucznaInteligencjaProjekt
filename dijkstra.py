
def Dijkstra(s, n, A, dist, pred):


    #brakuje zapisu do tablicy
    fin=[]



    inf=100
		
	#uzupe³nienie tablic
    for v in range(0, n):
        dist[v]=inf
        fin[v]=False
        pred[v]=-1

    dist[s]=0
    fin[s]=True
    minimal=s

    #petla wykonuje sie n-1 razy
    for i in range(0,n):
        for j in range(0,n):
            if A[minimal][j]< inf and fin[j]==False:
                if dist[minimal]+A[minimal][j]<dist[j]:
                    dist[j]=dist[minimal]+A[minimal][j]
                    pred[j]=minimal+1

        min_distance=inf
        min_verex=0
        for k in range(0,n):
            if fin[k]==False and dist[k]<min_distance:
                min_verex=k  
                min_distance=dist[k]

        if min_distance<inf:
            fin[min_verex]=True
            minimal=min_verex
    