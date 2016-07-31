#ifndef _LINKED_H
#define _LINKED_H
#define LEN 25
#include <stdbool.h>

typedef struct item
{
	char place[LEN];
}Item;

typedef struct node
{
	Item item;
	struct node *Nnode;
}Node;

typedef struct list
{
	Node *root;
	unsigned int size;
}List;

bool init_list(List *pl);
bool add_item(Item *pi, List *pl);
bool search_list(Item *pi, List *pl );
bool delete_item(Item *pi, List *pl);
bool is_full(List *pl);
bool is_empty(List *pl);
unsigned int lsize(List *pl);
bool replace_item(Item *i1, Item *i2, List *pl);
bool empty_list(List *plist);
void add_node(Node * pnode, List *pl);
void show_places(List *pl, void(*pfun)(Item *pi));

#endif