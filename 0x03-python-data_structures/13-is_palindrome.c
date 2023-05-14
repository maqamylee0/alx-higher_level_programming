#include "lists.h"
/**
 * reverse_list- revwerses linked list
 * @head: double pointer to list
 * Return: pointer to head
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current, *before, *next;

	if (*head == NULL)
		return (NULL);
	if ((*head)->next == NULL)
		return (*head);

	current = *head;
	before = NULL;
	next = NULL;

	while (current != NULL && current->next != NULL)
	{
		next = current->next;
		current->next = before;
		before = current;
		current = next;
	}
	*head = before;
	return (*head);

}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of listInvalid read of size 8
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *front, *front2;
	listint_t **head2 = NULL, *head3 = NULL;

	if (*head == NULL)
		return (1);
	head2 = malloc(sizeof(listint_t));
	if (!(*head2))
		return (0);
	(*head2)->n = (*head)->n;
	(*head2)->next = NULL;
	front = *head;
	while (front != NULL)
	{
		add_nodeint_end(head2, front->n);
		front = front->next;
	}
	head3 = reverse_list(head2);
	front2 = head3;
	while (front != NULL && front2 != NULL)
	{
		if (front->n != front2->n)
		{
			free_listint(*head2);
			free_listint(head3);
			return (0);
		}
		if (front->next != NULL)
		{
			front = front->next;
			front2 = front2->next;
		}
		else
		{
			free_listint(*head2);
			free_listint(head3);
			return (0);
		}
	}
	free_listint(*head2);
	free_listint(head3);
	return (1);
}
