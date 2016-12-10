#include "Day_04.h"

	const char* Day_04::Day_04::key = "northpoleobjectstorage";

Day_04::Day_04::Day_04() :
	sectorSum(0)
{
};

Day_04::Day_04::~Day_04() {
};

void Day_04::Day_04::Evaluate() {
	for each (std::string doorname in words) {
		names.push_back(Doorname(doorname));
	}

	for each (Doorname name in names) {
		if (name.isReal()) {
			sectorSum += name.GetSectorId();
		}

		if (0 == name.Decipher().compare(key)) {
			secretRoomId = name.GetSectorId();
		}
	}
	Print();
}


void Day_04::Day_04::Print() {
	std::cout << "Day 04 Sector Sum: " << sectorSum << " room id: " << secretRoomId << std::endl;
}

Day_04::Doorname::Doorname(std::string fullname) {
	originalName = fullname;
	for (unsigned char i = 'a'; i <= 'z'; ++i) {
		commonElements.push_back(std::make_tuple(i, 0));
	}

	size_t checksumIdx = fullname.find('[') + 1;
	size_t sectorIdx = fullname.find_last_of('-') + 1;
	checksum = fullname.substr(checksumIdx, CHECKSUM_SIZE);
	sectorId = atol(fullname.substr(sectorIdx, checksumIdx - sectorIdx).c_str());
	letters = fullname.substr(0, sectorIdx-1);
	
	// using Erase-Remove Idiom, because remove adjusts only the pointers
	//std::remove(letters.begin(), letters.end(), '-');
	letters.erase(std::remove(letters.begin(), letters.end(), '-'), letters.end());
}

bool Day_04::Doorname::isReal() {

	for each (char letter in letters) {
		/* awww sweet, in below lambda, letter is being taken by reference, 
		 * and input param to the lambda is the tuple (with auto)
		 * inside std::get compares the char, thus the find_if returns iterator to the tuple
		 * line below, the second elem of tuple is incremented.
		*/
		auto it = std::find_if(commonElements.begin(), commonElements.end(), [&letter](auto && elem) { 
			return std::get<0>(elem) == letter; 
		});
		std::get<1>(*it)++;
	}

	std::sort(commonElements.begin(), commonElements.end(), [](auto &&a, auto &&b) {
		if (std::get<1>(a) == std::get<1>(b)) {
			return std::get<0>(a) < std::get<0>(b);
		} else {
			return std::get<1>(a) > std::get<1>(b);
		}
	});

	std::string out;
	out.resize(CHECKSUM_SIZE);
	std::transform(commonElements.begin(), commonElements.begin() + CHECKSUM_SIZE, out.begin(), [](auto && elem) {
		return std::get<0>(elem);
	});

	if (0 == out.compare(checksum)) {
		return true;
	} 

	return false;
}

std::string Day_04::Doorname::Decipher() {
	uint16_t mod = sectorId % 26;
	std::string out;
	out.resize(letters.size());

	std::transform(letters.begin(), letters.end(), out.begin(), [&mod](char & c) {
		return 97 + ((c - 97 + mod) % 26);
	});

	return out;
}
