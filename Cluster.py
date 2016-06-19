import numpy as np



class Cluster():
    
    def __init__(self, cluster_size):
        self.center(0,0)
        self.list_x = np.zeros((0))
        self.list_y = np.zeros((0))
        self.list_xy = np.zeros((0,2))
        self.list_final_x = np.zeros((0))
        self.list_final_y = np.zeros((0))
        self.list_final_xy = np.zeros((0,2))
    
    def center(self, x, y):
        self.x = x
        self.y = y
        
        
    def return_center_point(self):
        center = np.zeros((1,2))
        center[:,0] = int(self.x)
        center[:,1] =  int(self.y)
        return self.x, self.y, center
        
            
    def print_center(self):
        print("x:", self.x, "y: ",self.y )
        
        
        
    def find_distance(self, xx, yy):
        distance = (np.sqrt((xx - self.x)**2 + (yy - self.y)**2))**2
        return distance
    
    def insert_xy(self, x, y):
        #self.list_x = []
        #self.list_y = []
        self.list_x = np.append(self.list_x, x) 
        self.list_y = np.append(self.list_y, y) 
        
        #self.all_point_list(self.list_x, self.list_y)
        return None
 
 
     
    def all_point_list(self, list_x, list_y):
        #self.list_xy   = np.zeros((3, 2))
        self.list_xy[:,0]= self.list_x
        self.list_xy[:,1]= self.list_y
        return self.list_xy
        

    
    def insert_xxyy(self, data_point):
        self.list_xy = np.append(self.list_xy, data_point)
        
        print("list printing ", self.list_xy)
        return None
  
 
 
 
        
    def print_points(self):
        for i in range(len(self.list_xy)):
            print(self.list_xy[i])    
        
        return None
    
    
    
    def clear_all_list(self):
        #for i in range(len(self.list_x)):
        #    self.list_x[i] = 0
        #    self.list_y[i] = 0
        #    self.list_xy[i] = 0
        #print(len(self.list_x))
        self.list_x = np.zeros((0))
        self.list_y = np.zeros((0))
        self.list_xy = np.zeros((0,2))
        
        
        return None
    
    
    
    def final_list(self, list_xy, list_x, list_y):
        #for i in range(len(self.list_x)):
        #    self.list_final_x[i] = 0
        #    self.list_final_y[i] = 0
        #    self.list_final_xy[i] = 0
        
        
        self.list_final_x = np.zeros((0))
        self.list_final_y = np.zeros((0))
        self.list_final_xy = np.zeros((0,2))
        
        
        self.list_final_x = list_x
        self.list_final_y = list_y
        self.list_final_xy = list_xy
        #print("points", list_xy)
        
        return None
    
    
    
    def insert_to_final_list(self, x , y ):
        
        self.list_final_x = np.append(self.list_final_x, x) 
        self.list_final_y = np.append(self.list_final_y, y) 
        
        #self.all_point_list(self.list_x, self.list_y)
        return None
 
    
    
    
    def return_final_point_list(self):
        return self.list_final_x, self.list_final_y, self.list_final_xy

    
    
    def print_size(self):
        print(len(self.list_final_x))    
        
        return None


    def return_cluster_size(self):
        
        return len(self.list_final_x)   
 
 
     
    def recalculate_center(self):
        
        #list_copy_xy = self.list_xy
        #print(list_copy_xy)
        #list_copy_xy = np.asarray(list_copy_xy)
        #print(list_xxyy)
        list_xxx = self.list_x
        #print(list_xxx)
        list_yyy = self.list_y
        #print(list_yyy)
        list_copy_final = np.zeros((len(list_xxx), 2))
        list_copy_final[:,0] = list_xxx
        list_copy_final[:,1] = list_yyy
        sum_x = sum(list_xxx)
        #print("sum_x", sum_x)
        ssize = len(list_xxx)
        #print("size", size)
        new_x = int(((1/ssize))*(sum_x))
        #print("new_x", new_x)
        sum_y = sum(list_yyy)
        new_y = int(((1/ssize))*(sum_y))
        
        self.center(new_x, new_y)
        self.final_list(list_copy_final, list_xxx, list_yyy)
        self.clear_all_list()
        return None

    
    
    def t_distance(self):
        total_dist = 0
        for i in range(len(self.list_final_x)):
            s = (np.sqrt((self.list_final_x[i] - self.x)**2 + (self.list_final_y[i] - self.y)**2))**2
            total_dist = total_dist + s
            
        return total_dist    
    
    
    
    def find_distant_points(self, c_size):
        distant_pt = np.zeros((len(self.list_final_x)))
        
        z = len(self.list_final_x) - c_size
        #print("difference", z)
        list_extra_x = np.zeros((z))
        list_extra_y = np.zeros((z))
        list_new_final_x = np.zeros((c_size))
        list_new_final_y = np.zeros((c_size))
        list_new_final_xy = np.zeros((c_size, 2))
        
        for i in range (len(self.list_final_x)):
            distant_pt[i] = (np.sqrt((self.list_final_x[i] - self.x)**2 + (self.list_final_y[i] - self.y)**2))**2
            
        sorted_index = np.argsort(distant_pt)
        #print("sorted", sorted_index) 
            
        for j in range (z):
            list_extra_x[j] = self.list_final_x[sorted_index[len(sorted_index) - 1 - j]]
            list_extra_y[j] = self.list_final_y[sorted_index[len(sorted_index) - 1 - j]]
        
        #print("list_ex", list_extra_x)            
            
        for j in range (c_size):
            list_new_final_x[j] = self.list_final_x[sorted_index[j]]
            list_new_final_y[j] = self.list_final_y[sorted_index[j]]
         
        #print("old list", self.list_final_x)    
        #print("new_final", list_new_final_x)    
            
        list_new_final_xy[:,0] = list_new_final_x
        list_new_final_xy[:,1] = list_new_final_y
        
        
        self.final_list(list_new_final_xy, list_new_final_x, list_new_final_y)
        
        return list_extra_x, list_extra_y
        
        
    def number_of_extra_points(self, c_size):
        z = len(self.list_final_x) - c_size
        
        return z, self.list_final_x, self.list_final_y
    
    
    
    def exists(self, x, y ):
        yess = 0
        #print("self.list_final_x", self.list_final_x)
        #print("self.list_final_y", self.list_final_y)
            
        
        
        for i in range(len(self.list_final_x)):
            if((self.list_final_x[i] == x) and (self.list_final_y[i] == y)):
                yess = 1
                break
                #print("yess: ", yess)
        
        #if(yess == 0):
        #    print("already used")        

        return yess
    
    
    def delete_point(self, x, y):
        
        #print("SUCCESS--------------------------------")
        #print("old length", len(self.list_final_x))
        
        copy_x = self.list_final_x
        copy_y = self.list_final_y
        #print("len of copy:" , len(copy_x))
        #print("x", x, " : y", y )
        
        #print(self.list_final_x)
        #print(self.list_final_y)
        
        for i in range(len(copy_x)):
            
            #print(copy_x[i], " : ", copy_y[i] )
            #print("len of copy:" , len(copy_x))
            
            if(copy_x[i] == x):
                if(copy_y[i] == y):
                    copy_x = np.delete(copy_x, i)
                    copy_y = np.delete(copy_y, i)
                    break
        
        self.final_list(self.list_final_xy, copy_x, copy_y)
        #            break
        
        #print("New length", len(self.list_final_x))
                       
        return None
        
        
        
        
        