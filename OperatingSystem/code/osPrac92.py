from collections import deque

def fifo_page_replacement(pages, frames):
    memory = deque()
    hits, misses = 0, 0

    for page in pages:
        if page in memory:
            hits += 1
        else:
            misses += 1
            if len(memory) >= frames:
                memory.popleft()  # remove oldest
            memory.append(page)

    hit_ratio = hits / len(pages)
    miss_ratio = misses / len(pages)
    return hits, misses, hit_ratio, miss_ratio


def lru_page_replacement(pages, frames):
    memory = []
    hits, misses = 0, 0

    for page in pages:
        if page in memory:
            hits += 1
            memory.remove(page)   # move to most recently used
            memory.append(page)
        else:
            misses += 1
            if len(memory) >= frames:
                memory.pop(0)  # remove least recently used
            memory.append(page)

    hit_ratio = hits / len(pages)
    miss_ratio = misses / len(pages)
    return hits, misses, hit_ratio, miss_ratio


# Example usage
if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    print("Reference string:", reference_string)
    print("Frames:", frames)

    fifo_res = fifo_page_replacement(reference_string, frames)
    lru_res = lru_page_replacement(reference_string, frames)

    print("\nFIFO:")
    print(f"Hits: {fifo_res[0]}, Misses: {fifo_res[1]}, "
          f"Hit Ratio: {fifo_res[2]:.2f}, Miss Ratio: {fifo_res[3]:.2f}")

    print("\nLRU:")
    print(f"Hits: {lru_res[0]}, Misses: {lru_res[1]}, "
          f"Hit Ratio: {lru_res[2]:.2f}, Miss Ratio: {lru_res[3]:.2f}")
