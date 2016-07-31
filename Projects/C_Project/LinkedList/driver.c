// driver.c -- test the linked list
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "linked.h"

char menu();
void uppercase(char *ar);
void show(Item *pi);
void make_item(List *pl);
void remove_item(List *pl);
void get_num_places(List *pl);
void find(List *pl);


int main(void)
{
	List *places;

	places = (List *) malloc(sizeof(List));

	init_list(places);
	char choice;
//	puts("Enter your favorite")
	while((choice = menu()) != EOF)
	{
		switch(choice)
		{
			case 'a': 
				make_item(places); 
				break;
			case 'b':				
				remove_item(places);
				break;				
			case 'c':
				puts("Places you have on your list are:");
				show_places(places, show);
				break;
			case 'd':
				find(places);
				break;
			case 'e':
				get_num_places(places);
				break;
			case 'f':
				puts("Bye");
				empty_list(places);
				free(places);
				exit(0);
		}
	}
	
	if(empty_list(places));
	{
		puts("Successfully emptied the list and recovered memory");
		free(places);
		exit(0);
	}

	fprintf(stderr, "Unable to empty the list\n");
	exit(1);
}

char menu()
{
	char ch;

	printf("Select from the following options\n"
		   "a) Add a place 			b) Remove a place\n"
		   "c) show places			d) Search for a place\n"
		   "e) Number of places        f)To quit\n");
	
	LABEL:
	ch = getchar();
	fflush(stdin);
	ch = tolower(ch);

	if(strchr("abcdef", ch) == NULL)
	{
		puts("Please enter a, b, c, d, e, or f");		
		goto LABEL;
	}

	if(ch == 'f')
		ch = EOF;

	return ch;
}

void uppercase(char *ar)
{
	while(*ar)
	{
		*ar = toupper(*ar);
		ar++;
	}
}


void show(Item *pi)
{
	printf("%s\n", pi->place);
}

void make_item(List *pl)
{
	Item *pi;
	if(is_full(pl))
		return;

	pi = (Item *)malloc(sizeof(Item));

	printf("Enter name of place to add:");
	fgets(pi->place,LEN,stdin);

	uppercase((pi->place));
	add_item(pi, pl);
	
	return;
}

void remove_item(List *pl)
{
	Item item;
	printf("Enter name of place to add:");
	fgets(item.place,LEN,stdin);

	uppercase((item.place));
	if(delete_item(&item, pl))
		printf("%s was Successfully removed\n", item.place);
	else
		puts("Operation failed");
}

void get_num_places(List *pl)
{
	unsigned int num = lsize(pl);
	printf("Number of places you've entered: %d\n", num);
}

void find(List *pl)
{
	Item item;
	printf("Enter name of place you want to find:");
	fgets(item.place,LEN,stdin);

	uppercase((item.place));
	if(search_list(&item, pl))
		printf("%s is in the list\n", item.place);
	else
		printf("%s was not found\n", item.place);
}