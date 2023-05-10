#include "lists.h"

/**
 * insert_node- insert node
 * @head: double pointer to start
 * @n: number
 * Return: pointer to inserted node
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *before;

	current = *head;
	before = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	while(current && current->next)
	{
		if(current->n <= number)
		{
			before = current;
			current = current->next;
		}
		else
		{
			before->next = new;
			new->next = current;
			return (new);
		}
	}
	return (NULL);
}
