"""Music Box"""
class Song:
    def __init__(self, name: str, genre: str, duration: int):
        self.name = name
        self.genre = genre
        self.durations = duration
    
    def show_info(self):
        min, sec = self.durations // 60, self.durations % 60
        return f"{self.name} <|> {self.genre} <|> {min}.{sec:02}"

class DataNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        """init queue"""
        self.count = 0
        self.head = None

    def enqueue(self, item: Song):
        """Add node to last queue"""
        new_music = DataNode(item(input(), input(), int(input())))
        current = self.head
        while current is not None:
            current = current.next
        current = new_music
        self.count += 1

    def dequeue(self):
        """Pop node from head of queue"""
        if self.head is None:
            print("Underflow! peek from an empty queue")
            return 0
        rem = self.head
        self.head = self.head.next
        self.count -= 1
        print(f"Dequeue item: {rem.data.show_info()}")
        return rem

    def peek(self):
        """Return head of queue"""
        if self.head is None:
            print("Underflow! peek from an empty queue")
            return 0
        rem = self.head
        return rem

    def isEmpty(self):
        """If queue is empty"""
        if self.head is None:
            return True
        return False

    def show_Queue(self):
        """Show music queue"""
        if self.head is None:
            print("Queue is empty!")
            return 0
        current = self.head
        count = 1
        while current is not None:
            print(f"Queue#{count} {current.data.show_info()}")
            current = current.next
            count += 1

    def lastSong(self, time: int):
        """Last song when time is over"""
        if self.isEmpty():
            print("Nothing here! Please add some song")
            return 0
        current = self.head
        total_duration = 0
        while current:
            total_duration += current.data.duration
            current = current.next
        time %= total_duration
        current = self.head
        while time > 0:
            time -= current.data.duration
            if time <= 0:
                print(f"Queue#{self.count} {current.data.show_info()}")
            else:
                if current.next:
                    current = current.next
                else:
                    current = self.head

    def removeSong(self, name: str):
        """Remove song"""
        if self.isEmpty():
            print(f"Can not Delete! {name} is not exist")
            return 0
        current = self.head
        prev = None
        while current is not None:
            if current.data.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.count -= 1
                return 0
            prev = current
            current = current.next
        else:
            print(f"Can not Delete! {name} is not exist")
            return 0

    def groupSong(self):
        pass
    def undo(self):
        pass
    def rev_queue(self):
        pass

def main():
    """this is main function"""
    q = Queue()
    while (choice := input()) != "End":
        command, data = choice.split(": ")
        match command:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    temp.show_info()
            case "peek":
                temp= q.peek()
                if temp:
                    temp.show_info()
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            case "rev":
                q.rev_queue()
    q.show_Queue()
main()
