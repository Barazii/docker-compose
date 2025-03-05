Docker can be use as a dev env of in which a script is run (only requirements.txt and dependencies included, no source code). In other words, the container is not a standalone microapplication. Docker can be also used as a standalone microapplication.
When docker containers run independently or jointly (with docker-compose), they run on the local machine (laptop), no cloud.
Docker compose for multiple containers/images orchestration basically.
Automating the build and push of docker images using github actions or other tools is only a thing if docker containers are intended to be standalone microapplications.
Each container can run different-language code, one container contains python code, another container contains javascript code.
Running containerized microapplications on the laptop is somehow called 'deployment'.