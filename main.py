import subprocess
import os

curr_env = {}
curr_env.update(os.environ)

if __name__ == "__main__":
    os.system("chmod 777 ./java/bin/java")
    butterfly = subprocess.Popen("./java/bin/java -jar butterfly.jar", stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 env=curr_env, shell=True)
    while True:
        for line in iter(butterfly.stdout.readline, b''):
            line = line.rstrip().decode("iso-8859-1")
            if line:
                print(line)
            else:
                break
