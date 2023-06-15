class Cat:
    happiness = 40
    satiety = 40
    sleep = 'off'

    @classmethod
    def play_pet(cls):
        cls.satiety -= 10

        if cls.sleep == 'on':
            cls.sleep = 'off'
            cls.happiness -= 5
        else:
            cls.happiness += 10

    @classmethod
    def feed_pet(cls):
        if cls.sleep == 'on':
            return

        if cls.satiety > 100:
            cls.satiety = 100
            cls.happiness -= 30
            return

        cls.satiety += 15
        cls.happiness += 5

    @classmethod
    def sleep_pet(cls):
        cls.sleep = 'on'
        cls.happiness += 10
        cls.satiety -= 5