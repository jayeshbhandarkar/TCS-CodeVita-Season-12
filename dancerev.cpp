#include <iostream>
#include <vector>
#include <string>
#include <climits> // For INT_MAX

using namespace std;

// Function to calculate the minimum leg movements
int minMoves(int n, const vector<string>& instructions) {
    vector<string> tiles = {"up", "down", "left", "right"};
    int min_moves = INT_MAX;

    // Try all combinations of initial positions for the two legs
    for (const string& start_left : tiles) {
        for (const string& start_right : tiles) {
            if (start_left == start_right) continue; // Legs can't start on the same tile

            int moves = 0;
            string left = start_left, right = start_right;

            for (const string& instruction : instructions) {
                // If the instruction matches one of the leg positions, no move needed
                if (instruction == left || instruction == right) {
                    continue;
                }

                // Move the leg closer to the instruction
                if (left == instruction || right == instruction) {
                    continue;
                } else if (left != instruction) {
                    left = instruction;
                } else {
                    right = instruction;
                }
                moves++;
            }

            // Update the minimum moves
            min_moves = min(min_moves, moves);
        }
    }

    return min_moves;
}

int main() {
    int n;
    cin >> n;
    vector<string> instructions(n);
    for (int i = 0; i < n; ++i) {
        cin >> instructions[i];
    }

    // Output the result without any extra spaces or newlines
    cout << minMoves(n, instructions);
    return 0;
}