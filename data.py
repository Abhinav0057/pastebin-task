from ast import Return
from itertools import filterfalse
import string


myDict={
    'name':'a',
    'description':'Hi this is a description field and is supposed to be long. This can also be empty sometimes',
    'number':123,
    'isMale':False,
    # 'arr':[100,200,300,400,5]
   
}
#[min,max]
myname=[5,100]
mydescription=[0,1000]
mynumber=[2,5]
isMale=True

datatypein={
    'name':str,
    'description':str,
    'number':int,
    'isMale':bool,
}
validationRules=[myname,mydescription,mynumber,isMale]

def checkInfo(item,itsid):
    data=myDict.get(item)
    if  not isinstance(data,bool):
        print('asdas')
        if len(str(data))<validationRules[itsid][0] or len(str(data))>validationRules[itsid][1]:
            print(" not in range of",item)
            return False
    # if not isinstance(item,datatypein.get(data)):
    #     print("{} is not of desired dataype ",item)
    
    if True:
        typeofdata=datatypein.get(item)
        if not isinstance(data,typeofdata):
            print(' not of desired dataype of ',item)
            return False
    
    



def myValidationfunc(myDict,validationRules):
    for itsid,item  in enumerate(myDict):
        # print(item)
        # print(validationRules[itsid])
        result=checkInfo(item,itsid)
        
    
        if result == False:
            return False
            break
   
        return True


   

myresponse=[]
myresponse= myValidationfunc(myDict,validationRules)
print(myresponse)






# def eachValueValidiar(x,validationRules):
#     ans=True
#     if (isinstance(x,bool)):
#         pass
#     elif(isinstance(x,int)):
#         if x>0:
#             if len(str(x))> validationRules[1][0] and len(str(x))<validationRules[1][1]:
#                 pass
                   
#             else:
#                 print('Intiger not in range')
#                 ans=False
                    
#         else:
#             print('Number is negative')
               
#     elif(isinstance(x,str)):
#         if len(x)> validationRules[0][0] and len(x)<validationRules[0][1]:
#             pass
               
#         else:
#             print('String not in range')
#             ans= False
            
#     return ans 



# def myValidatinfunc(myDict,validationRules):
#     for x in myDict:
#         # print(x)
#         y=(validationRules[2].get(x))
#         if(isinstance(myDict[x],str)):
       
#             x=(myDict[x])
#             # print(type(x))
#             if(isinstance(x,bool) or isinstance(x,str) or isinstance(x,int)):
#                 isDict=eachValueValidiar(x,validationRules)
#                 if (isDict==False):
#                     return False
#                     break
#             elif(isinstance(x,list)):
#                 for data in x:
#                     isDict=eachValueValidiar(data,validationRules)
#                     if (isDict==False):
#                         return False
#                         break
#             return True
        
#         else:
#             return False
#             print("Other Data types not supported now")

           
    
#     return True
                
            
   
