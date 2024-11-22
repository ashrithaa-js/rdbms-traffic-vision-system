from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Drivers(models.Model):
    driver_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    name = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(unique=True, max_length=20, blank=True, null=True)
    contact_info = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    license_expiry = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drivers'

    def __str__(self):
        return str(self.driver_id)


class EmergencyServices(models.Model):
    service_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    service_type = models.CharField(max_length=50, blank=True, null=True)
    response_time = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    availability_status = models.IntegerField(blank=True, null=True)
    service_area = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_services'


class ParkingLots(models.Model):
    parking_lot_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    location = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    available_spaces = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    road = models.ForeignKey('Roads', models.DO_NOTHING, blank=True, null=True)
    last_maintenance = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parking_lots'


class Roads(models.Model):
    road_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    name = models.CharField(max_length=50, blank=True, null=True)
    lane_count = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    congestion_level = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    length_km = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    max_speed_limit = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roads'


class TollBooths(models.Model):
    toll_booth_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    location = models.CharField(max_length=50, blank=True, null=True)
    road = models.ForeignKey(Roads, models.DO_NOTHING, blank=True, null=True)
    toll_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    collected_fees = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    last_collection_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toll_booths'


class TrafficCameras(models.Model):
    camera_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    location = models.CharField(max_length=100, blank=True, null=True)
    road = models.ForeignKey(Roads, models.DO_NOTHING, blank=True, null=True)
    last_maintenance = models.DateField(blank=True, null=True)
    camera_type = models.CharField(max_length=50, blank=True, null=True)
    active_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traffic_cameras'

    def __str__(self):
        return str(self.camera_id)


class TrafficIncidents(models.Model):
    incident_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    road = models.ForeignKey(Roads, models.DO_NOTHING, blank=True, null=True)
    incident_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    response_time = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    severity_level = models.CharField(max_length=20, blank=True, null=True)
    reported_by = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='reported_by', blank=True, null=True)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING, blank=True, null=True)
    emergency_service = models.ForeignKey(EmergencyServices, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traffic_incidents'


class TrafficLights(models.Model):
    light_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    location = models.CharField(max_length=50, blank=True, null=True)
    current_status = models.CharField(max_length=15, blank=True, null=True)
    road = models.ForeignKey(Roads, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)
    operation_mode = models.CharField(max_length=20, blank=True, null=True)
    maintenance_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traffic_lights'


class TrafficViolations(models.Model):
    violation_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    driver = models.ForeignKey('Drivers', models.DO_NOTHING, blank=True, null=True)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING, blank=True, null=True)
    violation_type = models.CharField(max_length=50, blank=True, null=True)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    violation_date = models.DateField(blank=True, null=True)
    violation_time = models.TimeField(blank=True, null=True)
    camera = models.ForeignKey('TrafficCameras', models.DO_NOTHING, blank=True, null=True)
    penalty_points = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traffic_violations'

    def __str__(self):
        return str(self.violation_id)


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=20)
    uname = models.CharField(max_length=100)
    uemail = models.CharField(max_length=254)
    ucontact = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'user'


class Vehicles(models.Model):
    vehicle_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    vehicle_number = models.CharField(unique=True, max_length=20, blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(Drivers, models.DO_NOTHING, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    vehicle_model = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    insurance_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles'

    def __str__(self):
        return str(self.vehicle_id)
