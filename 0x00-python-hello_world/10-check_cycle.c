#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks cycle in sll
 * @list: input
 * Return: 0 or 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *i =  list;
	listint_t *j = list;

	if (list == NULL)
		exit(0);
	while (1)
	{
		if (i == NULL)
			return (0);
		i = i->next;
		j = j->next->next;
		if (i->next == NULL || j->next->next == NULL)
			return (0);
		else if  (i->next == j->next->next)
			return (1);
	}
}
