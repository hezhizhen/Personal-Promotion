#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

class PrimeNumberGenerator
{
	const static int MAX_NUM = 32000;
	int PRIMES[MAX_NUM];
	int segPrimes[100000];
public:
	PrimeNumberGenerator()
	{
		memset(PRIMES, 0, sizeof(PRIMES));
		int j = 0;
		for (int i = 2; i < MAX_NUM; i++)
		{
			if (!PRIMES[i])
			{
				PRIMES[j++] = i;
				for (int k = i*2; k < MAX_NUM; k+=i)//不是k++注意
				{//写成 k = i+1，头痛错误!!!
					PRIMES[k] = 1;
				}
			}
		}
		PRIMES[j++] = MAX_NUM;
	}

	//本题不需使用的函数
	bool isPrimeNum(int num)
	{
		if (2 == num) return true;
		int i = 0;
		for ( ; PRIMES[i] * PRIMES[i] <= num && num % PRIMES[i]; i++);
		return MAX_NUM != PRIMES[i] && num % PRIMES[i] != 0;
	}

    	void getSegPrimes(int a, int b)
    	{
    		memset(segPrimes, 0, sizeof(segPrimes));//每一次都需要memset
    		for (int i = 0; PRIMES[i]*PRIMES[i] <= b; i++)//错误写成i <= b-a
    		{
    			int am = a/PRIMES[i];
    			for (int d = am; d * PRIMES[i] <= b; d++)
    			{
    				if (d > 1 && d * PRIMES[i] >= a) segPrimes[d*PRIMES[i]-a] = 1;
    			}//这里不能少了判断条件d>1
    		}
    	}

    	void judgePrimes()
    	{
    		int a = 0, b = 0;
    		int T = 0;
    		cin>>T;
    		while (T--)
    		{
    			cin>>a>>b;
    			if (a < 2) a = 2;
    			getSegPrimes(a, b);
    			for (int i = a ;  i <= b; i++)
    			{
    				if (0 == segPrimes[i-a]) cout<<i<<endl;
    			}
    			cout<<endl;
    		}
    	}
    };

    int main()
    {
    	PrimeNumberGenerator pri;
    	pri.judgePrimes();
    	return 0;
    }
