# Group Project 1: A Bite of Distributed Communication
## By Alexis Jaime, Sam Lara and Seena Kaboli
--------------------------------------------------------
### How to Compile and Run
1. run pip install pyshark in your terminal or command prompt.
2. Make sure you have your files downloaded and then open up terminal or the command prompt and go to the directory the files are located in.
3. Make sure to have excute permissions enabled on the network.sh file, you can do so by using the command: chmod +x network.sh
4. Ensure you have Docker properly installed.
5. Make sure there is only one custom network named "Proj1-distributed-network" created on your machine.
6. To verify, use: docker network ls in your shell to see all networks, and to remove them use:  docker network remove "network-to-remove", replacing "network-to-remove" with the appropriate network.
7. If you do not have it created, just run: docker network create Proj1-distributed-network
8. Next, use the command: sudo docker-compose up --build , putting in your password for your machine to enable the action.
9. If you are getting an invalid credentials error, use the command: rm ~/.docker/config.json , if not proceed to next step.
10. Now, watch as the master server communicates with the others through two methods, unicast and multicast.
11. Use ctrl + c to terminate the process, the nodes will "gracefully" terminate.
12. After that, run: python log_creator.py in your terminal to generate a log text file of all the network traffic.
13. After log_creator.py is finished running, then you cat log.txt or open with your preferred editor.  
