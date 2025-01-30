### Advantages of Array Data Structure:
Efficient and Fast Access: Arrays allow direct and efficient access to any element in the collection with constant access time, as the data is stored in contiguous memory locations.

### Memory Efficiency: 
Arrays store elements in contiguous memory, allowing efficient allocation in a single block and reducing memory fragmentation.

### Versatility: 
Arrays can be used to store a wide range of data types, including integers, floating-point numbers, characters, and even complex data structures such as objects and pointers.

### Compatibility with hardware: 
The array data structure is compatible with most hardware architectures, making it a versatile tool for programming in a wide range of environments.

### Disadvantages of Array Data Structure:
### Fixed Size: 
Arrays have a fixed size set at creation. Expanding an array requires creating a new one and copying elements, which is time-consuming and memory-intensive.

### Memory Allocation Issues: 
Allocating large arrays can cause memory exhaustion, leading to crashes, especially on systems with limited resources.

### Insertion and Deletion Challenges: 
Adding or removing elements requires shifting subsequent elements, making these operations inefficient.

### Limited Data Type Support: 
Arrays support only elements of the same type, limiting their use with complex data types.

### Lack of Flexibility:
Fixed size and limited type support make arrays less adaptable than structures like linked lists or trees.


### Array Traversal 
   1. run loop from i=0 to n
   2. print array inside loop

### Array Searching 
1. run loop from i=0 to n
2. check key with run time arr val
3. return i if found otherwise -1

### Array Insertion 
1. either use arr[pos]= key 
2. or user arr.insert(pos,key)
3. Its always update list , return None, so dont hold it in new variable

### Array Deletion 
1. Either use arr.remove(val)
2. or find pos, run loop from pos till n
3. and shift every item to left due to empty deleted position use arr[i] = arr[i+1]

### Time Complexity:

![alt text](image-6.png)