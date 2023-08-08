#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_i - insert node
* @head: head of list
* @number: number
* Return:  i address
*/
listint_t *insert_i(listint_t **head, int number)
{
	listint_t *i;
	listint_t *j;

	j = malloc(sizeof(listint_t));
	if (!head || !(*head))
	{
		j->n = number;
		j->next = NULL;
		*head = j;
		return (j);
	}
	i = *head;
	if (!j)
	{
		free(j);
		return (NULL);
	}
	if (number <= i->n)
	{
		j->n = number;
		j->next = i;
		i = j->next;
		*head = j;
		return (j);
	}
	while (i)
	{
		if (!i->next)
			return (add_iint_end(head, number));
		if ((number > i->n) && (number <= (i->next)->n))
		{
			j->n = number;
			j->next = i->next;
			i->next = j;
			return (j);
		}
		i = i->next;
	}
	free(j);
	return (NULL);
}
