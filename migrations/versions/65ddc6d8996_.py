"""empty message

Revision ID: 65ddc6d8996
Revises: None
Create Date: 2015-06-14 23:26:55.397442

"""

# revision identifiers, used by Alembic.
revision = '65ddc6d8996'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('GTFS_STOPS',
    sa.Column('stop_id', sa.Integer(), nullable=False),
    sa.Column('stop_code', sa.String(), nullable=True),
    sa.Column('stop_name', sa.String(), nullable=True),
    sa.Column('stop_desc', sa.String(), nullable=True),
    sa.Column('stop_lat', sa.Float(), nullable=True),
    sa.Column('stop_lon', sa.Float(), nullable=True),
    sa.Column('zone_id', sa.Float(), nullable=True),
    sa.Column('stop_url', sa.Float(), nullable=True),
    sa.Column('location_type', sa.Integer(), nullable=True),
    sa.Column('parent_station', sa.Integer(), nullable=True),
    sa.Column('stop_timezone', sa.String(), nullable=True),
    sa.Column('wheelchair_boarding', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('stop_id')
    )
    op.drop_table('gtfs_transfers')
    op.drop_table('gtfs_stops')
    op.drop_table('gtfs_calendar')
    op.drop_table('gtfs_routes')
    op.drop_table('gtfs_trips')
    op.drop_table('gtfs_calendar_dates')
    op.drop_table('gtfs_shapes')
    op.drop_table('gtfs_stop_times')
    op.drop_table('gtfs_agency')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gtfs_agency',
    sa.Column('agency_id', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('agency_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('agency_url', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('agency_timezone', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('agency_lang', sa.VARCHAR(length=2), autoincrement=False, nullable=True),
    sa.Column('agency_phone', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('agency_fare_url', sa.VARCHAR(length=100), autoincrement=False, nullable=True)
    )
    op.create_table('gtfs_stop_times',
    sa.Column('trip_id', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('arrival_time', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('departure_time', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('stop_id', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('stop_sequence', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('stop_headsign', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('pickup_type', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('drop_off_type', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('shape_dist_traveled', sa.NUMERIC(precision=5, scale=0), autoincrement=False, nullable=True)
    )
    op.create_table('gtfs_shapes',
    sa.Column('shape_id', sa.NUMERIC(precision=6, scale=0), autoincrement=False, nullable=True),
    sa.Column('shape_pt_lat', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('shape_pt_lon', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('shape_pt_sequence', sa.NUMERIC(precision=6, scale=0), autoincrement=False, nullable=True),
    sa.Column('shape_dist_traveled', sa.NUMERIC(), autoincrement=False, nullable=True)
    )
    op.create_table('gtfs_calendar_dates',
    sa.Column('service_id', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('exception_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('exception_type', sa.VARCHAR(length=10), autoincrement=False, nullable=True)
    )
    op.create_table('gtfs_trips',
    sa.Column('route_id', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('service_id', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('trip_id', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('trip_headsign', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('trip_short_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('direction_id', sa.NUMERIC(precision=2, scale=0), autoincrement=False, nullable=True),
    sa.Column('block_id', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('shape_id', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('wheelchair_accessible', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('bikes_allowed', sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    op.create_table('gtfs_routes',
    sa.Column('route_id', sa.NUMERIC(precision=5, scale=0), autoincrement=False, nullable=True),
    sa.Column('agency_id', sa.NUMERIC(precision=3, scale=0), autoincrement=False, nullable=True),
    sa.Column('route_short_name', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('route_long_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('route_desc', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('route_type', sa.NUMERIC(precision=3, scale=0), autoincrement=False, nullable=True),
    sa.Column('route_url', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('route_color', sa.VARCHAR(length=8), autoincrement=False, nullable=True),
    sa.Column('route_text_color', sa.VARCHAR(length=8), autoincrement=False, nullable=True)
    )
    op.create_table('gtfs_calendar',
    sa.Column('service_id', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('monday', sa.NUMERIC(precision=1, scale=0), autoincrement=False, nullable=True),
    sa.Column('tuesday', sa.NUMERIC(precision=1, scale=0), autoincrement=False, nullable=True),
    sa.Column('wednesday', sa.NUMERIC(precision=1, scale=0), autoincrement=False, nullable=True),
    sa.Column('thursday', sa.NUMERIC(precision=1, scale=0), autoincrement=False, nullable=True),
    sa.Column('friday', sa.NUMERIC(precision=1, scale=0), autoincrement=False, nullable=True),
    sa.Column('saturday', sa.NUMERIC(precision=1, scale=0), autoincrement=False, nullable=True),
    sa.Column('sunday', sa.NUMERIC(precision=1, scale=0), autoincrement=False, nullable=True),
    sa.Column('start_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('end_date', sa.DATE(), autoincrement=False, nullable=True)
    )
    op.create_table('gtfs_stops',
    sa.Column('stop_id', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('stop_code', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('stop_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('stop_desc', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('stop_lat', sa.NUMERIC(precision=38, scale=8), autoincrement=False, nullable=True),
    sa.Column('stop_lon', sa.NUMERIC(precision=38, scale=8), autoincrement=False, nullable=True),
    sa.Column('zone_id', sa.NUMERIC(precision=5, scale=0), autoincrement=False, nullable=True),
    sa.Column('stop_url', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('location_type', sa.NUMERIC(precision=2, scale=0), autoincrement=False, nullable=True),
    sa.Column('parent_station', sa.NUMERIC(precision=38, scale=0), autoincrement=False, nullable=True),
    sa.Column('stop_timezone', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('wheelchair_boarding', sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    op.create_table('gtfs_transfers',
    sa.Column('from_stop_id', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('to_stop_id', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('transfer_type', sa.NUMERIC(precision=3, scale=0), autoincrement=False, nullable=True),
    sa.Column('min_transfer_time', sa.NUMERIC(precision=6, scale=0), autoincrement=False, nullable=True)
    )
    op.drop_table('GTFS_STOPS')
    ### end Alembic commands ###
