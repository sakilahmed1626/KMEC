from Cluster import Cluster as CLS
import matplotlib.pyplot as plt
import numpy as np

##### To write output to a file.    #####
#import sys
#sys.stdout=open("500_Nodes_3_MC.txt","w")



# Defines a coluor for each line
#colours = ['#19A3FF', '#FF6AB4', '#19FF19', 'm', 'r'] 

colours = ['#1F45FC', '#57FEFF', '#437C17', '#FBB917', '#E77471', '#FF0000', '#B6B6B4', '#00FF00', '#FF00FF', '#3BB9FF', '#82CAFA' ] 
# Defines a marker for each line
markers = ['o', 'v', '*', 'D', '^','3', 'd' 'x']


total_data_points = 500
number_of_cluster = 5
cluster_size = int(total_data_points/number_of_cluster)

x_axis_begin = 0
x_axis_end = 200
y_axis_begin = 0
y_axis_end = 200



C = []

for i in range (number_of_cluster): 
    C.append(CLS(cluster_size))




def uniform_data_point(N):
#random data points
    
    xx = np.random.randint(x_axis_begin, x_axis_end, size = N)
    yy = np.random.randint(y_axis_begin, y_axis_end, size = N)

    list_of_xy_uniform= np.zeros((N,2))
    list_of_xy_uniform[:,1]= xx
    list_of_xy_uniform[:,0] = yy

    np.savetxt("data_point.csv", list_of_xy_uniform, delimiter=",")

    print(list_of_xy_uniform)    
    return xx, yy, list_of_xy_uniform




def data_point_from_file():
#random data points

    list_of_xy_uniform = np.loadtxt("data_point.csv" , delimiter=",") 
    
    xx = list_of_xy_uniform[:,1]
    yy = list_of_xy_uniform[:,0]

    print(list_of_xy_uniform)    
    return xx, yy, list_of_xy_uniform



def kmeanplusplus(data, limitt):
    
    dist_pt = np.zeros((limitt))
    dist = []
    probability_dist = []
    
    for i in range(len(data_xx)):
        for m in range (limitt):
            #print("M: ", m, "dist: ", C[m].find_distance(data_xx[i], data_yy[i]))
            dist_pt[m] = C[m].find_distance(data_xx[i], data_yy[i])
           
        n = np.argmin(dist_pt)
        #print("n", n)
        dist.append(dist_pt[n])
   
    
    #print("Number of Points", len(dist))
        
    sum_d = sum(dist)            
                
    for j in range(len(data)):
        probability_dist.append(dist[j]/sum_d) 

   
    max_point_index = np.argmax(probability_dist, axis=0)


    return max_point_index


#Initiate data points and scatter plot of data points
data_xx, data_yy, data = uniform_data_point(total_data_points)

#Initiate data points from saved file. 
#data_xx, data_yy, data = data_point_from_file()


sct_data_points = plt.scatter(data_xx, data_yy, s= 25, c = '#A4C3C3', marker = 'o')
plt.axis('off') 
plt.show()
sct_data_points.remove()

#Initiate Centers for each cluster.

c_x0 = np.random.randint(0,100,1)
c_y0 = np.random.randint(0,100,1)
    
C[0].center(c_x0, c_y0)

for j in range(number_of_cluster):
    if(j > 0):
        k = kmeanplusplus(data, j)
        C[j].center(data_xx[k], data_yy[k]) 
    else:
        print()




def recalculate_center():
    
    for i in range(number_of_cluster):
        C[i].recalculate_center()
    return None




def assign_point(x, y, data, number_of_cluster ):
    
    distanceKeeper = np.zeros((number_of_cluster))
    
    for i in range(number_of_cluster):
        distanceKeeper[i] = C[i].find_distance(x,y)
        #print(distanceKeeper[i])
        
    j = np.argmin(distanceKeeper)
    #print("data", data)
    C[j].insert_xy(x, y)
        
    return None

final_list_x = [0]
final_list_y = []

def see_the_plot():

    
    for i in range(number_of_cluster):
        x, y, center = C[i].return_center_point()
        list_x, list_y, list_xy = C[i].return_final_point_list() 
        plt.scatter(list_x, list_y, s= 200, c = colours[i], marker = markers[i])
        #plt.scatter(x, y, s= 60, c = colours[i], marker = 's')
        final_list_x.append(list_x)
        final_list_y.append(list_y)
    
        update_final_x= []
        update_final_x.append(list_x)
        update_final_y= []
        update_final_y.append(list_y)
        print("cluster: ", i , " x :" , update_final_x )
        print("cluster: ", i , " y :" , update_final_y )
    
    #print("x coordinates: \n")
    #print(update_final_x)
    
    #print("y coordinates \n")
    #print(update_final_x)
            
    
    plt.axis([x_axis_begin, x_axis_end, y_axis_begin, y_axis_end]) 
    plt.show()
        
    return None




