/* Copyright 2021
** Justin Baum
** MIT License
** AlgoExpert Solutions
*/



// Start of HEAD
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#ifdef __APPLE__
    #include <json/json.h>
#else
    #include <json/json.h>
#endif

using namespace std;
using namespace Json;

class TestStruct {
public:
    size_t testcase_id;
    string testcase_input_path;
    string testcase_output_path;
    string testcase_expected_output_path;
    string testcase_error_path;
    vector<string> metadata_file_paths;
    string submission_code_path;
    string submission_language;
    bool testcase_result;
    size_t testcase_signal;
    float testcase_time;
    size_t testcase_memory;
    string data;
};

class ResultStruct {
public:
    bool   result;
    float  score;
    string message;
};
// End of HEAD
        


// Start of BODY
/**
 * TestStruct members::
 *  testcase_id                   [size_t] ID of the test-case
 *  testcase_input_path           [string] File path to test-case input
 *  testcase_output_path          [string] File path to test-case output generated by the problem solver
 *  testcase_expected_output_path [string] File path to test-case expected output to be matched with
 *  testcase_error_path           [string] File path to test-case STDERR
 *  metadata_file_paths           [vector<string>] File paths to Question metadata (Extra files usually used for defining traning sets)
 *  submission_code_path          [string] File path to submission source code
 *  submission_language           [string] Language token of submission
 *  testcase_result               [bool] Set to true if test-case output matches test-case expected output. Matching is done line by line
 *  testcase_signal               [size_t] Exit code of the test-case process
 *  testcase_time                 [float] Time taken by the test-case process in seconds
 *  testcase_memory               [size_t] Peak memory of the test-case process determined in bytes
 *  data                          [string] <Future use>
 *
 *
 *  ResultStruct::
 *    result      [bool]  Assign test-case result. true determines success. false determines failure
 *    score       [float] Assign test-case score. Normalized between 0 to 1
 *    message     [string] Assign test-case message. This message is visible to the problem solver
**/


