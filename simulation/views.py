from django.shortcuts import render

def simulation(request):
    """Impact simulation page"""
    context = {
        'page_title': 'Impact Simulation'
    }
    return render(request, 'simulation/simulation.html', context)

def calculate_impact(request):
    """This endpoint is not needed as calculations are done in JavaScript"""
    from django.http import JsonResponse
    return JsonResponse({'message': 'Calculations are performed client-side'})