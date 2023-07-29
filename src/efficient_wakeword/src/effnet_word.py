import os
from subprocess import call
import rospy
from std_msgs.msg import String, Bool
from eff_word_net.streams import SimpleMicStream
from eff_word_net.engine import HotwordDetector


def callback():
    kai = HotwordDetector(
    hotword="hello kai",
    reference_file = "/home/acefly/speech_module/src/efficient_wakeword/src/sample_refs/hello_kai_ref.json",
	threshold=0.7 ,
	relaxation_time = 0.8
    )
    mic_stream = SimpleMicStream()
    mic_stream.start_stream()

    pub = rospy.Publisher('eff_net_wake_word', String, queue_size=10)
    session_pub = rospy.Publisher('stt_session_key', Bool, queue_size=10)
    print("Say Hello kai ")
    while not rospy.is_shutdown():
        frame = mic_stream.getFrame()
        result = kai.scoreFrame(frame)
        if result==None :
            #no voice activity
            continue
        if(result["match"]):
            print("Wakeword uttered",result["confidence"])
            pub.publish("wake word detected")
            session_pub.publish(True)


 
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('eff_wake_word', anonymous=True)
    callback()
    #rospy.Subscriber("eff_wake_word_status", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()