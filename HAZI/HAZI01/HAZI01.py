
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

def subset(input_list:list,start_index:int,end_index:int)->list:
  out_list=[]
  i = start_index
  while (i<= end_index and i < len(input_list)):
    output_list.append(input_list[i])
    i=i+1
  return out_list

#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

def every_nth(input_list:list, step_size:int)-> list:
  out_list = []
  for i in range( step_size-1, len(input_list), step_size):
    result.append(input_list[i])
  return out_list

#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

def unique(input_list:list)-> bool:
  for i in range(0, len(input_list),1):
    for j in range(len(input_list)-1, -1, -1):
      if j != i:
        if input_list[i]==input_list[j]:
          return False
  return True

#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

def flatten(input_list : list) -> list:
  output=[]
  for sub_list in input_list:
    for x in sub_list:
      output.append(x)
  return output

#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args

def merge_lists(*args) -> list:
    output = []
    for a in args:
     for item in a:
       if item not in output:
          output.append(item)
    return output

#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

def reverse_tuples(input_list : list) -> list:
  output = []
  for _tuple in input_list:
    Temp=[]
    for i in range(len(Temp)-1, -1 ,-1):
      Temp.append(_tuple[i])
    output.append(tuple(Temp))
  return output

#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

def remove_tuplicates(input_list : list) -> list:
    remove=[]
    for i in range(0, len(input_list),1):
      for j in range(len(input_list)-1, -1, -1):
        if j !=i:
          if input_list[i] == input_list[j]:
            if(input_list[i] not in remove):
              remove.append(input_list[i])
    for item in remove:
      input_list.remove(item)
    return input_list

#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

def transpose(input_list : list) -> list:
  output = []
  for i in range(len(input_list)):
    temp=[]
    for j in range(len(input_list[i])):
      temp.append(0)
    output.append(temp)
  for i in range(len(input_list[i])):
    for j in range(len(input_list[i])):
     output[i][j]=input_list[j][i]
  return output

#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

def split_into_chunks(input_list : list,chunk_size : int) -> list:
  output =[]
  i = 0
  while i< len(input_list):
    j=0
    temp = []
    while j < chunk_size and i+j < len(input_list):
      temp.append(input_list[i+j])
      j = j + 1
    i = i + j
    output.append(temp)
    return output

#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

def merge_dicts(*dict) -> dict:
  output={}
  for d in dict:
    output = output | d
  return output

#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

def by_parity(input_list : list) -> dict:
  even = []
  odd = []
  for item in input_list:
    if item & 1:
      odd.append(x)
    else:
      even.append(x)
  return{'even' : even, 'odd' : odd}

#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

def mean_key_value(input_dict: dict) -> dict:
  output = {}
  for key, value in input_dict.items():
    mean = 0
    for item in value:
      mean = mean + item
    output[key] = mean / len(value)
  return output

#If all the functions are created convert this notebook into a .py file and push to your repo