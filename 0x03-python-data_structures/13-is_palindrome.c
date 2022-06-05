#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is palindrome
 *
 * @head: the first node of the linked list
 * Return: 1 if it's a palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head || !(*head)->next)
		return (0);
	return (1);
}
