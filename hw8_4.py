import os
initial = "/home/aarirang/Documents"
#output_list = [os.listdir(initial)]
initial_list = os.scandir(initial)

def dive_in(path):
     working = os.scandir(path)
     print(os.listdir(path))
     for x in working:
        if x.dir is True:
            dive_in("path/"x)



            dirlist.append(x.name)
        else:
            filelist.append(x.name)

     #working_tuple.append(dirlist)
     #working_tuple.append(filelist)
     #output_list.append(working_tuple)

     return output_list

#print(dive_in(initial))
print(os.listdir(initial))