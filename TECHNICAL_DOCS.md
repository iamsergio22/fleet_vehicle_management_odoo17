# Fleet Vehicle Management - Technical Documentation

## Module Architecture

### Overview
The Fleet Vehicle Management module follows Odoo's standard module structure and implements a custom vehicle management system with integrated maintenance tracking and partner relationships.

### Module Structure
```
fleet_vehicle_management_odoo17/
├── __init__.py                 # Module initialization
├── __manifest__.py            # Module manifest and metadata
├── models/
│   └── my_company_vehicle.py  # Main vehicle model
├── views/
│   ├── vehicle_views.xml      # Vehicle UI views
│   ├── vehicle_menu.xml       # Menu structure
│   └── res_partner.xml        # Partner form extension
├── security/
│   ├── vehicle_security.xml   # Security groups and rules
│   └── ir.model.access.csv    # Access rights
└── demo/
    └── demo.xml               # Demo data
```

## Model Implementation

### MyCompanyVehicle Model

#### Class Definition
```python
class MyCompanyVehicle(models.Model):
    _name = 'my.company.vehicle'
    _description = 'Company Vehicle'
```

#### Field Definitions

| Field | Type | Attributes | Description |
|-------|------|------------|-------------|
| name | Char | required=True | Vehicle identifier |
| license_plate | Char | required=True | Registration number |
| fuel_type | Selection | - | Fuel type selection |
| mileage | Float | - | Current mileage |
| last_service_date | Date | - | Last maintenance date |
| needs_service | Boolean | compute, store | Service requirement flag |
| partner_id | Many2one | ondelete='cascade' | Vehicle owner |

#### Field Details

**fuel_type Selection Options:**
```python
[('gasoline', 'Gasoline'), ('diesel', 'Diesel'), ('electric', 'Electric')]
```

**partner_id Relationship:**
- Model: `res.partner`
- On Delete: Cascade (removes vehicle if partner is deleted)

### Business Logic Methods

#### Service Detection Algorithm
```python
@api.depends('mileage', 'last_service_date')
def _compute_needs_service(self):
    for record in self:
        six_months_ago = datetime.now().date() - timedelta(days=180)
        record.needs_service = (
            record.mileage > 20000 or
            (record.last_service_date and record.last_service_date < six_months_ago)
        )
```

**Logic:**
- Triggers on mileage or last_service_date changes
- Sets needs_service to True if:
  - Mileage > 20,000 units
  - Last service date > 6 months ago
- Stored computed field for performance

#### Fuel Type Change Handler
```python
@api.onchange('fuel_type')
def _onchange_fuel_type(self):
    if self.fuel_type == 'electric':
        self.mileage = 0
```

**Purpose:**
- Automatically resets mileage to 0 for electric vehicles
- Client-side execution only (not stored until save)

#### Record Creation Validation
```python
@api.model
def create(self, vals):
    if 'license_plate' in vals:
        existing_vehicle = self.search([('license_plate', '=', vals['license_plate'])], limit=1)
        if existing_vehicle:
            raise ValidationError("A vehicle with this license plate already exists.")
    return super(MyCompanyVehicle, self).create(vals)
```

**Validation:**
- Checks for duplicate license plates before creation
- Raises ValidationError if duplicate found
- Ensures data integrity

## View Implementation

### Kanban View
```xml
<record id="view_vehicle_kanban" model="ir.ui.view">
    <field name="name">my.company.vehicle.kanban</field>
    <field name="model">my.company.vehicle</field>
    <field name="arch" type="xml">
        <kanban>
            <field name="name"/>
            <field name="license_plate"/>
            <field name="needs_service"/>
            <templates>
                <t t-name="kanban-box">
                    <div class="oe_kanban_global_click">
                        <strong><field name="name"/></strong>
                        <div>License Plate: <field name="license_plate"/></div>
                        <div>Needs Service: <field name="needs_service"/></div>
                    </div>
                </t>
            </templates>
        </kanban>
    </field>
</record>
```

**Features:**
- Visual card layout
- Displays key information at a glance
- Clickable cards for navigation
- Service status indicator

### Form View
```xml
<record id="view_vehicle_form" model="ir.ui.view">
    <field name="name">my.company.vehicle.form</field>
    <field name="model">my.company.vehicle</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <div class="oe_button_box" name="button_box">
                    <button name="schedule_service" type="object" 
                            string="Schedule Service" 
                            class="oe_stat_button btn btn-success"/>
                </div>
                <group>
                    <group>
                        <field name="name"/>
                        <field name="license_plate"/>
                        <field name="partner_id"/>
                    </group>
                    <group>
                        <field name="fuel_type"/>
                        <field name="mileage"/>
                    </group>
                </group>
                <group>
                    <field name="last_service_date"/>
                    <field name="needs_service" readonly="1"/>
                </group>
            </sheet>
        </form>
    </field>
</record>
```

