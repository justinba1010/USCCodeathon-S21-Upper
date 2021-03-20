/* Copyright 2021
** Justin Baum
** MIT License
*/

#include <vector>
#include <iostream>
#include <string>
#include <climits>
using namespace std;

long maxInversions(vector<int> arr) {
    // Dynamic
    // Naive is O(n^3)
    // Optimal must be O(n^2) as this is doable with memoization
    int n = arr.size();
    long count = 0;
    if (n == 0) return 0;
    for (int i = 0; i < n - 2; ++i) {
        for (int j = i + 1; j < n - 1; ++j) {
            for (int k = j + 1; k < n; ++k) {
                count += (arr[i] > arr[j]) && (arr[j] > arr[k]);
            }
        }
    }
    return count;
}

int main(void) {
    int n;
    cin >> n;
    vector<int> array;
    for(int _ = 0; _ < n; ++_) {
        int x;
        cin >> x;
        array.push_back(x);
    }
    cout << maxInversions(array) << endl;
    return 0;
}
