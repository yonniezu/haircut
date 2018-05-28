from django.shortcuts import render

# Create your views here.
def home_page(request):
  
  if request.method == 'POST':
  	 time = request.POST.get('time')
  	 barber = request.POST.get("barber_name")

  	 return render(request, 'haircut/home_page.html', {context}
  return render(request,'haircut/home_page.html')
