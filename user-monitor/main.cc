#include <libevdev/libevdev.h>
//#include <libudev/libudev.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <ctime>
#include <fstream>
#include <cstdint>
#include <mutex>
#include <thread>
#include <chrono>

#define FLUSH_TICKS 50
#define EVENT_INTERVAL 50
#define nl '\n'
#define newline cout << nl;

using namespace std;
mutex mtx;
vector<int> occ;

string get_time()
{
	time_t result = time(nullptr);
	string unix_time = asctime(localtime(&result));
	return unix_time;
}

void read_csv(string filename)
{
	vector<pair<int, int>> data;
    ifstream file(filename);

    if (!file.is_open()) {
        cerr << "Error: Cannot open file " << filename << "\n";
        return;
    }

	int maxkey = 0;
    string line;
	getline(file, line);
    while (getline(file, line)) {
        pair<int, int> row;
        stringstream ss(line);
        string cell;

        if (getline(ss, cell, ',')) {
            row.first = stoi(cell);
        }
        if (getline(ss, cell)) {
            row.second = stoi(cell);
        }
		maxkey = max(maxkey, row.first);

        data.push_back(row);
    }
	occ.resize(maxkey + 1, 0);
	cout << " Max key: " << maxkey << nl;
	for(auto& p : data){
		cout << p.first << " " << p.second << nl;
		occ[p.first] = p.second;
	}

    file.close();
}

void dump_to_csv(string& filename)
{
	ofstream f;
	f.open(filename);
	f << "key,count" << nl;
	for(int i = 0; i < occ.size(); i++){
		if(occ[i] > 0){
			f << i << "," << occ[i] << nl;
		}
	}
	f.close();
}

void print_occ()
{
	for(int i = 0; i < occ.size(); i++){
		if(occ[i] >= 0){
			cout << i << ": " << occ[i] << " ";
		}
	}
	cout << "\n";
}

void capture(struct libevdev* dev)
{
	struct input_event ev;
    while (true) {
        int rc = libevdev_next_event(dev, LIBEVDEV_READ_FLAG_NORMAL, &ev);
        if (rc == 0 && ev.type == EV_KEY) {
            if (ev.value == 1) { // key press
                // printf("Key %d pressed\n", ev.code);
				cout << "ev code: " << ev.code << nl;
				lock_guard<mutex> lock(mtx);
				if(ev.code >= occ.size()){
					occ.resize(ev.code + 1);
				}
				occ[ev.code]++;
            }
        }

		this_thread::sleep_for(std::chrono::milliseconds(EVENT_INTERVAL));
    }
}

void exporter(string filename)
{
    while (true) {
        this_thread::sleep_for(chrono::seconds(5));
        lock_guard<mutex> lock(mtx);
		print_occ();
        dump_to_csv(filename);
    }
}

int main() {

	string csv_filename = "data/keystrokes.csv";
	read_csv(csv_filename);
	cout << "Occ size: " << occ.size() << nl;

    struct libevdev *dev = NULL;
	// find the usb keyboard environment variable 

	const char* keyboard = getenv("KEYBOARD");
	if (keyboard == NULL){
		cout << "USB Keyboard not found." << nl;
		exit(1);
	} 
	string input_path = "/dev/input/";

    int fd = open((input_path + keyboard).c_str(), O_RDONLY | O_NONBLOCK); // Change this to your keyboard device
    if (fd < 0) {
        perror("Failed to open device");
        return 1;
    }

    if (libevdev_new_from_fd(fd, &dev) < 0) {
        fprintf(stderr, "Failed to init libevdev\n");
        return 1;
    }

    printf("Input device name: \"%s\"\n", libevdev_get_name(dev));
    printf("Recording keystrokes...\n");

	thread _capture(capture, dev);
	thread _exporter(exporter, csv_filename);
	_capture.join();
	_exporter.join();

    libevdev_free(dev);
    close(fd);

    return 0;
}

