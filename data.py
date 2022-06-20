from ast import Return
import string


myDict={
    'name':123,
    'number':100,
    'isMale':False,
    # 'arr':[100,200,300,400,5]
   
}
#[min,max]
mystring=[5,100]
myNumber=[2,10]
datatypein={
    'name':str,
    'number':int,
    'isMale':bool,
}
validationRules=[mystring,myNumber,datatypein]


def eachValueValidiar(x,validationRules):
    ans=True
    if (isinstance(x,bool)):
        pass
    elif(isinstance(x,int)):
        if x>0:
            if len(str(x))> validationRules[1][0] and len(str(x))<validationRules[1][1]:
                pass
                   
            else:
                print('Intiger not in range')
                ans=False
                    
        else:
            print('Number is negative')
               
    elif(isinstance(x,str)):
        if len(x)> validationRules[0][0] and len(x)<validationRules[0][1]:
            pass
               
        else:
            print('String not in range')
            ans= False
            
    return ans 



def myValidatinfunc(myDict,validationRules):
    for x in myDict:
        # print(x)
        y=(validationRules[2].get(x))
        if(isinstance(myDict[x],str)):
       
            x=(myDict[x])
            # print(type(x))
            if(isinstance(x,bool) or isinstance(x,str) or isinstance(x,int)):
                isDict=eachValueValidiar(x,validationRules)
                if (isDict==False):
                    return False
                    break
            elif(isinstance(x,list)):
                for data in x:
                    isDict=eachValueValidiar(data,validationRules)
                    if (isDict==False):
                        return False
                        break
            return True
        
        else:
            return False
            print("Other Data types not supported now")

           
    
    return True
                
            
   
myresponse=[]
myresponse= myValidatinfunc(myDict,validationRules)
print(myresponse)
