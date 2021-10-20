import subprocess
import os

curr_env = {}
curr_env.update(os.environ)

if __name__ == "__main__":
    if os.name != "nt":
        os.system("chmod 777 ./java-min/linux/bin/java") 
        butterfly = subprocess.Popen("./java-min/linux/bin/java -jar butterfly.jar", stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, env=curr_env, shell=True)
    else:
        butterfly = subprocess.Popen(r"%cd%\java-min\win\bin\java -jar butterfly.jar", stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, env=curr_env, shell=True)
    while butterfly.stdout.readable():
        line = butterfly.stdout.readline().decode("iso-8859-1")
        if not line:
            break
        print(line)
