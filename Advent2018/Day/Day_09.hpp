#pragma once
#include "./Day.hpp"

namespace game
{
	class Node
	{
	public:
		Node(int i)
		{
			nxt = nullptr;
			prv = nullptr;
			val = i;
		}

		int val;
		Node* nxt;
		Node* prv;
	};

	int remove(Node* beg)
	{
		Node* cur = beg;
		int val;
		cur->prv->nxt = cur->nxt;
		cur->nxt->prv = cur->prv;

		val = cur->val;

		delete cur;
		return val;
	}

	Node* insert(Node* cur, int val)
	{
		auto last = cur->prv;
		auto tmp = cur;
		cur = new Node(val);
		cur->nxt = tmp;
		cur->prv = last;
		last->nxt = cur;
		tmp->prv = cur;
		return cur;
	}

	Node* insertAfter(Node* cur, int val)
	{
		auto future = cur->nxt;
		auto tmp = cur;
		cur = new Node(val);
		cur->nxt = future;
		cur->prv = tmp;
		future->prv = cur;
		tmp->nxt = cur;

		return cur;
	}

	void print(Node* beg, int i)
	{
		for (int j = 0; j < i; ++j)
		{
			std::cout << beg->val << ' ';
			beg = beg->nxt;
		}
		//std::cout << beg->val << '\n';
		std::cout << '\n';
	}

	long long game(int playerNo, int highNo)
	{
		//int idx = 1;
		int player = 1;
		const int joker = 23;
		std::vector<long long> scores;
		scores.resize(playerNo);
		for (auto each : scores)
		{
			each = 0;
		}

		Node* begin = new Node(0);
		begin->nxt = begin;
		begin->prv = begin;
		Node* cur = begin;
		Node* end = begin;

		cur = insertAfter(cur, 1);
		player += 1;

		for (int i = 2; i < highNo + 1; ++i)
		{
			if (i % 1000000 == 0)
			{
				std::cout << i << '\n';
			}

			if (i % joker == 0)
			{
				for (int i = 0; i < 7; ++i)
				{
					cur = cur->prv;
				}

				auto tmp = cur->nxt;
				scores[player - 1] += i + remove(cur);
				cur = tmp;
			} else 
			{
				cur = cur->nxt->nxt;
				cur = insert(cur, i);
			}
			player = (player % playerNo == 0) ? 1 : player + 1;
		}
		long long val = *std::max_element(scores.begin(), scores.end());
		return val;
	}
}
class Day_09 : public Day
{
public:

	Day_09()
	{
	}

	~Day_09()
	{
	}

	void solve()
	{
		std::cout << "test  " << game::game(9, 26) << '\n';
		std::cout << "test  " << game::game(10, 1618) << '\n';
		std::cout << "test  " << game::game(13, 7999) << '\n';
		std::cout << "test  " << game::game(17, 1104) << '\n';
		std::cout << "test  " << game::game(21, 6111) << '\n';
		std::cout << "test  " << game::game(30, 5807) << '\n';
		std::cout << "live 1 " << game::game(476, 71657) << '\n';
		std::cout << "live 2 " << game::game(476, 7165700) << '\n';
	}
};

