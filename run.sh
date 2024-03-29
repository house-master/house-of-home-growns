DEPLOYMENT_NAME=$1 # dev | staging | prod
COMMAND_TYPE="${2:-start}" # if not defined then 'start'
PROJECT_NAME='house-of-home-growns-staging'
DOCKER_COMPOSE_FILENAME='docker-compose.staging.yml'
DOCKER_COMPOSE_ENVIRONMENT_FILE='env_configs/staging.env'

############################################################
# Help                                                     #
############################################################
Help()
{
     # Display Help
     echo "Add description of the script functions here."
     echo
     echo "options:"
     echo "h     Print this Help."

     echo "DEPLOYMENT_NAME  --> dev | staging | prod  "
     echo "COMMAND_TYPE     --> start (default) | down "
     echo "FOR EXAMPLE: sh run_setup_server.sh DEPLOYMENT_NAME COMMAND_TYPE"
     echo "FOR EXAMPLE: sh run_setup_server.sh dev start"
     echo
}

# Get the options
while getopts ":hn:" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      n) # Enter a name
         Name=$OPTARG;;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done

case "$DEPLOYMENT_NAME" in
   "production") 
        PROJECT_NAME='house-of-home-growns-production'
        DOCKER_COMPOSE_ENVIRONMENT_FILE='env-configs/production.env'
        DOCKER_COMPOSE_FILENAME='docker-compose.production.yml'
   ;;
   "staging") 
        PROJECT_NAME='house-of-home-growns-staging'
        DOCKER_COMPOSE_ENVIRONMENT_FILE='env-configs/staging.env'
        DOCKER_COMPOSE_FILENAME='docker-compose.staging.yml'
   ;;
   "dev") 
        PROJECT_NAME='house-of-home-growns-dev'
        DOCKER_COMPOSE_ENVIRONMENT_FILE='env-configs/dev.env'
        DOCKER_COMPOSE_FILENAME='docker-compose.dev.yml'
   ;;
   "")
     Help
   ;;
esac

if [ -z $COMMAND_TYPE ]; 
then
    COMMAND_TYPE=start
fi

if [ "$COMMAND_TYPE" = "start" ]
then 

     ( cat $DOCKER_COMPOSE_ENVIRONMENT_FILE ; echo ""; ) > .env
     ( echo "PROJECT_NAME=$PROJECT_NAME" ; echo "") >> .env
     GIT_COMMIT_ID=$(git rev-list -1 HEAD)
     ( echo "GIT_COMMIT_ID=$GIT_COMMIT_ID" ; echo "") >> .env
     GIT_RELEASE_TAG=$(git describe --tags)
     ( echo "GIT_RELEASE_TAG=$GIT_RELEASE_TAG" ; echo "") >> .env
     echo $DOCKER_COMPOSE_ENVIRONMENT_FILE


     docker-compose -f $DOCKER_COMPOSE_FILENAME --env-file .env -p $PROJECT_NAME build
    	docker-compose -f $DOCKER_COMPOSE_FILENAME --env-file .env -p $PROJECT_NAME up -d
else  
     docker-compose -f $DOCKER_COMPOSE_FILENAME -p $PROJECT_NAME down
fi
