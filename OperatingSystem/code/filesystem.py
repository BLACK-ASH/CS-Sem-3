import math

class FileSystem:
    def __init__(self, totalBlocks=20, blockSize=1):
        self.totalBlocks = totalBlocks
        self.blockSize = blockSize
        self.freeBlocks = [True] * totalBlocks  # True = free, False = occupied
        self.directory = {}  # filename -> {"size": size, "blocks": [block indices]}

    def allocateBlocks(self, numBlocks):
        """Allocate free blocks for a file."""
        allocated = []
        for i in range(self.totalBlocks):
            if self.freeBlocks[i]:
                allocated.append(i)
                if len(allocated) == numBlocks:
                    for blk in allocated:
                        self.freeBlocks[blk] = False
                    return allocated
        return None

    def create(self, filename, size):
        """Create a file with given size (in units)."""
        if filename in self.directory:
            print(f"Error: File '{filename}' already exists.")
            return

        numBlocks = math.ceil(size / self.blockSize)
        allocated = self.allocateBlocks(numBlocks)

        if allocated is None:
            print("Error: Not enough space to allocate file.")
        else:
            self.directory[filename] = {"size": size, "blocks": allocated}
            print(f"File '{filename}' created with blocks {allocated}")

    def read(self, filename):
        """Read file info."""
        if filename not in self.directory:
            print(f"Error: File '{filename}' not found.")
            return
        fileInfo = self.directory[filename]
        print(f"Reading file '{filename}':")
        print(f" -> Size: {fileInfo['size']} units")
        print(f" -> Blocks: {fileInfo['blocks']}")

    def delete(self, filename):
        """Delete a file and free its blocks."""
        if filename not in self.directory:
            print(f"Error: File '{filename}' not found.")
            return
        for blk in self.directory[filename]['blocks']:
            self.freeBlocks[blk] = True
        del self.directory[filename]
        print(f"File '{filename}' deleted successfully.")

    def showDirectory(self):
        """Show all files and their block allocations."""
        if not self.directory:
            print("Directory is empty.")
            return
        print("Directory contents:")
        for fname, info in self.directory.items():
            print(f" -> {fname}: size={info['size']}, blocks={info['blocks']}")

    def showFreeBlocks(self):
        """Show free/used block status."""
        print("Block allocation status:")
        print("".join(["F" if free else "U" for free in self.freeBlocks]))


# Example usage
if __name__ == "__main__":
    fs = FileSystem(totalBlocks=10, blockSize=1)
    fs.create("file1", 3)
    fs.create("file2", 4)
    fs.showDirectory()
    fs.showFreeBlocks()
    fs.read("file1")
    fs.delete("file1")
    fs.showDirectory()
    fs.showFreeBlocks()
