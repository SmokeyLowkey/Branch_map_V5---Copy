from django.core.management.base import BaseCommand, CommandError
from branchwatchapp.models import CompanyBranch
from django.contrib.gis.geos import Point
from datetime import datetime
from timezonefinder import TimezoneFinder
import pandas as pd

class Command(BaseCommand):
    help = 'Import branch details from Excel file into the CompanyBranch model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--division',
            type=str,
            help="Specify the division for these branches. E.g., 'CF' or 'TT'",
        )

    def handle(self, *args, **kwargs):
        division = kwargs['division']
        if not division:
            raise CommandError("You must specify a division using the --division flag")
        
        tf = TimezoneFinder(in_memory=True)
        # Read the Excel file
        try:
            excel_path = f'C:\\Branch_map_V5 - COPY\\xlsx\\{division}_BRANCH_DETAILS_V2.xlsx'
            df_excelReader = pd.read_excel(excel_path)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading Excel file: {e}'))
            return

        # Loop through the rows in the DataFrame
        for index, row in df_excelReader.iterrows():
            geom = None  # Initialize to None for each row
            time_zone = None  # Initialize time_zone to None
            try:
                latitude, longitude = map(float, str(row.get('Coordinates', '')).split(','))
                geom = Point(longitude, latitude)
                # Get time zone
                print(latitude, longitude)
                time_zone = tf.certain_timezone_at(lng=longitude, lat=latitude)
                print(time_zone)
                if time_zone is None:
                    self.stdout.write(self.style.ERROR(f'Could not determine time zone for coordinates: {latitude}, {longitude}'))
                    continue  # Skip this row
                
                # Here you can convert your time to local time
                current_time_local = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                your_naive_time = pd.Timestamp(current_time_local)  # Replace with your actual time
                your_utc_time = your_naive_time.tz_localize('UTC')
                your_local_time = your_utc_time.tz_convert(time_zone)
            except (ValueError, TypeError) as e:
                self.stdout.write(self.style.ERROR(f"Error in row {index} for 'Coordinates': {e}"))
                continue

            # Only append the object if geom is not None
            if geom is not None:
                obj, created = CompanyBranch.objects.update_or_create(
                    Branch_Id=row['Branch_Id'],
                    defaults={
                        'Branch_Id': row['Branch_Id'],
                        'Branch_Name': row['Branch_Name'],
                        'Info': row['Info'],
                        # 'WareHouses': row['WareHouses'],
                        # 'Address': row['Address'],
                        # 'Phone': row['Phone'],
                        # 'Branch_Info': row['Branch_Info'],
                        # 'Shipping_Instructions': row['Shipping_Instructions'],
                        # 'Ordering_Instructions': row['Ordering_Instructions'],
                        # 'Branch_Specific_Policies': row['Branch_Specific_Policies'],
                        # 'Dropbox_Locations_Carriers': row['Dropbox_Locations_Carriers'],
                        # 'Other_Notes': row['Other_Notes'],
                        'Geom': geom,
                        'time_zone': time_zone,
                        'Division': division,
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created new record for Branch_ID: {row['Branch_Id']}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated existing record for Branch_ID: {row['Branch_Id']}"))
            else:
                self.stdout.write(self.style.ERROR(f"Skipping row {index} due to null or invalid Coordinates"))
