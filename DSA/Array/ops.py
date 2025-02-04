# Operations in Array

class ArrayOps:
    def arr_traversal(arr,n):
        for i in range(n):
            print(arr[i],end=' ')
    
    def find_element(arr,n,key):
        for i in range(n):
            if arr[i] == key:
                return i
        return -1

    def arr_insertion(arr,x,pos):
            arr.insert(pos,x)
            return arr
        # arr[pos]=x
        # return arr

 
    
    def arr_remove(key):
          arr.remove(key)
          return arr


arr = [1,2,3,4,5,6,7,8]
n= len(arr)
x=7
pos=5
# arr=ArrayOps.find_element(arr,n,x)

ArrayOps.arr_insertion(arr,x,pos)  
# Return : The insert() method returns None. It only updates the current list.

# arr=ArrayOps.arr_traversal(arr,n)

# arr=ArrayOps.arr_remove(x)

print(arr)