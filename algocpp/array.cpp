#include "array.hpp"

template<typename T>
Array<T>::Array(uint lenght_p)
{
	lenght_v = lenght_p;
	for(size_t i = 0; i < lenght_v; i++)
	{
		arr[i] = (T)0;
	}
}

template<typename T>
void Array<T>::print()
{
	for(size_t i = 0; i < lenght_v; i++)
	{
		algo::print('[');
		algo::print(arr[i]);
		algo::print(']');
	}
}