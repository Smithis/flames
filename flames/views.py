from django.shortcuts import render
from django.http import request,HttpResponse
from .models import reveal
import random
import string


# Create your views here.

def home(request,pk=''):

    
    
    if request.method=="POST":
        a=request.POST['crush']
        b=request.POST['name']
        i=request.POST['hide']

        if(i==''):
            rand=''.join(random.choices(string.ascii_letters+string.digits,k=5))
        else:
            rand=i


        c=list(a)
        d=list(b)
        print(c)
        count=0
        for i in range(len(c)):
            for j in range(len(d)):
                if(a[i]==b[j]):
                    count=count+1
                    del c[i]
                    del d[j]
                    break

                    
                add=c+d
                h=['f', 'l', 'a', 'm', 'e', 's']
                sum=round((len(add)/(len(h)-1)))
                if(sum==1):
                    k="Friends"
                    break

                elif(sum==2):
                    k="Love"
                    break

                elif(sum==3):
                    k="Affection"
                    break

                elif(sum==4):
                    k="Marriage"
                    break

                elif(sum==5):
                    k="Enemy"
                    break

                elif(sum==6):
                    k="Siblings"
                    break

                else:
                    k="something went wrong"
                    break

    
        
        db=reveal.objects.create(name=a,code=rand,crush=b)
        context={
            'val':k,
            'n':b,
            'c':a,
            'code':rand,
        }
        return render(request,"letter.html",context)
    
    context={
        'ur':pk,
    }
    return render(request,"index.html",context)


def love(request):
    return render(request,"letter.html")


def data(request,pl):
    if(reveal.objects.all().filter(code=pl).exists()):
        il=reveal.objects.filter(code=pl)

    return render(request,"s/index.html",{'user':il})
        
        
    
