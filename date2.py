# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 12:04:29 2018
@author: OpenSource
"""
import datetime as dt
text=[]
answer=[]
sentence="two days after today in bangalore and three days after yesterday  in delhi"

mainlist=sentence.split();


##identifying normal date form and converting it to standard form
fmts = ('%d-%m-%Y','%d:%m:%Y','%d/%m/%Y','%d-%B-%Y','%d:%B:%Y','%d/%B/%Y')
parsed=[]

for e in mainlist:
    for fmt in fmts:
        try:
           t = dt.datetime.strptime(e, fmt)
           parsed.append((e, fmt, t)) 
           break
        except ValueError as err:
           pass
   

for t in parsed:
    answer.append(('{}'.format(*t)).replace(":","-") )
 ##===================================================================

list_1=['today','tomorrow','yesterday','this','last','previous','next','upcoming']  
list_2=['after','before']
list_3=['last','this','next']
list_4=list(range(1, 32))
list_5=['1st','2nd','3rd']
for i in list_4[3:]:
    list_5.append(str(i)+'th')

list_6=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen', 'fourteen',
          'fifteen','sixteen','seventeen', 'eighteen','nineteen', 'twenty']
for i in range (9):
    list_6.append('twenty'+list_6[i])
    
list_6.append('thirty')
list_6.append('thirtyone')

list_7=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
list_8=['month','year']
list_9 =['delhi', 'meeting', 'client meeting' , 'bangalore' , 'flight']

for i in mainlist:
    for j in list_1:
        if(i==j):
            if(i=="today"):
                temp_var=dt.date.today()
                for k in list_2:
                    if(k==mainlist[mainlist.index(i)-1]):
                        if(k=='after'):
                            if(mainlist[mainlist.index(i)-2]=='day'):
                                temp_var=dt.date.today()+dt.timedelta(1)
                                answer.append(temp_var.strftime('%d-%B-%Y'))
                                break
                            elif(mainlist[mainlist.index(i)-2]=='days'):
                                for l in list_4:
                                    if(str(l)==mainlist[mainlist.index(i)-3]):
                                        temp_var=dt.date.today()+dt.timedelta(l)
                                        answer.append(temp_var.strftime('%d-%B-%Y'))
                                        break
                           
                                for m in list_6:
                                    if(m==mainlist[mainlist.index(i)-3]):
                                        temp_var=dt.date.today()+dt.timedelta(list_6.index(m)+1)
                                        answer.append(temp_var.strftime('%d-%B-%Y'))
                                        break
         
                                        
                        
                                        
                                        
                        elif(k=='before'):
                            if(mainlist[mainlist.index(i)-2]=='day'):
                                temp_var=dt.date.today()-dt.timedelta(1)
                                answer.append(temp_var.strftime('%d-%B-%Y'))
                                break
                                
                                
                                
                            elif(mainlist[mainlist.index(i)-2]=='days'):
                                for l in list_4:
                                    if(str(l)==mainlist[mainlist.index(i)-3]):
                                        temp_var=dt.date.today()-dt.timedelta(l)
                                        answer.append(temp_var.strftime('%d-%B-%Y'))
                                        break
                                        
                                for m in list_6:
                                    if(m==mainlist[mainlist.index(i)-3]):
                                        temp_var=dt.date.today()-dt.timedelta(list_6.index(m)+1)
                                        answer.append(temp_var.strftime('%d-%B-%Y'))
                                        break
                                    
                for r in list_9:
                    for a in range(2):
                        if((mainlist.index(i)+a+1)<len(mainlist)):
                            if(r==mainlist[mainlist.index(i)+a+1]):
                                answer.append(r)         
                text.append(mainlist.index(i))
                break                       
                                
                            
                    
                        
                
            elif (i=="yesterday"):
                temp_var=dt.date.today()-dt.timedelta(1)
                for k in list_2:
                    if(k==mainlist[mainlist.index(i)-1]):
                        if(k=='after'):
                            if(mainlist[mainlist.index(i)-2]=='day'):
                                temp_var=temp_var+dt.timedelta(1)
                                answer.append(temp_var.strftime('%d-%B-%Y'))
                                break
                            elif(mainlist[mainlist.index(i)-2]=='days'):
                                for l in list_4:
                                    if(str(l)==mainlist[mainlist.index(i)-3]):
                                        temp_var=temp_var+dt.timedelta(l)
                                        answer.append(temp_var.strftime('%d-%B-%Y'))
                                        break
                           
                                for m in list_6:
                                    if(m==mainlist[mainlist.index(i)-3]):
                                        temp_var=temp_var+dt.timedelta(list_6.index(m)+1)
                                        answer.append(temp_var.strftime('%d-%B-%Y'))
                                        break
                                        
                        
                                        
                                        
                        elif(k=='before'):
                            if(mainlist[mainlist.index(i)-2]=='day'):
                                temp_var=temp_var-dt.timedelta(1)
                                answer.append(temp_var.strftime('%d-%m-%Y'))
                                break
                                
                                
                                
                            elif(mainlist[mainlist.index(i)-2]=='days'):
                                for l in list_4:
                                    if(str(l)==mainlist[mainlist.index(i)-3]):
                                        temp_var=temp_var-dt.timedelta(l)
                                        answer.append(temp_var.strftime('%d-%m-%Y'))
                                        break
                                        
                                for m in list_6:
                                    if(m==mainlist[mainlist.index(i)-3]):
                                        temp_var=temp_var-dt.timedelta(list_6.index(m)+1)
                                        answer.append(temp_var.strftime('%d-%m-%Y'))
                                        break
                
                for r in list_9:
                    for a in range(2):
                        if((mainlist.index(i)+a+1)<len(mainlist)):
                            if(r==mainlist[mainlist.index(i)+a+1]):
                                answer.append(r)
                text.append(mainlist.index(i))                
                break 
                
            elif (i=="tomorrow"):
                temp_var=dt.date.today()+dt.timedelta(1)
                for k in list_2:
                    if(k==mainlist[mainlist.index(i)-1]):
                        if(k=='after'):
                            if(mainlist[mainlist.index(i)-2]=='day'):
                                temp_var=temp_var+dt.timedelta(1)
                                answer.append(temp_var.strftime('%d-%m-%Y'))
                                break
                            elif(mainlist[mainlist.index(i)-2]=='days'):
                                for l in list_4:
                                    if(str(l)==mainlist[mainlist.index(i)-3]):
                                        temp_var=temp_var+dt.timedelta(l)
                                        answer.append(temp_var.strftime('%d-%m-%Y'))
                                        break
                           
                                for m in list_6:
                                    if(m==mainlist[mainlist.index(i)-3]):
                                        temp_var=temp_var+dt.timedelta(list_6.index(m)+1)
                                        answer.append(temp_var.strftime('%d-%m-%Y'))
                                        break
                                        
                        
                                        
                                        
                        elif(k=='before'):
                            if(mainlist[mainlist.index(i)-2]=='day'):
                                temp_var=temp_var-dt.timedelta(1)
                                answer.append(temp_var.strftime('%d-%m-%Y'))
                                break
                                
                                
                                
                            elif(mainlist[mainlist.index(i)-2]=='days'):
                                for l in list_4:
                                    if(str(l)==mainlist[mainlist.index(i)-3]):
                                        temp_var=temp_var-dt.timedelta(l)
                                        answer.append(temp_var.strftime('%d-%m-%Y'))
                                        break
                                        
                                for m in list_6:
                                    if(m==mainlist[mainlist.index(i)-3]):
                                        temp_var=temp_var-dt.timedelta(list_6.index(m)+1)
                                        answer.append(temp_var.strftime('%d-%B-%Y'))
                                        break
                
                for r in list_9:
                    for a in range(2):
                        if((mainlist.index(i)+a+1)<len(mainlist)):
                            if(r==mainlist[mainlist.index(i)+a+1]):
                                answer.append(r)
                text.append(mainlist.index(i))
                break 
            
            
            elif(i=='this' ):
                for j in list_8:
                    if(j==mainlist[mainlist.index(i)+1]):
                        if(mainlist[mainlist.index(i)+1]=="year"):
                            temp_var=str(dt.date.today())[:4]
                            if(mainlist[mainlist.index(i)-1]=='of' or mainlist[mainlist.index(i)-1]=='in' or mainlist[mainlist.index(i)-1]=='on'):
                                for k in list_7:
                                    if(mainlist[mainlist.index(i)-2]==k):
                                        temp_var=k+'-'+temp_var
                                        for l in list_5:
                                            if(l==mainlist[mainlist.index(i)-3]):
                                                if(len(str(list_5.index(l)+1))==1):
                                                    temp_var='0'+str(list_5.index(l)+1)+'-'+temp_var
                                                    
                                                else:
                                                    temp_var=str(list_5.index(l)+1)+'-'+temp_var
 
                            for r in list_9:
                                for a in range(2):
                                    if((mainlist.index(i)+a+1)<len(mainlist)):
                                        if(r==mainlist[mainlist.index(i)+a+1]):
                                            answer.append(r)
                            text.append(mainlist.index(i))
                            answer.append(temp_var)                
                            break     
                        
            elif(i=='last'or i=='previous'): 
                
               for j in list_8:
                    if(j==mainlist[mainlist.index(i)+1]):
                        if(mainlist[mainlist.index(i)+1]=="year"):
                            temp_var=str(int(str(dt.date.today())[:4])-1)
                            if(mainlist[mainlist.index(i)-1]=='of' or mainlist[mainlist.index(i)-1]=='in' or mainlist[mainlist.index(i)-1]=='on'):
                                for k in list_7:
                                    if(mainlist[mainlist.index(i)-2]==k):
                                        temp_var=k+'-'+temp_var
                                        for l in list_5:
                                            if(l==mainlist[mainlist.index(i)-3]):
                                                if(len(str(list_5.index(l)+1))==1):
                                                    temp_var='0'+str(list_5.index(l)+1)+'-'+temp_var
                                                    
                                                else:
                                                    temp_var=str(list_5.index(l)+1)+'-'+temp_var
 
                            for r in list_9:
                                for a in range(2):
                                    if((mainlist.index(i)+a+1)<len(mainlist)):
                                        if(r==mainlist[mainlist.index(i)+a+1]):
                                            answer.append(r)
                            text.append(mainlist.index(i))
                            answer.append(temp_var)                
                            break 
#                        elif(mainlist[mainlist.index(i)+1]=="month"):
#                            temp_var=str(int(str(dt.date.today())[5:7]))
                            
                            
                        
            elif(i=='next'or i=='upcoming'):
                for j in list_8:
                    if(j==mainlist[mainlist.index(i)+1]):
                        if(mainlist[mainlist.index(i)+1]=="year"):
                            temp_var=str(int(str(dt.date.today())[:4])+1)
                            if(mainlist[mainlist.index(i)-1]=='of' or mainlist[mainlist.index(i)-1]=='in' or mainlist[mainlist.index(i)-1]=='on'):
                                for k in list_7:
                                    if(mainlist[mainlist.index(i)-2]==k):
                                        temp_var=k+'-'+temp_var
                                        for l in list_5:
                                            if(l==mainlist[mainlist.index(i)-3]):
                                                if(len(str(list_5.index(l)+1))==1):
                                                    temp_var='0'+str(list_5.index(l)+1)+'-'+temp_var
                            
                                                    
                                                    
                                                else:
                                                    temp_var=str(list_5.index(l)+1)+'-'+temp_var
                            
                            
                            for r in list_9:
                                for a in range(2):
                                    if((mainlist.index(i)+a+1)<len(mainlist)):
                                        if(r==mainlist[mainlist.index(i)+a+1]):
                                            answer.append(r)
                            text.append(mainlist.index(i))
                            answer.append(temp_var)                
                            break
    
                            
                            
                
                
            else:   
                break
                #answer.append(temp_var.strftime('%d-%m-%y'))
                                
print(answer)
for i in range (len(answer)):
   for j in range (len(answer)):
       if answer[i]==answer[j] and i!=j:
           print("There is a contradiction on " + answer[i])
                
                
                
                
                
                
                
                
                
                
                