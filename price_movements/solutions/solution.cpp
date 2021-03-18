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
    if (n == 0) return 0;
    // dynamic[i][j] = max(dynamic[i-1][j], )
    vector<int> lefts = vector<int>(n, 0);
    vector<int> rights = vector<int>(n, 0);
    for (int i = 1; i < n - 1; ++i) {
        for (int j = i - 1; j >= 0; --j) {
            lefts[i] += (arr[j] > arr[i]);
        }
        for (int j = i + 1; j < n; ++j) {
            rights[i] += (arr[i] > arr[j]);
        }
    }
    long count = 0;
    for (int i = 1; i < n - 1; ++i) {
        // This is the number of combos possible
        count += lefts[i] * rights[i]; 
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
