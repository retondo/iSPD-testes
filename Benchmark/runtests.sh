#!/bin/bash

TASKS=(20 40 60 80 100 140 200)

for (( INDEX = 0; INDEX < 7; INDEX++ )); do
	echo -e "Iniciando testes de "${TASKS[INDEX]}" tarefas.\n"
	for (( COUNTER = 0; COUNTER < 20; COUNTER++ )); do
		echo "python3.5 client.py "${TASKS[INDEX]}
		python3.5 client.py ${TASKS[INDEX]}
	done
done