from pymavlink import mavutil
from pymavlink.mavwp import MAVWPLoader


def save_waypoint_file(waypoint):
    wploader = MAVWPLoader()
    wploader.add(waypoint)
    wploader.save("waypoints.txt")


waypoint = mavutil.mavlink.MAVLink_mission_item_message(
    1,       # target_system
    1,       # target_component
    1,       # seq
    0,       # frame
    mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,  # command
    1,       # current
    1,       # autocontinue
    0,       # param1
    0,       # param2
    0,       # param3
    0,       # param4
    47.1234,  # x
    -122.5678,  # y
    10       # z
)

save_waypoint_file(waypoint)
