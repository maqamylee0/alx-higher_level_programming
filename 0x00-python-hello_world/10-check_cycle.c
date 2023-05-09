#include "lists.h"
/**
 * check_cycle -checks if there is a cycle in a linked list
 * @list: singly linked list
 * Return: integer
 */
int check_cycle(listint_t *list)
{
	const listint_t *current;

	current = list;
	while (current != NULL)
	{
		if (current->next != list && current->next != current)
			current = current->next;
		else
			return (1);
	}
	return (0);
}
