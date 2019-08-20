class Car():
    def exclaim(self):
        print("I'm Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm Yugo!")

    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

print(give_me_a_yugo.need_a_push())