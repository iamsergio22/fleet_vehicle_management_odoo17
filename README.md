# Fleet Vehicle Management Module for Odoo 17

## Overview

The Fleet Vehicle Management module is a comprehensive solution for managing company vehicles in Odoo 17. It provides a complete system for tracking vehicle information, maintenance schedules, and ownership details with an intuitive user interface and robust security features.

## Features

### 🚗 Vehicle Management
- **Vehicle Registration**: Complete vehicle information tracking including name, license plate, and fuel type
- **Fuel Type Support**: Supports gasoline, diesel, and electric vehicles
- **Mileage Tracking**: Automatic mileage monitoring and service scheduling
- **Service Management**: Automated service reminders based on mileage and time intervals
- **Owner Assignment**: Link vehicles to partners/contacts for ownership tracking

### 🔧 Maintenance Features
- **Service Scheduling**: Automatic detection of vehicles needing service
- **Service History**: Track last service dates and maintenance requirements
- **Smart Alerts**: Automatic flagging of vehicles requiring maintenance based on:
  - Mileage exceeding 20,000 units
  - Last service date older than 6 months

### 👥 User Interface
- **Kanban View**: Visual card-based interface for quick vehicle overview
- **List View**: Detailed table view with all vehicle information
- **Form View**: Comprehensive form for detailed vehicle management
- **Dashboard Integration**: Seamless integration with Odoo's main interface

### 🔐 Security & Access Control
- **Role-Based Access**: Two-tier security system
  - **Vehicle Managers**: Full CRUD operations on vehicles
  - **Regular Users**: Read-only access to vehicle information
- **Data Protection**: Secure access rules and permissions

## Installation

### Prerequisites
- Odoo 17.0 or later
- Python 3.11+
- Access to Odoo development environment

### Installation Steps

1. **Clone or Download the Module**
   ```bash
   # Place the module in your Odoo addons directory
   cp -r fleet_vehicle_management_odoo17 /path/to/odoo/addons/
   ```

2. **Update Module List**
   - Go to Apps → Update Apps List in Odoo
   - Or restart Odoo server to auto-detect the module

3. **Install the Module**
   - Navigate to Apps in Odoo
   - Search for "Fleet Vehicle Management"
   - Click Install

4. **Configure Security Groups**
   - The module automatically creates a "Vehicle Manager" group
   - Assign users to appropriate groups based on their responsibilities

## Usage Guide

### Accessing the Module

1. **Main Menu**: Navigate to "Fleet Management" in the main menu
2. **Vehicles Submenu**: Click on "Vehicles" to access the vehicle list

### Adding a New Vehicle

1. Click "Create" button in the Vehicles view
2. Fill in the required fields:
   - **Name**: Vehicle name/identifier
   - **License Plate**: Vehicle registration number
   - **Fuel Type**: Select from Gasoline, Diesel, or Electric
   - **Owner**: Assign to a partner/contact (optional)
3. Save the record

### Managing Vehicle Information

#### Basic Information
- **Name**: Vehicle identifier (required)
- **License Plate**: Registration number (required, must be unique)
- **Fuel Type**: Type of fuel used
- **Owner**: Associated partner/contact

#### Maintenance Information
- **Mileage**: Current vehicle mileage
- **Last Service Date**: Date of last maintenance
- **Needs Service**: Automatic flag (computed field)

### Service Management

#### Automatic Service Detection
The system automatically flags vehicles for service when:
- Mileage exceeds 20,000 units
- Last service date is older than 6 months

#### Manual Service Scheduling
1. Open a vehicle record
2. Click "Schedule Service" button
3. Update service information as needed

### Partner Integration

The module extends the Partner (Contact) form to show:
- **Vehicle Count**: Number of vehicles owned by the partner
- **Vehicle Management**: Direct access to vehicle records

## Technical Architecture

### Models

