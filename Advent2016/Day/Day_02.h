#pragma once
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

namespace Day_02 {

	enum ValidationPolicy {
		Square,		// coordinates cannot exceed the borders
		Distance	// sum of coordinates cannot be bigger than X
	};

	class KeypadPos {
	public:
		void GoLeft();
		void GoRight();
		void GoUp();
		void GoDown();

		const int& GetX() const;
		const int& GetY() const;

		void Initialize(int _x, int _y, ValidationPolicy _policy, int _keypadSize, int _xOffset = 0, int _yOffset = 0);
	private:
		void SavePosition();
		void RestoreLastValidPosition();
		void ValidatePos();
		bool VerifySquare();
		bool VerifyDistance();

		ValidationPolicy policy;
		int x;
		int y;
		int xOffset;
		int yOffset;
		int keypadSize;

		int lastValidX;
		int lastValidY;
	};

	class Keypad {
	public:
		KeypadPos position;

		Keypad();
		void Move(char direction); 
		void PrintKey();
	private:
		int keys[3][3] = { {1,2,3}, {4,5,6}, {7, 8, 9} };
	};

	class KeypadDiamond : public Keypad{
	public: 
		void PrintKey();
		KeypadDiamond();
	private:
		char keys[5][5] = {
			'-', '-', '1', '-', '-',
			'-', '2', '3', '4', '-',
			'5', '6', '7', '8', '9',
			'-', 'A', 'B', 'C', '-',
			'-', '-', 'D', '-', '-',
		};


	};

	class Day_02  {
	private:

		Keypad keypad;
		KeypadDiamond keypadDiamond;
		std::vector<std::string> keys;

	public:
		void ReadFile(std::string fileName);
		void Evaluate();
		Day_02();
		~Day_02();

	};
}
