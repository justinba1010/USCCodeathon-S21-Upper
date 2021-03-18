/* Copyright 2021
** Justin Baum
** MIT License
*/


#include <vector>
#include <iostream>
#include <string>
using namespace std;

typedef pair<int, vector<int> > pairy;
typedef vector<pairy> wow;

pairy min_number_of_jumps(vector<int> &array) {
    int size = array.size();
    wow jumps = vector<pairy>(size, pairy(INT_MAX >> 1, vector<int>(0)));
    jumps[size-1] = pairy(0, vector<int>());
    for (int i = size - 2; i >= 0; --i) {
        int forward = min(array[i], size - i - 1);
        for (int j = 1; j <= forward; ++j) {
            if (jumps[i + j].first + 1 < jumps[i].first) {
                jumps[i] = pairy(jumps[i + j].first + 1, jumps[i + j].second);
                jumps[i].second.insert(jumps[i].second.begin(), i);
            }
        }
    }
    return jumps[0];
}

int main(void) {
    int n;
    cin >> n;
    vector<int> array;
    vector<string> names;
    for(int _ = 0; _ < n; ++_) {
        int x;
        cin >> x;
        array.push_back(x);
    }
    for(int _ = 0; _ < n; ++_) {
        string x;
        cin >> x;
        names.push_back(x);
    }
    pairy x = min_number_of_jumps(array);
    //cout << x.first << endl;
    for(int jump : x.second) {
        cout << names[jump] << " ";
    }
    cout << names[n - 1];
    cout << endl;
    return 0;
}