#### `my.company.vehicle`
Main vehicle model with the following fields:

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| name | Char | Vehicle name/identifier | Yes |
| license_plate | Char | Registration number | Yes |
| fuel_type | Selection | Gasoline/Diesel/Electric | No |
| mileage | Float | Current mileage | No |
| last_service_date | Date | Last maintenance date | No |
| needs_service | Boolean | Service required flag | Computed |
| partner_id | Many2one | Vehicle owner | No |

### Views

#### Kanban View (`view_vehicle_kanban`)
- Visual card layout showing key vehicle information
- Displays name, license plate, and service status
- Click to open detailed form

#### Form View (`view_vehicle_form`)
- Comprehensive form for vehicle management
- Organized in logical groups
- Service scheduling button
- Read-only service status indicator

#### List View
- Tabular view with all vehicle fields
- Sortable and filterable columns
- Bulk operations support

### Security Model

#### Access Rights (`ir.model.access.csv`)
- **Vehicle User**: Read-only access for regular users
- **Vehicle Manager**: Full CRUD access for managers

#### Security Groups (`vehicle_security.xml`)
- **Vehicle Manager Group**: Created automatically
- **Access Rules**: Domain-based record access control

### Business Logic

#### Service Detection Algorithm
```python
def _compute_needs_service(self):
    six_months_ago = datetime.now().date() - timedelta(days=180)
    needs_service = (
        mileage > 20000 or
        (last_service_date and last_service_date < six_months_ago)
    )
```

#### Validation Rules
- **License Plate Uniqueness**: Prevents duplicate license plates
- **Electric Vehicle Mileage**: Auto-sets mileage to 0 for electric vehicles

## Configuration

### Module Dependencies
- `base`: Core Odoo functionality
- `contacts`: Partner management integration

### Data Files
- `security/vehicle_security.xml`: Security groups and rules
- `security/ir.model.access.csv`: Access rights
- `views/vehicle_views.xml`: Vehicle interface views
- `views/vehicle_menu.xml`: Menu structure
- `views/res_partner.xml`: Partner form extension

## Customization

### Adding New Fields
1. Modify `models/my_company_vehicle.py`
2. Update corresponding views in `views/vehicle_views.xml`
3. Update security rules if needed

### Customizing Service Logic
1. Modify `_compute_needs_service` method
2. Adjust mileage thresholds and time intervals
3. Add additional service criteria as needed

### Extending Partner Integration
1. Add fields to partner model
2. Update partner views in `views/res_partner.xml`
3. Implement related business logic

## Troubleshooting

### Common Issues

#### Installation Errors
- **External ID Errors**: Ensure all XML IDs are correctly referenced
- **Permission Errors**: Check user group assignments
- **Module Not Found**: Verify module is in correct addons directory

#### Runtime Issues
- **Service Not Detected**: Check mileage and service date values
- **Access Denied**: Verify user group permissions
- **Duplicate License Plates**: Ensure unique license plate values

### Debug Mode
Enable debug mode in Odoo to see detailed error messages and technical information.

## Development

### Code Structure
```
fleet_vehicle_management_odoo17/
├── __init__.py
├── __manifest__.py
├── models/
│   └── my_company_vehicle.py
├── views/
│   ├── vehicle_views.xml
│   ├── vehicle_menu.xml
│   └── res_partner.xml
├── security/
│   ├── vehicle_security.xml
│   └── ir.model.access.csv
└── demo/
    └── demo.xml
```

### Contributing
1. Follow Odoo development standards
2. Test changes thoroughly
3. Update documentation for new features
4. Maintain backward compatibility

## License

This module is provided as-is for educational and development purposes. Please ensure compliance with your organization's licensing requirements.

## Support

For technical support or feature requests, please contact the development team or create an issue in the project repository.

---

**Version**: 0.1  
**Author**: Sergio Rojas  
**Last Updated**: 2024  
**Compatibility**: Odoo 17.0+ 