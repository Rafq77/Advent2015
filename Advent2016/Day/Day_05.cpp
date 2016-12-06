#include "stdafx.h"
#include "Day_05.h"

	const char* Day_05::Day_05::input = "ugkcyxxp";
	//std::string abc("abc5017308");
	//std::string abc2("abc3231929");

Day_05::Day_05::Day_05() 
{
};

Day_05::Day_05::~Day_05() {
};

void Day_05::Day_05::Evaluate() {
	unsigned char digest[16];
	t1 << std::hex;
	t2 << std::hex;
	MD5_CTX hash;

	unsigned long int i = 0;
	int idx = 0, tabIdx;
	bool done = false;
	std::stringstream ss;
	std::string tmp;
	std::string out("--------");
	tmp.reserve(16);

#pragma omp parallel num_threads(8) private(tmp, hash, digest, tabIdx)
	while (done == false) {
		tmp = input + std::to_string(++i);
		MD5_Init(&hash);
		MD5_Update(&hash, tmp.c_str(), tmp.size());
		MD5_Final(digest, &hash);

		if (digest[0] == 0x00
			&& digest[1] == 0x00
			&& (digest[2] & 0xF0) == 0x00) {

				if (idx < 8) {
					//std::cout << std::hex << (digest[2] & 0x0F);
					t1 << (digest[2] & 0x0F);
				}

#pragma omp atomic
				++idx;

				tabIdx = ((digest[2] & 0x0F));
				//std::cout << i << "\t" << tabIdx << "\t" << out << std::endl;
				if (tabIdx < 8 && tabIdx >= 0 && out[tabIdx] == '-') {
					out[tabIdx] = (digest[3] & 0xF0) >> 4;
					t2 << (unsigned int)((digest[3] & 0xF0) >> 4);
				}
		}

		if (idx >= 8) {
			if (out.find('-') == std::string::npos) {
				done = true;
				break;
			}
		}
	}

	Print();
}


void Day_05::Day_05::Print() {
	std::cout << "Day 05  task1: " << t1.str() << " task2: " << t2.str() << std::endl;
}
