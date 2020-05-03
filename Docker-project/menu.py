import os
os.system("tput setaf 1")
print("\t\t\tHey Welcome to my Docker TUI Project")
os.system("tput setaf 7")
print("\t\t\t------------------------------------")
print("\n\n\n\n")
while True:
    print("""Press 1 for pull the images
Press 2 for run the containers
Press 3 for start the container
Press 4 for attach the container
Press 5 for commit the image
Press 6 for creating a storage
Press 7 for run a containers in a particular storage
Press 8 for docker-compose installation
Press 9 creating a yml file for a docker compose based project
Press 10 for running a docker compose
Press 11 for start a docker compose
Press 12 for exit the TUI""")
    print("Enter your Choice: ", end="")
    ch = input()
    if int(ch) == 1:
        print("Name the image which you can pull in docker: " , end = "")
        create_image = input()
        os.system("docker pull {}".format(create_image))
    elif int(ch) == 2:
        print("Name the container and image to run it: " , end = "")
        create_container = input()
        image = input()
        os.system("docker run -dit --name {} {}".format(create_container,image))
    elif int(ch) == 3:
        print("Name the container for start the image: ", end = "")
        container_name = input()
        os.system("docker start {}".format(container_name))
    elif int(ch) == 4:
        print("Name the container for attachment: ", end = "")
        container = input()
        os.system("docker attach {}".format(container))
    elif int(ch) == 5:
        print("Enter the container and new image name for creation of copy image: ")
        container = input()
        new_image = input()
        os.system("docker commit {} {}".format(container,new_image))
    elif int(ch) == 6:
        print("Enter the volume name for creation of Storage: ")
        create_volume = input()
        os.system("docker volume create {}".format(create_volume))
    elif int(ch) == 7:
        print("Enter the volume,image and container name to run inside a container into a storage: ")
        container = input()
        volume = input()
        image = input()
        os.system("docker run -it --name {} -v {}:/var/www/html {}".format(container,volume,image))
    elif int(ch) == 8:
        print("Docker Compose is installing")
        os.system(" curl -L 'https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)' -o /usr/local/bin/docker-compose ")
        os.system("chmod +x /usr/local/bin/docker-compose")
        print("Docker Compose is Successfully Installed")
    elif int(ch) == 9:
        os.system("vim docker-compose.yml")
    elif int(ch) == 10:
        print("Docker Compose is running")
        os.system("docker-compose up")
    elif int(ch) == 11:
        print("Docker Compose is starting a infrastructure")
        os.system("docker-compose start")
    elif int(ch) == 12:
        print("It Exits the TUI Terminal")
        exit()
    else:
        print("Option is not available")
    os.system("clear")
