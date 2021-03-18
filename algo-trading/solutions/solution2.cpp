/* Copyright 2021
** Justin Baum
*/

#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

vector<int> min_number_of_jumps(vector<int> &array) {
    int size = array.size();
    vector<int> jumps = vector<int>(size + 1, INT_MAX >> 1);
    jumps[size] = 0;
    for (int i = size; i >= 0; --i) {
        int forward = min(array[i], size - i);
        for (int j = 1; j <= forward; ++j) {
            if (jumps[i + j] + 1 < jumps[i]) {
                jumps[i] = jumps[i+j] + 1;
            }
        }
    }
    return jumps;
}

vector<string> to_names(vector<int> &min_jumps, vector<string> &names) {
    int size = min_jumps.size();
    int i = size - 1;
    names.insert(names.begin(), "");
    vector<string> order = {};
    while (i > 0) {
        if (min_jumps[i] < min_jumps[i-1]) {
            order.insert(order.begin(), names[i]);
            cout << "Name: " << names[i] << endl;
        }
        --i;
    }
    names.erase(names.begin());
    cout << names[0] << endl;
    order.insert(order.begin(), names[0]);
    unique(order.begin(), order.end());
    return order;
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
    auto x = min_number_of_jumps(array);
    for(int jump : x) {
        cout << jump << " ";
    }
    cout << endl;
    for (auto name : to_names(x, names)) cout << name << " ";
    cout << endl;
    return 0;
}
    

