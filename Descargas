#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main( int argc, char* argv[])
{
	printf("Inicio\n");
	if( fork()==0)
		printf("Hola\n");

	if( fork()==0)
		printf("Hola\n");
	else
		printf("Adios\n");

	exit(0);
}
