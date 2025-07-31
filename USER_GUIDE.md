# Fleet Vehicle Management - User Guide

## Getting Started

### Accessing the Module
1. Log into your Odoo system
2. Look for "Fleet Management" in the main menu
3. Click on "Vehicles" to access the vehicle management system

### User Permissions
- **Regular Users**: Can view vehicle information (read-only access)
- **Vehicle Managers**: Can create, edit, and delete vehicles (full access)

## Managing Vehicles

### Viewing Vehicles

#### Kanban View (Default)
- Shows vehicles as cards with key information
- Each card displays:
  - Vehicle name
  - License plate number
  - Service status (needs service or not)
- Click any card to open the detailed vehicle form

#### List View
- Shows all vehicles in a table format
- Displays all vehicle information in columns
- Can be sorted by clicking column headers
- Use filters to find specific vehicles

#### Form View
- Detailed view of a single vehicle
- Shows all vehicle information in organized sections
- Use this view for editing vehicle details

### Adding a New Vehicle

1. **Navigate to Vehicles**
   - Go to Fleet Management → Vehicles

2. **Create New Vehicle**
   - Click the "Create" button
   - Fill in the required information:
     - **Name**: Enter a descriptive name for the vehicle
     - **License Plate**: Enter the vehicle's registration number
     - **Fuel Type**: Select from Gasoline, Diesel, or Electric
     - **Owner**: Choose the person/company who owns the vehicle (optional)

3. **Additional Information** (Optional)
   - **Mileage**: Enter current vehicle mileage
   - **Last Service Date**: Select the date of the last maintenance

4. **Save the Vehicle**
   - Click "Save" to create the vehicle record

### Editing Vehicle Information

1. **Open Vehicle Record**
   - Find the vehicle in the list or kanban view
   - Click on the vehicle to open its form

2. **Make Changes**
   - Update any field as needed
   - Changes are saved automatically

3. **Important Notes**
   - License plate numbers must be unique
   - Changing fuel type to "Electric" will reset mileage to 0
   - Service status updates automatically based on mileage and service date

### Deleting a Vehicle

1. **Open Vehicle Record**
   - Navigate to the vehicle you want to delete

2. **Delete Vehicle**
   - Click the "Action" menu (three dots)
   - Select "Delete"
   - Confirm the deletion

**Note**: Only Vehicle Managers can delete vehicles.

## Service Management

### Understanding Service Status

The system automatically determines if a vehicle needs service based on:
- **Mileage**: Vehicles with more than 20,000 units need service
- **Time**: Vehicles that haven't been serviced in 6 months need service

### Service Status Indicators

- **Green**: Vehicle is in good condition, no service needed
- **Red/Alert**: Vehicle needs service (shown as "True" in needs_service field)

### Scheduling Service

1. **Open Vehicle Record**
   - Navigate to the vehicle that needs service

2. **Schedule Service**
   - Click the "Schedule Service" button
   - Update the "Last Service Date" field with the service date
   - The system will automatically update the service status

### Updating Service Information

1. **After Service is Completed**
   - Open the vehicle record
   - Update the "Last Service Date" field
   - Update the "Mileage" field if it has changed

2. **Service Status Update**
   - The "Needs Service" field will automatically update
   - Green status indicates the vehicle is current on maintenance

## Partner Integration

### Viewing Partner Vehicles

1. **Open Partner Record**
   - Go to Contacts and find the partner/company

2. **Vehicle Information**
   - Look for the "Vehicle Count" field
   - This shows how many vehicles the partner owns

### Assigning Vehicles to Partners

1. **When Creating/Editing a Vehicle**
   - In the vehicle form, find the "Owner" field
   - Select the appropriate partner from the dropdown
   - Save the vehicle

2. **Verification**
   - The partner's vehicle count will automatically update
   - You can verify by checking the partner record

## Best Practices

### Vehicle Naming
- Use descriptive names (e.g., "Company Van 1", "Sales Car Toyota")
- Include make/model in the name for easy identification

### License Plate Management
- Always enter the complete license plate number
- Use consistent formatting (e.g., ABC-123 or ABC123)
- Double-check for typos as license plates must be unique

### Service Tracking
- Update service dates immediately after maintenance
- Keep mileage records current
- Use the service scheduling feature for planning

### Data Maintenance
- Regularly review vehicles that need service
- Update partner assignments when ownership changes
- Archive or delete vehicles that are no longer in use

## Troubleshooting

### Common Issues

#### "License Plate Already Exists" Error
- **Cause**: Trying to create a vehicle with a duplicate license plate
- **Solution**: Check existing vehicles for the license plate number
- **Prevention**: Use a unique license plate for each vehicle

#### Service Status Not Updating
- **Cause**: Mileage or service date not properly entered
- **Solution**: Verify the values in the vehicle record
- **Check**: Ensure dates are in the correct format

#### Cannot Edit Vehicle
- **Cause**: Insufficient user permissions
- **Solution**: Contact your administrator to assign Vehicle Manager role
- **Alternative**: Ask a Vehicle Manager to make the changes

#### Partner Vehicle Count Incorrect
- **Cause**: Vehicle ownership not properly assigned
- **Solution**: Check the "Owner" field in vehicle records
- **Update**: Assign vehicles to the correct partners

### Getting Help

#### Contact Administrator
- For permission issues
- For technical problems
- For data correction requests

#### Self-Service
- Check this user guide
- Review vehicle records for data accuracy
- Use the search and filter features to find information

## Tips and Tricks

### Quick Navigation
- Use the search bar to find vehicles by name or license plate
- Use filters to show only vehicles that need service
- Sort by different columns to organize information

### Efficient Data Entry
- Use copy/paste for similar vehicle information
- Set up templates for common vehicle types
- Use consistent naming conventions

### Monitoring
- Regularly check the kanban view for service alerts
- Use the list view for bulk operations
- Export data for reporting purposes

### Integration
- Link vehicles to the correct partners for better organization
- Use the service scheduling feature for maintenance planning
- Keep all vehicle information current and accurate

---

**Need Help?** Contact your system administrator or refer to the technical documentation for advanced features.

**Last Updated**: 2024  
**Version**: 0.1 