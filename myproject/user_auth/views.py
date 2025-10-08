from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

#2 
def login_page(request):
    
    if request.user.is_authenticated:
         return redirect('home')

    if request.method == 'POST':
        username_data = request.POST['username']
        password_data = request.POST['password']
        print(username_data, password_data)
        u = authenticate(username = username_data , password = password_data)  #authenticate returns True when correct , wrong credentials = False(None)
        # authenicate class check username, password of user in already available in database , If yes = True , else = False(None) 
        
        if u is not None:
            login(request, u)  #with the help of login we storing login data in session storage
            return redirect('home')
        else :
             return render(request, 'login_page.html', {'wrong_credentials':True})
          

    return render(request, 'login_page.html')


# 1 - do registration part first

def register_page(request):

    if request.method == 'POST':
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
            user_name = request.POST['username']
            password_data = request.POST['password']

            print(first_name, last_name, email, user_name, password_data)

            try:
                username_exist = User.objects.get(username = user_name) 
                return render(request, 'register_page.html', {'username_existed':True})
            except:
                 u = User.objects.create(
                 first_name = first_name,
                 last_name = last_name,
                 email = email,
                 username= user_name,
            )
            u.set_password(password_data)
            u.save()
            return redirect('login_page')
                  

            

    return render(request, 'register_page.html')

def logout_page(request):
     logout(request)  # inbuilt method = erase the data stored(verified credentials) in session storage
     
     return redirect('login_page')

def profile(request):
     
    return render(request, 'profile.html')

def update_profile(request):
     user_record = User.objects.get(username=request.user)

     if request.method == "POST":
          first_name = request.POST['firstname']
          last_name = request.POST['lastname']
          email = request.POST['email']
          user_name = request.POST['username']
          print(first_name, last_name, email, user_name)

          user_record.first_name = first_name
          user_record.last_name = last_name
          user_record.email= email
          user_record.username = user_name
          user_record.save()
          return redirect('profile')

     
     return render(request, 'update_profile.html',{'user_record':user_record})


def change_password(request):
     
     if request.method == 'POST':
        try:
             old_password = request.POST['old_password']
             u= authenticate(username= request.user.username, password =old_password)
             if u is not None:
                  return render(request,'change_password.html',{'new_pass':True})
             else:
                  return render(request,'change_password.html',{'wrong_old_pass':True})
             
        except:
             new_password=request.POST['new_password']
             user_record=User.objects.get(username=request.user)
             user_record.set_password(new_password)
             user_record.save()
             return redirect('login_page')
                                  
     
     return render(request, 'change_password.html')