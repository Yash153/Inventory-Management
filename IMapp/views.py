from IMapp.models import MovementModel, ProductModel
from IMapp.models import LocationModel
from django.shortcuts import redirect, render
from .forms import ProductForm, LocationForm

def stock(request):
    return render(request, 'stock.html')

def product(request):
    p = ProductModel.objects.all()
    return render(request, 'product.html',{"data": p})

def location(request):
    l = LocationModel.objects.all()
    return render(request, 'location.html', {'data' : l})

def movement(request):
    return render(request, 'movement.html')

def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_product.html', {"form" : form})

def add_location(request):
    form = LocationForm()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_location.html', {"form" : form})


def view_product(request,id):
    vp = ProductModel.objects.get(pk = id)
    return render(request, 'view.html', {'vp':vp})

def view_location(request,id):
    vl = LocationModel.objects.get(pk = id)
    return render(request, 'view.html', {'vl':vl})

def edit_product(request, id):
    ep = ProductModel.objects.get(pk = id)
    location = LocationModel.objects.all()
    return render(request, 'edit_product.html', { 'ep' : ep, 'location' : location })

def save_changes_product(request):
    if request.method == 'POST':
        p_id = request.POST.get('id')
        l_id = request.POST.get('location')
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        update_product = ProductModel.objects.get(pk = p_id)
        l = LocationModel.objects.get(pk = l_id)
        update_product.name = name
        update_product.quantity = quantity
        update_product.location = l
        update_product.save()
        return redirect(product)

def edit_location(request, id):
    el = LocationModel.objects.get(pk = id)
    return render(request, 'edit_location.html', { 'el' : el})

def save_changes_product(request):
    if request.method == 'POST':
        p_id = request.POST.get('id')
        l_id = request.POST.get('location')
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        update_product = ProductModel.objects.get(pk = p_id)
        l = LocationModel.objects.get(pk = l_id)
        update_product.name = name
        update_product.quantity = quantity
        update_product.location = l
        update_product.save()
        return redirect(product)

def save_changes_location(request):
    if request.method == 'POST':
        l_id = request.POST.get('id')
        name = request.POST.get('name')
        update_location = LocationModel.objects.get(pk = l_id)
        update_location.name = name
        update_location.save()
        return redirect(location)

def movement(request):
    product = ProductModel.objects.all()
    location = LocationModel.objects.all()
    if request.method == 'POST':
        available_locations = list()
        p_id = request.POST.get('product')
        from_id = request.POST.get('from_location')
        to_id = request.POST.get('to_location')
        quantity = int(request.POST.get('quantity'))

        from_location = LocationModel.objects.get(id = from_id)
        to_location = LocationModel.objects.get(id = to_id)

        selected_product = ProductModel.objects.get(pk = p_id)
        print(selected_product.name)
        database_quantity = selected_product.quantity
        if quantity > int(database_quantity):
            return render (request, 'movement.html', {'msg' : "Insufficient Stock", 'product' : product, 'location' : location})
        if from_location.name == to_location.name:
            return render(request, 'movement.html', {'msg' : 'Select two different locaations', 'product' : product, 'location' : location})
        print(selected_product.location.name)
        ap = ProductModel.objects.all()
        for a in ap:
            if a.name == selected_product.name:
                available_locations.append(a.location.name)
        for al in available_locations:
            if from_location.name == al:
                selected_product.quantity = database_quantity - quantity
                selected_product.save()
                for a in ap:
                    if a.name == selected_product.name and a.location.name == to_location.name:
                        a.quantity += quantity
                        a.save()
                        m = MovementModel(from_location = from_location.name, to_location = to_location.name, product_id = p_id, product_name = selected_product.name, quantity = quantity)
                        m.save()
                        return render(request, 'movement.html', { 'product' : product, 'location' : location, 'msg' : 'Done' })
                else:
                    p = ProductModel.objects.create(location = to_location, name = selected_product.name, quantity = quantity)
                    p.save()
                m = MovementModel(from_location = from_location.name, to_location = to_location.name, product_id = p_id, product_name = selected_product.name, quantity = quantity)
                m.save()
                return render(request, 'movement.html', { 'product' : product, 'location' : location, 'msg' : 'Done' })
        else:
            
            return render(request, 'movement.html', { 'product' : product, 'location' : location, 'msg' : 'Selected Product not available for this location' })
    else:
        return render(request, 'movement.html', { 'product' : product, 'location' : location })

def stock_location(request):
    al = LocationModel.objects.all()
    if request.method == 'POST':
        l_id = request.POST.get('location')
        selected_location = LocationModel.objects.get(pk = l_id)
        ap = ProductModel.objects.all()
        data = ProductModel.objects.filter(location = selected_location)
        print(data)
        return render(request, 'stock.html', {'data' : data, 'al' : al, 'l' : selected_location.name })
    else:
        return render(request, 'stock.html', { 'al' : al })

def stock_product(request):
    ap = ProductModel.objects.all()
    if request.method == 'POST':
        p_id = request.POST.get('product')
        selected_product = ProductModel.objects.get(pk = p_id)
        ap = ProductModel.objects.all()
        data = ProductModel.objects.filter(name = selected_product.name)
        print(data)
        return render(request, 'stock_product.html', {'data' : data, 'ap' : ap, 'p' : selected_product.name })
    else:
        return render(request, 'stock_product.html', { 'ap' : ap })

def movementhistory(request):
    data = MovementModel.objects.all()
    return render(request, 'movementhistory.html', { 'data' : data })    

def delete_product(request, id):
    ds = ProductModel.objects.get(pk = id)
    ds.delete()
    return redirect('location')

def delete_location(request, id):
    ds = LocationModel.objects.get(pk = id)
    ds.delete()
    return redirect('location')