**Layout:**
- Button box with service scheduling action
- Two-column layout for basic information
- Service information in separate group
- Read-only service status indicator

## Security Implementation

### Access Rights (ir.model.access.csv)
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_vehicle_user,access.vehicle.user,model_my_company_vehicle,base.group_user,1,0,0,0
access_vehicle_manager,access.vehicle.manager,model_my_company_vehicle,group_vehicle_manager,1,1,1,1
```

**Permissions:**
- **Regular Users**: Read-only access (1,0,0,0)
- **Vehicle Managers**: Full access (1,1,1,1)

### Security Groups (vehicle_security.xml)
```xml
<record id="group_vehicle_manager" model="res.groups">
    <field name="name">Vehicle Manager</field>
</record>
```

### Access Rules
```xml
<record id="rule_vehicle_manager" model="ir.rule">
    <field name="name">Vehicle Manager Access</field>
    <field name="model_id" ref="model_my_company_vehicle" />
    <field name="groups" eval="[(4, ref('group_vehicle_manager'))]" />
    <field name="domain_force">[('id', '!=', False)]</field>
</record>
```

**Rule Details:**
- Applies to Vehicle Manager group
- Allows access to all records (domain: `[('id', '!=', False)]`)
- No record-level restrictions

## Menu Structure

### Main Menu
```xml
<menuitem id="menu_fleet_management" name="Fleet Management" sequence="10"/>
```

### Submenu
```xml
<menuitem id="menu_vehicle" name="Vehicles" 
          parent="menu_fleet_management"
          action="action_vehicle" 
          groups="fleet_vehicle_management_odoo17.group_vehicle_manager,base.group_user" />
```

**Access Control:**
- Requires either Vehicle Manager or base user group
- Hierarchical menu structure

## Partner Integration

### Partner Form Extension
```xml
<record id="view_res_partner_form_inherit" model="ir.ui.view">
    <field name="name">res.partner.form.inherit</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="base.view_partner_form" />
    <field name="arch" type="xml">
        <xpath expr="//field[@name='category_id']" position="after">
            <field name="vehicle_count"/>
        </xpath>
    </field>
</record>
```

**Integration:**
- Extends base partner form
- Adds vehicle count field
- Positioned after category field

## Action Definition

### Vehicle Action
```xml
<record id="action_vehicle" model="ir.actions.act_window">
    <field name="name">Vehicles</field>
    <field name="res_model">my.company.vehicle</field>
    <field name="view_mode">kanban,tree,form</field>
</record>
```

**Configuration:**
- Window action for vehicle model
- Multiple view modes: kanban, tree, form
- Default view order

## API Reference

### Model Methods

#### Public Methods
- `schedule_service()`: Placeholder for service scheduling functionality

#### Private Methods
- `_compute_needs_service()`: Computed field method
- `_onchange_fuel_type()`: Onchange handler
- `create()`: Overridden creation method

### Computed Fields
- `needs_service`: Boolean field computed from mileage and service date

### Constraints
- License plate uniqueness enforced at creation
- Electric vehicle mileage auto-reset

## Performance Considerations

### Computed Fields
- `needs_service` is stored for performance
- Depends on `mileage` and `last_service_date`
- Automatic recomputation on field changes

### Database Indexes
- License plate field should be indexed for uniqueness checks
- Consider adding indexes on frequently queried fields

### Query Optimization
- Service detection uses efficient date arithmetic
- Limited search scope for duplicate detection

## Extension Points

### Adding New Fields
1. Add field definition to model
2. Update views to display new field
3. Add to security rules if needed
4. Update computed field dependencies

### Customizing Business Logic
1. Override existing methods
2. Add new computed fields
3. Implement additional validation rules
4. Extend service detection logic

### Security Extensions
1. Add new security groups
2. Create record-level access rules
3. Implement field-level security
4. Add domain restrictions

## Testing Considerations

### Unit Tests
- Test service detection logic
- Validate license plate uniqueness
- Test fuel type change behavior
- Verify computed field calculations

### Integration Tests
- Test partner integration
- Validate security permissions
- Test menu access control
- Verify view rendering

### Data Validation
- Test edge cases in service detection
- Validate date arithmetic accuracy
- Test duplicate prevention
- Verify cascade deletion

## Deployment Notes

### Installation Order
1. Install base module
2. Create security groups
3. Load access rights
4. Install views and menus
5. Load demo data (optional)

### Configuration Requirements
- Ensure proper user group assignments
- Configure partner relationships
- Set up initial service schedules
- Validate security rules

### Migration Considerations
- Preserve existing vehicle data
- Update external IDs if needed
- Validate security group assignments
- Test computed field calculations

---

**Technical Contact**: Development Team  
**Last Updated**: 2024  
**Odoo Version**: 17.0+ 