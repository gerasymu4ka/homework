##solver(data) ->
##[
## [9, 1, 3, 7, 4, 6, 8, 5, 2],
## [8, 6, 2, 5, 1, 3, 4, 9, 7],
## [5, 4, 7, 2, 9, 8, 3, 6, 1],
## [6, 8, 1, 3, 7, 9, 5, 2, 4],
## [2, 9, 5, 4, 6, 1, 7, 3, 8],
## [3, 7, 4, 8, 2, 5, 6, 1, 9],
## [4, 2, 9, 6, 5, 7, 1, 8, 3],
## [7, 5, 8, 1, 3, 2, 9, 4, 6],
## [1, 3, 6, 9, 8, 4, 2, 7, 5]
##]

data = [
[9, 0, 0, 7, 0, 0, 8, 0, 0],
[0, 6, 0, 5, 1, 0, 0, 0, 0],
[0, 0, 7, 2, 0, 0, 0, 0, 0],
[0, 0, 1, 3, 0, 0, 0, 2, 4],
[2, 0, 0, 4, 0, 1, 0, 0, 8],
[3, 7, 0, 0, 0, 5, 6, 0, 0],
[0, 0, 0, 0, 0, 7, 1, 0, 0],
[0, 0, 0, 0, 3, 2, 0, 4, 0],
[0, 0, 6, 0, 0, 4, 0, 0, 5]
]
def rmnl(data):
    fd = []
    for x, line in enumerate(data):
        for y, cell in enumerate(line):

            if cell == 0:
                for i in range(1, 10):   
                    cell = i
                    
                    #nextcell = line[(y+1)%len(line)]
                    if cell in line:
                        cell = 0     

            print L
        
                        
        line[y] = cell
        
        print line        
        fd.append(line)
        
    print fd
            
                    
            
    

##    for el in data:
##        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
##        for e in el:
##            if e in lst:
##                e = e
##                lst.remove(e)
##                print e
##               
##            if e == 0:
##                e = lst[0]
##                lst.remove(e)
##               
##                if e in el:
##                    e = 0
##                print e
##           
##            print el


#def rm_num_col(data):

#def rm_num_sqrt(data):
