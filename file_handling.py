import os.path
import time

def show_items(a):
    '''
        This Function Is For Displaying Items 
    '''
    if os.path.isfile('items.txt'):
        fin=open('items.txt','r')
        items=eval(fin.read())
        fin.close()
        print('We Are Having --> ')
        choice='y'
        cart=[]
        cart1={}
        while choice=='y':

            if a[2]<10:
                print('Your Wallet Balance Is Low')
                ct=input('Press y to play game and earn money ').lower()
                if ct=='y':
                    import game
                    game.instruction_of_game()
                    score=game.game_algo()*5
                    fin=open('wallet.txt','r')
                    data=eval(fin.read())
                    fin.close()
                    fin=open('wallet.txt','w')
                    data[a[1]]+=score
                    a[2]=data[a[1]]
                    fin.write(str(data))
                    fin.close()
                    log_details=['played_game',a[1],'cash_gained -- '+str(score),time.time()]
                    fin=open('log_of_'+a[1]+'.txt','a')
                    fin.write(str(log_details)+'\n')
                    fin.close()
            for i in items:
                print(str(i)+' ----> '+str(items[i])+'$')
            print('Amount In Your Wallet --> ',a[2])
            print('Items in your cart --> ',len(cart))
            print('Enter name of item to buy or press n to exit store. ')
            char=input().lower()
            if char=='n':
                log_details=['logout',a[1],time.time()]
                fin=open('log_of_'+a[1]+'.txt','a')
                fin.write(str(log_details)+'\n')
                fin.close()
                print('Thanks For Coming')
                return True
            else:
                cart.append(items[char])
                if char not in cart1:
                    cart1[char]=[items[char]]
                else:
                    cart1[char].append(items[char])
                choice=input('Press y to purchase more or n to end shopping ').lower()
                if choice=='n':
                    if a[2]>=sum(cart):
                        print('Your Bill Is --> ',sum(cart))
                        print('Your Amount Left --> ',a[2]-sum(cart))
                        print('Your purchaising is successful','Thanks For Coming',sep='\n')
                        fin=open('wallet.txt','r')
                        d=eval(fin.read())
                        fin.close()
                        log_details=['purchase',a[1],cart1,time.time()]
                        fin=open('log_of_'+a[1]+'.txt','a')
                        fin.write(str(log_details)+'\n')
                        fin.close()
                        fin=open('wallet.txt','w')
                        d[a[1]]=a[2]-sum(cart)
                        fin.write(str(d))
                        fin.close()
                        log_details=['logout',a[1],time.time()]
                        fin=open('log_of_'+a[1]+'.txt','a')
                        
                        fin.write(str(log_details)+'\n')
                        fin.close()
                    else:
                        print('You are not having sufficient balance in your account.')
                        print('Transaction Cancelled...')
                        log_details=['logout_insufficient_balance',a[1],time.time()]
                        fin=open('log_of_'+a[1]+'.txt','a')
                        fin.write(str(log_details)+'\n')
                        fin.close()
                        return True
    else:
        log_details=['logout_server_error',a[1],time.time()]
        fin=open('log_of_'+a[1]+'.txt','a')
        fin.write(str(log_details)+'\n')
        fin.close()
        print('Server Error Quiting...')
        return True

def wallet(user_name):
        '''
            This function returns wallet statement of user
        '''
        if os.path.isfile('wallet.txt'):
            fin=open('wallet.txt','r')
            d=eval(fin.read())
            fin.close()
            if user_name in d:
                return d[user_name]
            else:
                fin=open('wallet.txt','w')
                d[user_name]=40
                fin.write(str(d))
                fin.close()
                print('Congrats!!! You received $40 Bonus')
                return 40
        else:
            d={}
            fin=open('wallet.txt','w')
            d[user_name]=40
            fin.write(str(d))
            fin.close()
            print('Congrats!!! You received $40 Bonus')
            return 40
        
def login_page():
    '''
        this function is for logging in user 
    '''
    user_name=input('Enter Username --> ')
    password=input('Enter Password --> ')
    if os.path.isfile('login_data.txt'):
        fin=open('login_data.txt','r')
        d=eval(fin.read())
        fin.close()
        if user_name in d:
            if d[user_name]==password:
                return (True,user_name)
            else:
                print('Either Username or Password Not Found')
        else:
            print('Either Username or Password Not Found')
    else:
        print('Please create account first')
        return (False,user_name)
    return (False,user_name)    
    
def sign_up_page():
    '''
        this function is for signing up user
    '''
    user_name=input('Enter username --> ')
    password=input('Enter Password --> ')
    if os.path.isfile('login_data.txt'):
        fin=open('login_data.txt','r')
        d=eval(fin.read())
        fin.close()
        if user_name in d:
            print('Sorry, Username Exist.')
            return False
        else:
            d[user_name]=password
            fin=open('login_data.txt','w')
            fin.write(str(d))
            fin.close()
            return (True,user_name)
    else:
        d={}
        d[user_name]=password
        fin=open('login_data.txt','w')
        fin.write(str(d))
        fin.close()
        return (True,user_name)
    
if __name__=='__main__':

    print('          Dummy Merchant        ')
    a=(False,)
    while not a[0]:
        print('Press 1 for sign up or 2 for login or 3 for exit')
        n=int(input())
        if n==1:
            a=list(sign_up_page())
            if a[0]== True:
                log_details=['sign_up',a[1],time.time()]
                fin=open('log_of_'+a[1]+'.txt','a')
                fin.write(str(log_details)+'\n')
                fin.close()
                money=wallet(a[1])
                a.append(money)
                b=show_items(a)
                if b==True:
                    break
        elif n==2:
            a=list(login_page())
            if a[0]== True:
                log_details=['login',a[1],time.time()]
                fin=open('log_of_'+a[1]+'.txt','a')
                fin.write(str(log_details)+'\n')
                fin.close()
                money=wallet(a[1])
                a.append(money)
                b=show_items(a)
                if b==True:
                    break
        else:
            a=(True,)
