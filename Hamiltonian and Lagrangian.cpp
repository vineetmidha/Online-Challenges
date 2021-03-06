
Problem: Hamiltonian and Lagrangian @ Hacker Earth

https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/description/

#include <iostream>

using namespace std;

void get_answer(int marks[], int n);

int main()
{
	int n;

	cin >> n;

	int marks[n];

	for (int i = 0; i < n; ++i)
	{
		cin >> marks[i];
	}

	get_answer(marks, n);
}

void get_answer(int marks[], int n)
{
	int count = 0;

	for (int i = 0; i < n; ++i)
	{
		int flag = 1;

		int max = marks[i];

		for (int j = i + 1; j < n; ++j)
		{
			if (marks[j] > max)
			{
				flag = 0;
				break;
			}
		}

		if (flag)
			cout << marks[i] << " ";
	}
}