void run_custom_checker(const TestStruct t_obj,
                        ResultStruct &r_obj) {
    //Don't print anything to STDOUT in this function
    //Enter your custom checker scoring logic here
    ifstream expected, output, input;
    map<string, int> indexOfMeme;
    vector<int> jumps;
    vector<string> memes;
    int n;
    input.open(t_obj.testcase_input_path);
    input >> n;
    for (int i = 0; i < n; ++i) {
        int x;
        input >> x;
        jumps.push_back(x);
    }
    for (int i = 0; i < n; ++i) {
        string m;
        input >> m;
        memes.push_back(m);
        indexOfMeme[m] = i;
    }
    
    expected.open(t_obj.testcase_expected_output_path);
    int answer = 0;
    string memethrow;
    while (expected >> memethrow) {
        ++answer;
    }
    
    output.open(t_obj.testcase_output_path);
    int index = 0;
    int count = 0;
    r_obj.message = "";
    string last = "";
    while (output >> memethrow) {
        ++count;
        auto x = indexOfMeme.find(memethrow);
        r_obj.message += memethrow;
        if (x == indexOfMeme.end()) {
            r_obj.result = false;
            r_obj.score = 0.0;
            r_obj.message += "You used an illegal meme.";
            return;
        }
        int jumpss = jumps[x->second];
        if (x->second > index + jumpss) {
            r_obj.result = false;
            r_obj.score = 0.0;
            r_obj.message = "You made an illegal jump.";
            return;
        }
        index = x->second + jumpss;
        last = memethrow;
    }
    if (last != memes[n-1]) {
        r_obj.result = false;
        r_obj.score = 0.0;
        r_obj.message = "You didn't jump land on the last meme.";
        return;
    }
    if (count > answer) {
        r_obj.result = false;
        r_obj.score = 0.0;
        r_obj.message = "You had too many jumps.";
        return;
    }
    if (index < n) {
        r_obj.result = false;
        r_obj.score = 0.0;
        r_obj.message = "Didn't make it to the end";
        return;
    }
    if (count < answer) {
        r_obj.result = false;
        r_obj.score = 0.0;
        r_obj.message = "IF YOU SEE THIS LET SOMEONE KNOW";
        return;
    }
    
    
    
    r_obj.result = true;
    r_obj.score = 1.0f;
    r_obj.message = "Success";
}
// End of BODY
               
 
// Start of TAIL
int read_input_json(const string json_file_path,
                    TestStruct &t_obj) {
    ifstream stream(json_file_path);
    string json_file_contents((std::istreambuf_iterator<char>(stream)),
                 std::istreambuf_iterator<char>());

    Value root;
    Reader reader;
    if(!reader.parse(json_file_contents, root, false))
        return 1;

    try {
        // Read values
        if(root.isMember("testcase_id"))
            t_obj.testcase_id = root["testcase_id"].asInt();
        if(root.isMember("input_file_path"))
            t_obj.testcase_input_path = root["input_file_path"].asString();
        if(root.isMember("output_file_path"))
            t_obj.testcase_output_path = root["output_file_path"].asString();
        if(root.isMember("expected_output_file_path"))
            t_obj.testcase_expected_output_path = root["expected_output_file_path"].asString();
        if(root.isMember("error_file_path"))
            t_obj.testcase_error_path = root["error_file_path"].asString();
        if(root.isMember("metadata_file_paths")) {
            Value metadata_file_path_node = root["metadata_file_paths"];
            if(metadata_file_path_node.isArray()) {
                for(int i = 0; i < (int)metadata_file_path_node.size(); i++) {
                    string metadata_file = metadata_file_path_node[i].asString();
                    t_obj.metadata_file_paths.push_back(metadata_file);
                }
            }
        }
        if(root.isMember("submission_code_path"))
            t_obj.submission_code_path = root["submission_code_path"].asString();
        if(root.isMember("submission_language"))
            t_obj.submission_language = root["submission_language"].asString();
        if(root.isMember("testcase_result"))
            t_obj.testcase_result = root["testcase_result"].asBool();
        if(root.isMember("testcase_signal"))
            t_obj.testcase_signal = root["testcase_signal"].asInt();
        if(root.isMember("testcase_time"))
            t_obj.testcase_time = root["testcase_time"].asFloat();
        if(root.isMember("testcase_memory"))
            t_obj.testcase_memory = root["testcase_memory"].asInt();
        if(root.isMember("data"))
            t_obj.data = root["data"].asString();
    }
    catch(const runtime_error& error) {
        return 1;
    }

    return 0;
}

void write_result_json(const ResultStruct r_obj) {
    Value root;
    root["custom_result"] = (int)r_obj.result;
    root["custom_score"] = max( ((r_obj.score > 1.0f)? 1.0f : r_obj.score), 0.0f);
    root["custom_message"] = (r_obj.message.size() > 4096)? r_obj.message.substr(0, 4095) : r_obj.message;
    cout << root.toStyledString() << endl;
}

int main(int argc, char** argv) {
    // Input parameters
    TestStruct t_obj;
    t_obj.testcase_id = 0;
    t_obj.testcase_signal = 0;
    t_obj.testcase_memory = 0;
    t_obj.testcase_time = 0.0f;
    t_obj.testcase_result = true;

    // Out parameters
    ResultStruct r_obj;
    r_obj.result = false;
    r_obj.score = 0.0f;
    r_obj.message = "Uninitialized";

    if(argc < 2) {
        write_result_json(r_obj);
        return 1;
    }

    // Decode input JSON
    int failure = read_input_json((string)argv[1],
                                    t_obj);
    // Incase input JSON was malformed or not existent
    if(failure) {
        r_obj.message = "Unable to read input json";
        write_result_json(r_obj);
        return 2;
    }

    // Run the custom checker evaluator
    run_custom_checker(t_obj, r_obj);

    // Encode result JSON
    write_result_json(r_obj);
    return 0;
}
// End of TAIL
