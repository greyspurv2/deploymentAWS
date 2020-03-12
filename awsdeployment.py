import time
import base64
boto.ec2 import connect_to_region

#ec2 instance connection goes here

ec2_conn = connect_to_region("ap-southwest-2")

#create security group allowing SSH and connections
#put connection configurations here.
demo_sg = ec2_conn.create.security_group("demo_sg")
demo_sg.authorize("tcp", 22, 22, "0.0.0.0/0")
demo_sg.authorize("tcp", 22, 22, "0.0.0.0/0")

#create a save a public key for SSH login

demo_key = ec2_conn.create_key_pair("demo-key")
demo_key.save(".")


with open("init.py") as f:
    userdata = f.read()

resrv = ec2_conn.run_instances("ami-fade91a9", key_name= demo-key, isntance_type=t1.micro, security_groups=["demo-sg"], user_data=userdata)


#get the demo instance IP address.

demo = resrv.instances[0]
while demo.update() != "running":
    time.sleep(1)
    print demo.ip_address