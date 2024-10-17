# Data Sorting Algorithms Visualizer

This project is a Python-based visualizer for data sorting algorithms using the `pygame` library. It provides an interactive way to observe and understand how different sorting algorithms work by visualizing their sorting processes step by step.

## Features

- **Sorting Algorithms**: 
  - **Bubble Sort**: Visualizes the classic Bubble Sort algorithm.
  - **Insertion Sort**: Visualizes the Insertion Sort algorithm.
  - **Merge Sort**: Planned feature (to be implemented).
- **Array Generation**:
  - Generate random arrays.
  - Generate pre-sorted arrays.
  - Generate reversed arrays.
- **Visualization**:
  - Sorting steps are shown in real-time with colored bars representing data.
  - Animations highlight the sorting progress and completion.
- **Interactivity**: 
  - Choose between different sorting algorithms.
  - Generate new datasets to be sorted.
  - Replay the sorting process on demand.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SamyDnx/sorting-algorithms-visualizer.git
   cd sorting-algorithms-visualizer
   ```

2. **Install Dependencies**:
   This project requires Python 3.x and the `pygame` library.
   You can install `pygame` using pip:
   ```bash
   pip install pygame
   ```

## How to Run

1. After installing the dependencies, run the `main.py` file:
   ```bash
   python main.py
   ```

2. Use the controls below to interact with the visualization.

## Controls

- **`SPACE`**: Start the sorting visualization for the selected algorithm.
- **`R`**: Generate a new random array.
- **`ENTER`**: Generate a pre-sorted array.
- **`BACKSPACE`**: Generate a reversed array.
- **`B`**: Select Bubble Sort as the sorting algorithm.
- **`I`**: Select Insertion Sort as the sorting algorithm.
- **`M`**: Select Merge Sort (not yet implemented).
  
## Sorting Algorithms

- **Bubble Sort**: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
  ```python
  def draw_bubble_sort(array):
      ...
  ```

- **Insertion Sort**: A simple comparison-based algorithm that builds the sorted array one element at a time by repeatedly picking the next element and inserting it into its correct position.
  ```python
  def draw_insertion_sort(array):
      ...
  ```

- **Merge Sort** (planned): A divide-and-conquer algorithm that divides the list into halves, recursively sorts each half, and then merges them back together.
  ```python
  def draw_merge_sort(array, l, r):
      ...
  ```

## Code Overview

- **Visualization**: Sorting is visualized using colored bars, where each bar represents a number in the array. The height of the bar corresponds to the value of the number.

- **Array Generators**:
  - **Random Array**: Generates an array of random integers.
  - **Sorted Array**: Generates an array sorted in ascending order.
  - **Reversed Array**: Generates an array sorted in descending order.

  ```python
  def generate_random_array():
      ...
  def generate_sorted_array():
      ...
  def generate_reversed_array():
      ...
  ```

- **Sorting Animations**:
  Sorting algorithms are visualized in real-time using `pygame`’s rendering capabilities.
  
  ```python
  def show_sorting_data(array, sort="b"):
      ...
  ```

## Future Improvements

- **Merge Sort**: Implement the merge sort algorithm for visualization.
- **More Sorting Algorithms**: Add support for algorithms like Quick Sort, Heap Sort, and others.
- **Customization**: Allow users to change array size, delay between steps, and color schemes.

## Acknowledgements

This project was built using the `pygame` library and classic sorting algorithms.

---

Feel free to experiment with the code and try implementing additional sorting algorithms or visual effects!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
