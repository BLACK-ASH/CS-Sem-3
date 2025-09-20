from collections import deque

def fifo_page_replacement(pages, frames):
    memory = deque()
    hits, misses = 0, 0

    print("\n--- FIFO Page Replacement ---")
    for page in pages:
        if page in memory:
            hits += 1
        else:
            misses += 1
            if len(memory) >= frames:
                memory.popleft()  # Remove oldest page (FIFO)
            memory.append(page)
        print(f"Page: {page} -> Memory: {list(memory)}")

    print(f"\nFIFO Results: Hits = {hits}, Misses = {misses}, "
          f"Hit Ratio = {hits/len(pages):.2f}, Miss Ratio = {misses/len(pages):.2f}")


def lru_page_replacement(pages, frames):
    memory = deque()
    hits, misses = 0, 0

    print("\n--- LRU Page Replacement ---")
    for page in pages:
        if page in memory:
            hits += 1
            memory.remove(page)   # Remove old position
            memory.append(page)   # Move to most recently used
        else:
            misses += 1
            if len(memory) >= frames:
                memory.popleft()  # Remove least recently used
            memory.append(page)
        print(f"Page: {page} -> Memory: {list(memory)}")

    print(f"\nLRU Results: Hits = {hits}, Misses = {misses}, "
          f"Hit Ratio = {hits/len(pages):.2f}, Miss Ratio = {misses/len(pages):.2f}")


if __name__ == "__main__":
    # Example page reference string
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    print("Reference String:", reference_string)
    print("Frames:", frames)

    fifo_page_replacement(reference_string, frames)
    lru_page_replacement(reference_string, frames)
