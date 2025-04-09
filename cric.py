print("welcome!")
import random
y=random.randint(1,2)
runs=0
runs1=0
runs2=0
runs3=0
runs4=0
runs5=0
u=int(input("enter any number between 1-2: "))
print(y)
if u==y:
    print("u won")
    o=input("choose batting or bowling? ")
    if o=="batting":
        q = list(range(1, 12))
        w=input("select the striker between 1-11: ")
        for i in range(1,121):
            h=random.randint(1,10)
            print("bowl: ",h)
            k=int(input("enter the shot between 1-10: "))
            runs+=k
            if k==h:
                runs-=k
                print("out")
                print("your runs: ",runs)
                f=runs+1
                print("computer need's",f,"to win")
                break
        print("computer's turn")
        y=int(input("select the bowler between 1-11: "))
        for i in range(1,121):
            s=random.randint(1,10)
            print("batting: ",s)
            o=int(input("enter the ball between 1-10: "))
            runs1+=o
            if s==o:
                runs1-=s
                print("out")
                print("computer's run: ",runs1)
                break
            if runs1>runs:
                print("out")
                print("computer's runs are",runs1)
                break
        if runs==runs1:
            print("match tie")
        elif runs>runs1:
            print("you won")
        else:
            print("computer won")
    else:
        p = list(range(1, 12))
        l=input("select the bowler between 1-11: ")
        for h in range(1,121):
            g=random.randint(1,10)
            print("batting: ",g)
            x=int(input("enter the ball between 1-10: "))
            runs2+=g
            if g==x:
                runs2-=g
                print("out")
                print("total runs: ",runs2)
                e=runs2+1
                print("you need",e,"runs to win")
                break
        print("your turn comes")
        f=int(input("select the batsman between 1-11: "))
        for t in range(1,121):
            v=random.randint(1,10)
            print("bowling: ",v)
            r=int(input("enter the shot between 1-10: "))
            runs3+=r
            if v==r:
                runs3-=r
                print("out")
                print("your runs: ",runs3)
                break
            if runs3>runs2:
                print("out")
                print("your runs are",runs2)
                break
        if runs2==runs3:
            print("match tie")
        elif runs2>runs3:
            print("computer won")
        else:
            print("you won")
else:
    print("computer won the toss")
    print("computer chooses to bat first")
    s=int(input("select the bowler between 1-11: "))
    for g in range(1,121):
        z=random.randint(1,11)
        print("batting: ",z)
        d=int(input("enter the ball between 1-10: "))
        runs4+=z
        if z==d:
            runs4-=z
            print("out")
            print("total runs: ",runs4)
            w=runs4+1
            print("you need",w,"to win")
            break
    print("your turn comes")
    f=int(input("select the batsman between 1-11: "))
    for e in range(1,121):
        v=random.randint(1,10)
        print("bowling: ",v)
        r=int(input("enter the shot between 1-10: "))
        runs5+=r
        if v==r:
            runs5-=r
            print("out")
            print("total runs: ",runs5)
            break
        if runs5>runs4:
            print("out")
            print("your runs are",runs5)
            break
    if runs4==runs5:
        print("match tie")
    elif runs4<runs5:
        print("you won")
    else:
        print("computer won")