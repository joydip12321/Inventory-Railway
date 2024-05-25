from django.shortcuts import render,redirect
from Invent.models import*
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test,login_required


def is_admin(user):
    return user.is_authenticated and user.is_staff

def Admin_log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request,user)
            
            return redirect('/')
        else:
            messages.success(request, "Invalid username or password")
        return redirect('/')
    return render(request, 'admin_log_in.html')

def Log_in(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/')
        user=authenticate(request,username=username,password=password)
        if user is None :
            messages.error(request, "Invalid Username or Password")
        else:
            login(request,user)
            return redirect('/')
    return render(request, "log_in.html")

@login_required(login_url="/log_in/")
def Log_out(request):
    logout(request)
    return redirect('/log_in/')

def Register_invent(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        if User.objects.filter(email=email).exists():
                messages.info(request, "An account with this email already exists.")
                return redirect('/register_in/')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register_in/')
        
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Accout Created Successfully")
        return redirect('/log_in/')
    return render(request, "register_invent.html")

def Category(request):
    if request.method=="POST":
        data=request.POST
        category_name=data.get('category_name') 
        category_des=data.get('category_des')  
        Cate.objects.create(
            category_name=category_name ,
            category_des= category_des ,

            ) 
        messages.success(request, 'Category added successfully.')
        ProductMessage.objects.create(content="Category added successfully")

        return redirect('/Category/')
    return render(request, "category.html")

def category_list(request):
    queryset = Cate.objects.all()
    context = {'category': queryset}
    return render(request, "category_view.html", context)


def deletebt(request,id):
    
     queryset=Cate.objects.get(id=id)
     queryset.delete()
     messages.success(request, 'Category deleted successfully.')
     ProductMessage.objects.create(content="Category deleted successfully")

     return redirect('/category_list/')

def updatebt(request,id):
    
     queryset=Cate.objects.get(id=id)
     if request.method=="POST":
        data=request.POST
        category_name=data.get('category_name') 
        category_des=data.get('category_des')  
        
        queryset.category_name=category_name 
        queryset.category_des= category_des 
        
        queryset.save()
        messages.success(request, 'Category updated successfully.')
        ProductMessage.objects.create(content="Category updated successfully")

        return redirect('/category_list/')

     context={'category' : queryset}
     return render(request, "category_update.html" , context)
 
def home(request):
    return render(request,'home.html')

def room(request):
    if request.method=="POST":
        data=request.POST
        room_no=data.get('room_no') 
        Room.objects.create(
            room_no=room_no ,
            ) 
        messages.success(request, 'Room addedd successfully.')
        ProductMessage.objects.create(content="Room added successfully")


        return redirect('/room/')
    return render(request,"room.html")

def room_list(request):
    queryset = Room.objects.all()
    context = {'room': queryset}
    return render(request, "room_list.html", context)

def delete_room(request,id):
    
     queryset=Room.objects.get(id=id)
     queryset.delete()
     messages.success(request, 'Room deleted successfully.')
     ProductMessage.objects.create(content="Room deleted successfully")


     return redirect('/room_list/')
 
def update_room(request,id):
    
     queryset=Room.objects.get(id=id)
     if request.method=="POST":
        data=request.POST
        room_no=data.get('room_no') 
        
        queryset.room_no=room_no         
        queryset.save()
        messages.success(request, 'Room updated successfully.')
        ProductMessage.objects.create(content="Room updated successfully")

        return redirect('/room_list/')

     context={'room' : queryset}
     return render(request, "room_update.html" , context)
 
def product(request):
    rooms=Room.objects.all()
    categories=Cate.objects.all()

    if request.method == "POST":
        data = request.POST
        product_name = data.get('product_name')
        product_des = data.get('product_des')
        product_quantity = data.get('product_quantity')
        room_id = data.get('room')  # Use 'room' to get the selected room's primary key
        category_id = data.get('category')  # Use 'category' to get the selected category's primary key

        room_no = Room.objects.get(pk=room_id)
        category_name= Cate.objects.get(pk=category_id)  # Assuming the select field is named 'category'

        pro=Product.objects.create(
            product_name=product_name ,
            product_des=product_des ,
            product_quantity=product_quantity ,
            room_no=room_no ,
            category_name=category_name ,
        )
        pro.save()
        
        messages.success(request, 'Product added successfully.')
        ProductMessage.objects.create(content="Product added successfully")

        return redirect('/product/')

    context={
        'rooms':rooms ,
        'categories':categories ,
             }
    return render(request, 'product.html',context)

def base_side(request):
    return render(request,"base_side.html")

def Product_list(request):
    queryset=Product.objects.all()

    if request.GET.get("search"):
        queryset=queryset.filter(product_name__icontains=request.GET.get("search"))|queryset.filter(room_no__room_no__icontains=request.GET.get("search"))

    context={
    'product':queryset,
   }
    return render(request, "product_list.html",context);
def delete_product(request,id):
    
     queryset=Product.objects.get(id=id)
     queryset.delete()
     messages.success(request, 'Product deleted successfully.')
     ProductMessage.objects.create(content="Product deleted successfully")


     return redirect('/Product_list/')
def update_product(request, id):
    rooms = Room.objects.all()
    categories = Cate.objects.all()
    queryset = Product.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        product_name = data.get('product_name')
        product_des = data.get('product_des')
        product_quantity = int(data.get('product_quantity'))
        room_id = data.get('room')
        category_id = data.get('category')

        room_no = Room.objects.get(pk=room_id)
        category_name = Cate.objects.get(pk=category_id)

        queryset.product_name = product_name
        queryset.product_des = product_des
        queryset.product_quantity = product_quantity
        queryset.room_no = room_no
        queryset.category_name = category_name

        queryset.save()
        messages.success(request, 'Product updated successfully.')
        ProductMessage.objects.create(content="Product updated successfully")


        return redirect('/Product_list/')

    context = {'product': queryset, 'rooms': rooms, 'categories': categories}
    return render(request, "product_update.html", context)


def Dashboard(request):
    product=Product.objects.all()
    category=Cate.objects.all()
    category_quantity=category.count()
    product_quantity=product.count()
    room=Room.objects.all()
    room_quantity=room.count()
    sum=0
    for tot_product in product:
        sum+=tot_product.product_quantity
    
    context={
        'product_quantity':product_quantity,
        'product' : product,
        'category_quantity':category_quantity,
        "room_quantity":room_quantity,
        'sum':sum,
             }
    return render(request, "dashboard.html",context);

def message(request):
    queryset=ProductMessage.objects.all()

    context={
    'message':queryset,
   }
    return render(request, "message.html",context)