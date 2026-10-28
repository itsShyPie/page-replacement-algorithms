# Page replacement simulator: FIFO, LRU and Optimal

import random
import sys


def FIFO(frameSize, pages):
    frames = [-1] * frameSize
    frameIndex = 0
    pageFaults = 0

    # Iterate over each page in pages and check if it already in the frames array
    for page in pages:
        # print(frames)
        if page not in frames:
            # If not in frames add 1 to faults
            pageFaults += 1

            # Replace the oldest page in frames with the current page
            frames[frameIndex] = page
            frameIndex = (frameIndex + 1) % frameSize

    # Return number of page faults
    return pageFaults


def LRU(frameSize, pages):
    frames = []
    pageFaults = 0

    # Iterate over each page in pages and check if it already in the frames array
    for page in pages:
        # print(frames)
        if page not in frames:

            pageFaults += 1

            # Add page if the list is less than frameSize
            if len(frames) < frameSize:
                frames.append(page)

            # Remove first frame and add current frame to the end
            else:
                frames.pop(0)
                frames.append(page)

        # Removes page from list and adds it to the end
        else:
            frames.remove(page)
            frames.append(page)

    return pageFaults


def OPT(frames, pages):
    # Initialise page faults to 0 and LRUFrames as an empty array
    faults = 0
    OPTframes = []

    # Loop through each page reference in the list to check if the page is not in the frames
    for temp in range(len(pages)):
        if pages[temp] not in OPTframes:

            # If not in OPTframes add 1 to faults
            faults += 1

            # If length of OPTframes less than frames array append page to OPTframes
            if len(OPTframes) < frames:
                OPTframes.append(pages[temp])

            # Otherwise find least recently used element and replace it with the new page
            else:

                # Initialise upper and lower bounds
                OPTindex = -1  # -> Max future index set as -1
                TMPpage = OPTframes[0]  # -> Least used page == first page

                # Loops through all OPTframes
                for frame in OPTframes:

                    # Find the index of the frame in the list of future references
                    try:
                        index = pages[temp + 1:].index(frame)

                    # If frame not found in the future references, index set to the end of the list of references
                    except ValueError:
                        index = len(pages)

                    # If future index greater than maximum future index
                    # Update maximum future index and page to replace
                    if index > OPTindex:
                        OPTindex = index
                        TMPpage = frame

                # Replace the least recently used page at its index
                OPTframes[OPTframes.index(TMPpage)] = pages[temp]

    # Return number of page faults
    return faults


def main():
    pages = []
    size = int(sys.argv[1])

    # Check to see if size is valid input
    if size not in range(1, 8):
        print("Usage: Page Frame Size [1-7]")
        exit()

    # Create random page reference string
    for i in range(50):  ## Change this value for length of referance string
        pages.append(random.randint(0, 9))

    # print("Size: ", size, "\nPages:\n", pages, "\n")
    # print("FIFO: ", FIFO(3, (7, 0 , 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1)), "Page Faults.")
    # print("LRU: ", LRU(3, (7, 0 , 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1)), "Page Faults.")
    # print("OPT: ", OPT(3, (7, 0 , 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1)), "Page Faults.")

    print("FIFO:", FIFO(size, pages), "Page Faults.")
    print("LRU:", LRU(size, pages), "Page Faults.")
    print("OPT:", OPT(size, pages), "Page Faults.")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of page frames]")
        exit()
    else:
        main()
