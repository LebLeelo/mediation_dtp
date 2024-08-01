# actions.py
from duckietown_msgs.msg import Twist2DStamped
import rospy

# Action for the "Turn Left" sign
def handle_left(instance, pub_car_cmd):
    instance.log("Left")
    # publish 10 messages every second (10Hz)  
    rate = rospy.Rate(10)
    # stop message
    stop = Twist2DStamped(v=0.0, omega=0.0) 

    rospy.loginfo("moving with a radial velocity of 0.5 for 1 seconds")
    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < 1:
      pub_car_cmd.publish(Twist2DStamped(v=0.0, omega=0.5))
      rate.sleep()
    
    # Stop the duckiebot
    rospy.loginfo("stopping")
    pub_car_cmd.publish(stop)


# Ation for the "Park" sign
def handle_park(instance, pub_car_cmd):
    instance.log("Park")
    # publish 10 messages every second (10Hz)  
    rate = rospy.Rate(10)
    # stop message
    stop = Twist2DStamped(v=0.0, omega=0.0) 

    rospy.loginfo("moving with a radial velocity of -0.5 for 6 seconds")
    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < 6:
      pub_car_cmd.publish(Twist2DStamped(v=0.0, omega=-0.5))
      rate.sleep()
    
    # Stop the duckiebot
    rospy.loginfo("stopping")
    pub_car_cmd.publish(stop)
    
    
# Action for the "Turn Right" sign
def handle_right(instance, pub_car_cmd):
    instance.log("Right")
    # publish 10 messages every second (10Hz)  
    rate = rospy.Rate(10)
    # stop message
    stop = Twist2DStamped(v=0.0, omega=0.0) 

    rospy.loginfo("moving with a radial velocity of -0.5 for 1 seconds")
    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < 1:
      pub_car_cmd.publish(Twist2DStamped(v=0.0, omega=-0.5))
      rate.sleep()
    
    # Stop the duckiebot
    rospy.loginfo("stopping")
    pub_car_cmd.publish(stop)


# Action for the "Stop" sign
def handle_stop(instance, pub_car_cmd):
    instance.log("Stop")
    instance.avoid_duckies = True


# ACtion for the "U-Turn" sign
def handle_uturn(instance, pub_car_cmd):
    instance.log("Uturn")
    # publish 10 messages every second (10Hz)  
    rate = rospy.Rate(10)
    # stop message
    stop = Twist2DStamped(v=0.0, omega=0.0) 

    rospy.loginfo("moving with a linear velocity of -0.3 for 2 seconds")
    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < 2:
      pub_car_cmd.publish(Twist2DStamped(v=-0.3, omega=0.0))
      rate.sleep()
    
    rospy.loginfo("moving with a radial velocity of 0.3 for 2 seconds")
    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < 2:
      pub_car_cmd.publish(Twist2DStamped(v=0.0, omega=0.3))
      rate.sleep()
    
    # Stop the duckiebot
    rospy.loginfo("stopping")
    pub_car_cmd.publish(stop)
    
    
# TO DO : ADD THE METHODS OF THE ACTIONS TO BE PERFORMED FOR THE CLASSES YOU ADDED
# ADD BELLOW












# Dictionary to define the classes
Dclasses = {
    0: {"name": "Left", "color": (0, 255, 255), "action": handle_left},
    1: {"name": "Park", "color": (0, 165, 255), "action": handle_park},
    2: {"name": "Right", "color": (0, 250, 0), "action": handle_right},
    3: {"name": "Stop", "color": (0, 0, 255), "action": handle_stop},
    4: {"name": "Uturn", "color": (255, 0, 0), "action": handle_uturn}
    
# TO DO : ADD THE CLASSES YOU TRAINED YOUR NEW MODEL FOR
}


def getColors():
    return {key: value['color'] for key, value in Dclasses.items()}

def getNames():
    return {key: value['name'] for key, value in Dclasses.items()}

def getActions(instance, detected_classes):
    for clas in detected_classes:
        action = Dclasses.get(clas, {}).get('action')
        if action:
            action(instance, instance.pub_car_cmd)
        else:
            instance.log("Unknown class detected")




