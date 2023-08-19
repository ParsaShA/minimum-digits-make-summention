
def sum_bekhosos(su :int):
      lst = []
      i = 9
      if 0 < su < 10:
              return su
      else:
              while su>0 :
                     for i in range(i,0,-1):
                            su = su-i
                            lst.append(i)
                            if 0<su<9:
                                   lst.append(su)
                                   break
                     return lst
print(sum_bekhosos(35))
       
       
       
       
              
       
       
       
       
       
       
                     
                     
       
       
       
       
       
       
       
       