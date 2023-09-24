# Slicing = create a substring by extracting elements from another string 
#   indexing[] or slice()
#   [start:stop:step]
# By default, start = 0,stop = -1 and step = 1

name = "Endian Ness"

first_name = name[:3]      # Stop value is not included
                            
last_name = name[4:]       

print(first_name)
print(last_name)

# Providing step value
fname = name[ : : 2]
print(fname)

# Reversing string
reversed_name = name[-1 :  : -1]        # or use name[ : : -1]
print(reversed_name)

# Slice func
website = "http://google.com"

# Create slice obj
slice = slice(7,-4,)     #Values separated by commas instead of colon(:)

# Apply slice obj
print(website[slice]) 

website1 = "http://wikipedia.com"
print(website1[slice]) 