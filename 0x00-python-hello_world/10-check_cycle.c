#include "lists.h"
/**
 * check_cycle -checks if there is a cycle in a linked list
 * @list: singly linked list
 * Return: integer
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *speed = list;

	while (current != NULL && speed != NULL && speed->next != NULL)
	{
		speed = speed->next->next;
		current = current->next;
		
		if (speed == current)
			return (1);
	}
	return (0);
}