count = np.zeros((4))
mm = 0


for k in range(30):
    for i in range(total_data_points):
        assign_point(data_xx[i], data_yy[i], data[i],  number_of_cluster)
    
    see_the_plot()
    
    for j in range(number_of_cluster):
        C[j].recalculate_center()
        C[j].print_size() 
        #C[j].print_center()
    
    print("\n")    

    x_1, y_1, center = C[0].return_center_point()
    sum_x_y = x_1 + y_1
    #print("sum_x_y", sum_x_y)
    count[mm] = sum_x_y 
    #print("count[mm]", count[mm], "mm", mm)
    mm = mm + 1
    if(mm == 4):
        mm = 0
    
    if(count[2] == count[3] ):
        if(count[2] == count[1] ):
            if(count[0] == count[1] ):
                print("STOP at ", k)
                break




def total_distance():
    tdistance = 0
    for i in range(number_of_cluster):
        ss = C[i].t_distance()
        tdistance = tdistance + ss
    #print("Total Distance: ", tdistance)    
    return tdistance

d1 = total_distance()


def assign_extra_points(extra_points, list_ex, list_ey, cluster_index ):
    
    o = cluster_index 
    #print("TURN=======================", o)
    m = 0
    #print("list_x", list_ex)
    #print("list_y", list_ey)
    re_cluster = number_of_cluster-1
    size_dist_e = re_cluster*len(list_ex)
    dist_e = np.zeros(( size_dist_e ))
    diff_e = np.zeros(( size_dist_e ))
    
    
    for i in range(len(list_ex)):
        dist_a = C[o].find_distance(list_ex[i], list_ey[i])
        
        
        for j in range(number_of_cluster):
            dist_b = C[j].find_distance(list_ex[i], list_ey[i])
            if((dist_a - dist_b) != 0):
                diff_e[m] = abs(dist_a - dist_b)
                dist_e[m] = dist_b
                m = m+1
                #print(dist_e[j])
        
        sortt = np.argsort(diff_e)
        
        #print("dist_a", dist_a)
    #print("dist_e", dist_e)
    #print("sortt", sortt)
    #print("diff", diff_e)    
    #print("list_ex:", list_ex)
    #print("list_ey:", list_ey)
    
        
    for i in range(len(dist_e)):
        #print("loop: ", i)
        
        if(C[o].return_cluster_size() == cluster_size):
            break
        
        z = np.floor(sortt[i]/re_cluster)
        #print("z flooring", z)
        
        
        
        for k in range(number_of_cluster):
            dist_c = C[k].find_distance(list_ex[z], list_ey[z])
            #print("dist_c_x", list_ex[z])
            #print("dist_c", dist_c)
            #print("need to match", dist_e[sortt[i]])
            
            
            
            if(dist_c == dist_e[sortt[i]]):
                #print("incoming cluster:", k)
                break
            
        
        #print(list_ex[z]," ",  list_ey[z])
        
        if(C[o].exists(list_ex[z], list_ey[z]) == 1):    
            if((C[k].return_cluster_size() < cluster_size) and (C[o].return_cluster_size() > cluster_size)  ):
                C[k].insert_to_final_list(list_ex[z], list_ey[z])
                C[o].delete_point(list_ex[z], list_ey[z])
                #print("entered in ", sortt[k])
                #break        

    #for k in range(len(list_ex)):    
        #print("original distance", C[o].find_distance(list_ex[k], list_ey[k]))
    return None    




for i in range(number_of_cluster):
    if(C[i].return_cluster_size() > cluster_size):
        #print("Cluster: ", i+1)
        #list_extra_points_x, list_extra_points_y = C[i].find_distant_points(cluster_size)
        extra_points, list_ex, list_ey = C[i].number_of_extra_points(cluster_size)
        assign_extra_points(extra_points, list_ex, list_ey, i)
        
        for i in range(number_of_cluster):
            s = C[i].return_cluster_size()
        #   print("Cluster: ", i , "Size: ", s)
        #print("\n")
        
        
        
        
        
        
for i in range(number_of_cluster):
    s = C[i].return_cluster_size()
    print("Cluster: ", i , "Size: ", s)


print("K-means objective function value: ", d1)
d2 = total_distance()
print("KMEC value: ", d2)

differece_old_new = np.abs(d1-d2)
print("differene Kmean vs kmean mod: ", differece_old_new)


see_the_plot()


p_increase = ((d2-d1)/d1)*100
print("Percent Increase: ", p_increase)        