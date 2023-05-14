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

	while (current != NULL)
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
	size_t nodes = 0, counter = 1, half = 0;

	if (*head == NULL)
		return (1);
	front = *head;
	while (front != NULL)
	{
		nodes++;
		front = front->next;
	}
	if (nodes == 1)
		return (1);
	half = nodes / 2;
	if (nodes % 2 != 0)
	{
		half = half++;
	}
	front = *head;
	while (counter != half)
	{
		counter++;
		front = front->next;
	}
	front2 = reverse_list(&front->next);
	front = *head;
	while (front2 != NULL)
	{
		if (front->n != front2->n)
			return (0);
		front = front->next;
		front2 = front2->next;
	}
	return (1);
}
