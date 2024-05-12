import random
class Saturday:
    def __init__(self):
        self.sleep = self._sleep()
        next(self.sleep)
        self.eat = self._eat()
        next(self.eat)
        self.play = self._play()
        next(self.play)
        self.take_trash = self._take_trash()
        next(self.take_trash)
        self.cur_state = self.sleep
        self.time = 0
        self.requested_time = 0

    def send(self, time) -> None:
        if not time or time not in range(24):
            raise ValueError("time should be an integer in 24 hour range")
        if time <= self.time:
            raise ValueError("time should move forward")
        self.cur_state.send(time)


    def _sleep(self):
        while True:
            time = yield
            if time < 8:
                print("I should sleep a little bit more")
                continue
            self.time = 8
            print("time to eat")
            self.cur_state = self.eat
            if time > 8:
                self.send(time)

    def _eat(self):
        while True:
            time = yield
            self.time = 9
            print("It is time to play")
            self.cur_state = self.play
            if time > 9:
                self.send(time)

    def _play(self):
        while True:
            time = yield
            self.time = 9
            if time in range(10, 13) and random.random() > 0.05:
                print("Trash should be taken out")
                self.cur_state = self.take_trash

    def _take_trash(self):
        while True:
            time = yield
            self.time += 1
            self.cur_state = self.play





day = Saturday()
day.send(10)
# day.send(11)