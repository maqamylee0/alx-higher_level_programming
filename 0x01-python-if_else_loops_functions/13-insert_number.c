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

	if (!head)
		return (NULL);
	current = *head;
	before = NULL;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	while(current)
	{
		if(current->n <= number)
		{
			before = current;
			current = current->next;
		}
		else
		{
			if(before)
			{
				before->next = new;
				new->next = current;
				return (new);
			}
			else
			{
				*head = new;
				return (new);
			}
		}
	}
	before->next = new;
	new->next = NULL;
	return (new);
}
