#include "base.hpp"

#define MAX_ARRAY 1000


template<typename T>
class Array
{
	public:
		Array(uint lenght_p);
		T& operator[](uint i);
		uint lenght();
		void print();
	private:
		T arr[MAX_ARRAY];
		uint lenght_v;
};