#pragma once
#include "Day.h"
#include <vector>

namespace Day_02 {

	class Box {
	private:
		int w, h, l;
		int area;
		int littleExtra;

	public:
		Box() {
			w = h = l = 0;
			area = 0;
		}

		Box(int _w, int _h, int _l) {
			w = _w;
			h = _h;
			l = _l;
		}

		int Area() {
			area = (2 * l * w) + (2 * w * h) + (2 * h * l);
			return area;
		}

		int SmallestArea() {
			int c0 =  l*w;
			int c1 =  w*h;
			int c2 =  h*l;

			c0 = (c0 < c1) ? c0 : c1;
			return (c0 < c2) ? c0 : c2;
		}

		int Ribbon() {
			// lame sort
			int c0, c1;
			if (w < h) {
				c0 = w;
				c1 = (h < l) ? h : l;
			}
			else {
				c0 = h;
				c1 = (w < l) ? w : l;
			}

			int wrap = c0 + c0 + c1 + c1;
			int bow = w*h*l;
			return bow + wrap;
		}
	};

	class Day_02 : public Day {
	private:
		std::string input;
		std::vector<Box> presents;
		std::vector<std::string> presentsRaw;
		long totalWrapping;
		long totalRibbon;

		Box ParseString(std::string _word);
		void ReadFile();
	public:
		Day_02();
		~Day_02();

		// Inherited via Day
		virtual void DoMagic() override;
		virtual void PrintOutput() override;
	};
}
