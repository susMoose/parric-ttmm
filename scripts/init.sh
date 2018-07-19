# make sure docker client is logged into docker hub with 'docker login'
# as written, must run this from the scripts/ directory (or wherever master.sh and slave.sh live)

if [[ -n $(docker ps -q) ]]
then
	printf "INFO : Stopping containers...\n"
	docker stop $(docker ps -q)
	printf "INFO : ...done.\n\n"
fi

if [[ -n $(docker ps -aq) ]]
then
	printf "INFO : Removing containers...\n"
	docker rm $(docker ps -aq)
	printf "INFO : ...done.\n\n"
fi

printf "INFO : Invoking 'master.sh'...\n"
./master.sh
printf "INFO : ...done.\n\n"

printf "INFO : Sleeping for 30 seconds to let 'jenkins' initialize..."
sleep 30
printf "done.\n\n"

printf "INFO : Invoking 'slave.sh'...\n"
# This slave secret '85a3ba...' may not work.
# If you get an error, then invoke master.sh first.
# Then log into the jenkins web portal, and get the node secret from settings.
# Then pass that new node secret to slave.sh.
./slave.sh 85a3ba331969f0afe8a821e6441992866887d7cc97e257a48dbaa85ef71b7e61
printf "INFO : ...done.\n\n"
