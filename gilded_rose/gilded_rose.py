class GildedRose(object):

    def __init__(self, items):
        self.items = items

    @staticmethod
    def increase_quality(item):
        item.quality += 1

    @staticmethod
    def decrease_quality(item):
        item.quality -= 1

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
                    self.decrease_quality(item)
            elif item.quality < 50:
                self.increase_quality(item)
                if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.quality < 50:
                    if item.sell_in < 11:
                        self.increase_quality(item)
                    if item.sell_in < 6:
                        self.increase_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        item.quality = item.quality - item.quality
                    if item.name != "Sulfuras, Hand of Ragnaros" and item.quality > 0:
                        self.decrease_quality(item)
                elif item.quality < 50:
                    self.increase_quality(item)
