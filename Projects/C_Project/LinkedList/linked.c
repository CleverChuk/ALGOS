#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include "linked.h"

typedef struct pair
{
	Node *parent;
	Node *child;
}Pair;

static bool seek_item(Item *pi, List *pl);
static Pair get_node(Item *pi, List *pl);

bool init_list(List *pl)
{
	pl->root = NULL; // sets root node to empty
	pl->size = 0;
}

bool add_item(Item *pi, List *pl)
{

	Node *new_node;
	new_node = (Node *) malloc(sizeof(Node));

	if(is_full(pl))
	{
		fprintf(stderr, "Trying to add item to a full list\n");
		return false;
	}

	if(new_node != NULL)
		if(pl->root == NULL)
		{
			new_node->item = *pi;
			new_node->Nnode = NULL;
			pl->root = new_node;
			pl->size++;

			return true;
		}
		else
		{			
			
			new_node->item = *pi;
			new_node->Nnode = NULL;
			add_node(new_node, pl);
			pl->size++;

			return true;
		}

	return false;
}


bool search_list(Item *pi, List *pl )
{
	if(is_empty(pl))
	{
		fprintf(stderr, "Trying to search an empty list\n");
		return false;
	}

	Node *temp;

	for(temp = pl->root; temp != NULL; temp = temp->Nnode)
	{
		if((strcmp(pi->place, (temp->item).place)) == 0)
			return true;
	}

	return false;
}


bool delete_item(Item *pi, List *pl)
{// MIGHT WORK
	Pair found;

	if(seek_item(pi, pl))
	{
		found = get_node(pi, pl);
		found.parent = (found.child)->Nnode;
		free(found.child);
		pl->size--;
		return true;		 
	}

	return false;
}


bool is_full(List *pl)
{
	Node *new_node;

	new_node = (Node *) malloc(sizeof(Node));

	if(new_node == NULL)
		return true;

	free(new_node);

	return false;
}

bool is_empty(List *pl)
{
	if(pl->root == NULL)
		return true;

	return false;
}

unsigned int lsize(List *pl)
{
	return pl->size;
}

bool replace_item(Item *i1, Item *i2, List *pl)
{
	if(is_empty(pl))
	{
		fprintf(stderr, "Attempted to access an empty list\n");
		return false;
	}

	if(seek_item(i1, pl))
	{
		strncpy(i1->place, i2->place, LEN);
		return true;
	}

	return false;
}


bool empty_list(List *pl)
{
	Node *temp;

	if(!is_empty(pl))
	{
		while(pl->root)
		{
			temp = pl->root->Nnode;
			free(pl->root);
			pl->root = temp;
		}
		pl->size = 0;
		return true;
	}

	return false;
}

void add_node(Node *pnode, List *pl)
{
	Node *temp = pl->root;
	while(temp->Nnode != NULL)
		temp = temp->Nnode;

	temp->Nnode = pnode;
}



void show_places(List *pl, void(*pfun)(Item *pi))
{
	Node *temp;
	if(is_empty(pl))
		return;
	for(temp = pl->root; temp != NULL; temp = temp->Nnode)
	{
		if(temp != NULL)
			pfun(&(temp->item));
	}
}


static bool seek_item(Item *pi, List *pl)
{
	Node *temp;

	if(search_list(pi, pl))
		for(temp = pl->root; temp != NULL; temp = temp->Nnode)
		{
			if((strcmp(pi->place, (temp->item).place) == 0))
			{
				pi = &(temp->item);
				return true;
			}
		}
	puts("Item not in List");

	return false;
}

static Pair get_node(Item *pi, List *pl)
{
	Pair find;
	find.parent = NULL;
	find.child = pl->root;

	if(search_list(pi, pl))
		for( ; find.child != NULL; find.child = find.child->Nnode)
		{
			if((strcmp(pi->place, (find.child->item).place) == 0))
				return find;			

			find.parent = find.child;
		}

	return find;
}