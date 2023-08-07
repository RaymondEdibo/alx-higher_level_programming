#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks cycle in sll
 * @list: input
 * Return: 0 or 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *i;

	if (!list)
	{
		return (0);
	}

	while (list)
	{
		i = list;
		list = list->next;

		if (i <= list)
		{
			return (1);
		}
	}
	return (0);
}
