from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse  # Add JsonResponse here
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from timezonefinder import TimezoneFinder
from django.core.serializers import serialize
from branchwatchapp.models import CompanyBranch,Branch
from django.template.context import Context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import UserAuthentication
from .forms import CustomUserLoginForm
from django.contrib.auth.decorators import login_required
import pandas as pd
import pytz


def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = UserAuthentication.objects.get(username=username)
                if user.check_password(password):
                    # Handle login
                    login(request, user) # type: ignore
                    return redirect('home')  # Redirect to a success page.
                else:
                    form.add_error('password', 'Invalid password')
            except UserAuthentication.DoesNotExist:
                form.add_error('username', 'Username does not exist')
    else:
        form = CustomUserLoginForm()
    
    return render(request, 'login.html', {'form': form})

def your_view_function(request):
    # Instantiate TimezoneFinder
    obj = TimezoneFinder()

    # Fetch your data from the CompanyBranch model
    queryset = CompanyBranch.objects.all()
    
    # Initialize an empty GeoJSON object
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    
    # Convert queryset to GeoJSON
    for branch in queryset:
        try:
            tz = pytz.timezone(branch.time_zone) # type: ignore
        except pytz.exceptions.UnknownTimeZoneError:
            print(f"Unknown time zone for branch {branch.Branch_Id}: {branch.time_zone}")
            continue
        localized_time = datetime.now(tz)
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [branch.Geom.x, branch.Geom.y]
            },
            "properties": {
                "Branch_Id": branch.Branch_Id,
                "Branch_Name": branch.Branch_Name,
                "Time_Zone": branch.time_zone,
                
                # Add other fields as needed
            }
        }
        
        latitude = feature['geometry']['coordinates'][1]
        longitude = feature['geometry']['coordinates'][0]
        
        # Find the time zone
        result = obj.timezone_at(lat=latitude, lng=longitude)
        
        # Add the time zone to the feature properties
        feature['properties']['Time_Zone'] = result

        localized_time = datetime.now(pytz.timezone(branch.time_zone))  # type: ignore # Convert to local time
        feature["properties"]["Localized_Time"] = localized_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        
        # Append the feature to the GeoJSON object
        geojson['features'].append(feature)
    
    return JsonResponse(geojson)

def companybranch_dataset(request):
    try:
        branches = CompanyBranch.objects.all()
        features = []
        for branch in branches:
            try:
                tz = pytz.timezone(branch.time_zone) # type: ignore
            except pytz.exceptions.UnknownTimeZoneError:
                print(f"Unknown time zone for branch {branch.Branch_Id}: {branch.time_zone}")
                continue
            localized_time = datetime.now(tz)
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [branch.Geom.x, branch.Geom.y],
                },
                "properties": {
                    "Branch_Id": branch.Branch_Id,
                    "Branch_Name": branch.Branch_Name,
                    "Info": branch.Info,
                    # "Address": branch.Address,
                    # "Phone" : branch.Phone,
                    # "Branch_Info": branch.Branch_Info,
                    # "Shipping_Instructions": branch.Shipping_Instructions,
                    # "Ordering_Instructions": branch.Ordering_Instructions,
                    # "Branch_Specific_Policies" : branch.Branch_Specific_Policies,
                    # "Dropbox_Locations_Carriers" :branch.Dropbox_Locations_Carriers,
                    # "Other_Notes": branch.Other_Notes,
                    'Time_Zone': branch.time_zone,
                    "Localized_Time": localized_time.strftime('%H:%M:%S %Z%z'), #%Y-%m-%d
                    # Add other fields here
                },
            }
            features.append(feature)
            if branch.time_zone is None:
                print(f"Time zone is None for branch {branch.Branch_Id}")

        geojson = {
            "type": "FeatureCollection",
            "features": features,
        }

        return JsonResponse(geojson, safe=False)
    except Exception as e:
        print(f"An error occurred: {e}")  # Debugging line
        return JsonResponse({"error": f"Internal Server Error: {e}"}, status=500)
    
def division_dataset(request, division):
    try:
        # Filter branches by Division
        branches = CompanyBranch.objects.filter(Division=division)
        features = []
        
        for branch in branches:
            try:
                tz = pytz.timezone(branch.time_zone) # type: ignore
            except pytz.exceptions.UnknownTimeZoneError:
                print(f"Unknown time zone for branch {branch.Branch_Id}: {branch.time_zone}")
                continue

            localized_time = datetime.now(tz)
            
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [branch.Geom.x, branch.Geom.y],
                },
                "properties": {
                    "Branch_Id": branch.Branch_Id,
                    "Branch_Name": branch.Branch_Name,
                    "Info": branch.Info,
                    # "Phone": branch.Phone,
                    # "Branch_Info": branch.Branch_Info,
                    'Time_Zone': branch.time_zone,
                    "Localized_Time": localized_time.strftime('%H:%M:%S %Z%z'),
                    # Add other fields here
                },
            }
            features.append(feature)

        geojson = {
            "type": "FeatureCollection",
            "features": features,
        }

        return JsonResponse(geojson, safe=False)

    except Exception as e:
        print(f"An error occurred: {e}")  # Debugging line
        return JsonResponse({"error": f"Internal Server Error: {e}"}, status=500)

def get_branch_info(request, branch_id):
    try:
        branch = CompanyBranch.objects.get(Branch_Id=branch_id)
        if branch:
            data = {
                # "Branch_Id": branch.Branch_Id,
                # "Branch_Name": branch.Branch_Name,
                "Info": branch.Info,
                # "Address": branch.Address,
                # "Phone" : branch.Phone,
                # "Branch_Info": branch.Branch_Info,
                # "Shipping_Instructions": branch.Shipping_Instructions,
                # "Ordering_Instructions": branch.Ordering_Instructions,
                # "Branch_Specific_Policies" : branch.Branch_Specific_Policies,
                # "Dropbox_Locations_Carriers" :branch.Dropbox_Locations_Carriers,
                # "Other_Notes": branch.Other_Notes,
                # Add other fields here
            }
            return JsonResponse(data)
        else:
            return JsonResponse({"error": "Branch not found"}, status=404)
    except Exception as e:
        print(f"An error occurred: {e}")  # Debugging line
        return JsonResponse({"error": "Internal Server Error"}, status=500)


def get_branch_contact(request, branch_id):
    try:
        branch = Branch.objects.get(Branch_Id=branch_id)
        data = {
            'Name': branch.Name,
            'Contacts': branch.Contacts,
            # 'Misc': branch.Misc,
            # 'Parts': branch.Parts,
            # 'Shipping_Info': branch.Shipping_Info,
            # 'Service': branch.Service,
            # 'Sales': branch.Sales,
        }
        return JsonResponse(data)
    except Branch.DoesNotExist:
        return JsonResponse({'error': 'Branch not found'}, status=404)
# New function to pass model headers
def get_branch_headers(request):
    # Get field names from the Branch model
    field_names = [field.name for field in Branch._meta.get_fields()]
     # Remove Branch_Id and Name from the list
    field_names = [f for f in field_names if f not in ['Branch_Id', 'Name']]
    return JsonResponse({'field_names': field_names})
    
@login_required(login_url='/admin/login/')
def home(request):
    """ Renders home page """
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
        }
    )

